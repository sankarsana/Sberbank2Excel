# NESSY.md — Sberbank2Excel

Инструкционный контекст для работы с этим репозиторием.

## Обзор проекта

**Sberbank2Excel** — расширяемая утилита для конвертации выписок Сбербанка из формата PDF в Excel/CSV. Восполняет отсутствие у Сбербанка выгрузки в CSV. Работает на Windows, macOS и Linux.

- Язык: **Python** (строго `==3.12.*`).
- Пакетный менеджер: **uv** (рекомендуется), сборка через `setuptools`.
- Зависимости: `pdfminer.six`, `pandas`, `Unidecode`, `XlsxWriter`. Dev: `pytest`, `pyinstaller`.
- Точка входа (entry point): `sberbank2Excel` → `Sberbank2Excel.sberbank2Excel:main`.
  - Без аргументов → GUI (`sberbankPDF2ExcelGUI`).
  - С аргументами → CLI (`sberbankPDF2Excel`).
- Все строковые литералы и docstring'и в коде — на русском. Приветствуется сохранять этот стиль.

## Архитектура / поток конвертации

Конвейер трёхэтапный: PDF → промежуточный текст → Excel/CSV.

```
PDF ──► (pdf2txtev.py) ──► .txt ──► (sberbankPDFtext2Excel.py) ──► .xlsx/.csv
```

Ключевые модули в `src/Sberbank2Excel/`:

| Модуль | Роль |
|--------|------|
| `sberbank2Excel.py` | Точка входа; диспетчер CLI/GUI. |
| `sberbankPDF2Excel.py` | Оркестратор: PDF→txt (через `pdf2txtev`), затем txt→Excel. Удаляет промежуточный .txt, если не указано иначе. |
| `pdf2txtev.py` | Конвертация PDF→текст на базе `pdfminer.six`. Переделка `extract_text` для обхода [pdfminer issue #466](https://github.com/pdfminer/pdfminer.six/issues/466) (не смешивает строки выписки). |
| `sberbankPDFtext2Excel.py` | Ядро: читает txt, определяет экстрактор, строит DataFrame, сверяет баланс, пишет файл. |
| `extractor.py` | Абстрактный базовый класс `Extractor` (ABC) — все экстракторы наследуют его. |
| `extractors.py` | Реестр: список `extractors_list` всех доступных классов экстракторов. Правится при добавлении нового формата. |
| `extractors_generic.py` | `determine_extractor_auto` (автоопределение формата) и `debug_extractor` (самотестирование экстрактора). |
| `extractor_SBER_*.py` | По одному модулю на формат выписки (например `extractor_SBER_CREDIT_2110.py`). |
| `utils.py` | Хелперы: парсинг денег в `Decimal`, работа с DataFrame, проверка баланса, запись файла. |
| `exceptions.py` | Иерархия исключений (см. ниже). |
| `version_info.py` | Версия/имя/ссылки из метаданных пакета. |
| `debug.py` | Отладочные утилиты. |

### Абстрактный класс `Extractor` (`extractor.py`)

Каждый экстрактор обязан реализовать:

- `check_specific_signatures()` — бросает `exceptions.InputFileStructureError()`, если текст не подходит.
- `get_period_balance() -> Decimal` — баланс периода из шапки выписки.
- `split_text_on_entries() -> list[str]` — разбивает текст на отдельные транзакции (записи).
- `decompose_entry_to_dict(entry) -> dict | list[dict]` — разбирает запись в словарь. Все деньги → `Decimal`, все даты → `datetime`. Возврат списка поддерживает случаи вроде [issue #51](https://github.com/Ev2geny/Sberbank2Excel/issues/51).
- `get_column_name_for_balance_calculation() -> str` — имя колонки для сверки баланса (обычно `value_account_currency`).
- `get_columns_info() -> dict` — отображение «ключ словаря → имя колонки в Excel» в нужном порядке. Ключи должны соответствовать ключам из `decompose_entry_to_dict`.
- `get_internal_columns() -> list[str]` — (по умолчанию `[]`) колонки, используемые во внутренних расчётах (например сверка баланса), но не попадающие в итоговый файл.

Готовые методы: `check_support()`, `get_entries()`.

### Сверка баланса

В `sberbankPDFtext2Excel.sberbankPDFtext2Excel`: вычисленный из шапки баланс сравнивается с суммой колонки транзакций (`utils.check_transactions_balance`). При расхождении — `exceptions.BalanceVerificationError`, и по умолчанию файл **не создаётся** (флаг `-b`/`perform_balance_check=False` это отключает).

Internal-колонки (`get_internal_columns()`) остаются в DataFrame для расчётов, но удаляются перед записью в файл.

### Исключения (`exceptions.py`)

- `Bank2ExcelError` — базовое.
- `InputFileStructureError` — текст не соответствует формату.
- `BalanceVerificationError` — расхождение балансов.
- `UserInputError` — неверный ввод пользователя.
- `TestingError` — используется в самопроверках.

## Добавление нового формата выписки

Подробно в `CONTRIBUTING.md`. Кратко:

1. **Создать** `src/Sberbank2Excel/extractor_SBER_XXXX.py` — скопировать ближайший существующий экстрактор, переименовать класс (наследует `Extractor`), реализовать/скорректировать абстрактные методы.
2. **Зарегистрировать** класс в `src/Sberbank2Excel/extractors.py` (добавить импорт + `extractors_list.append(...)`).
3. **Документация**: при PR добавить анонимизированный скриншот в `docs/format_examples/` и строку в таблицу README.

Отладка изолированного экстрактора (модуль с `if __name__ == '__main__':` запускает `extractors_generic.debug_extractor`):

```
py extractor_SBER_XXXX.py <bank_extract_converted_to_txt.txt>
```

Функция `debug_extractor` сама проверяет все методы и печатает WARNINGS.

## Сборка и запуск

### Установка из исходников (dev)

```bash
python3.12 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\Activate
git switch develop               # ветка разработки
python -m pip install -e .[dev]
```

### Запуск

```bash
# GUI
python -m Sberbank2Excel.sberbank2Excel        # или команда: sberbank2Excel

# CLI (справка)
sberbank2Excel -h
```

CLI-аргументы: `-o/--output`, `-b/--balcheck`, `-f/--format`, `-t/--type {xlsx,csv}`, `-r/--reverse`, `-i/--interm`, позиционный `input_file_name`.

### Сборка .exe (PyInstaller)

```bash
pyinstaller src/Sberbank2Excel/sberbank2Excel.py
# результат в dist/
```

Есть готовые спеки: `sberbank2Excel.spec`, `sberbankPDF2ExcelGUI.spec`.

## Тестирование

Фреймворк: **pytest**. Конвенции:

- Маркер `private` — тесты, требующие приватных выписок (есть только у автора), не включаются в обычный прогон.
- Публичный (без приватных данных) прогон:
  ```bash
  python -m pytest -m "not private"
  ```
  После прогона в `tests/test_data/` должны появляться `.xlsx`.
- Публичный тест: `tests/sberbankPDF2Excel_test.py` → `Test_SBER_DEBIT_2107.test_correctly_converts_SBER_DEBIT_2107_txt_anonim` (использует `tests/test_data/_SBER_DEBIT_2107_anonymized_reduced.txt`).
- Приватные тесты опираются на `tests/no_github_module.py` (в git не попадает, содержит пути к приватным выпискам). Новые приватные тесты добавляются рядом по образцу.
- Паттерн имен тестов: `test_correctly_converts_<FORMAT>_...`, `test_does_not_convert_wrong_...`, ссылки на GitHub issues в имени (например `_issue_51`).

## Конвенции разработки

- **Код и комментарии** — docstring'и и сообщения на русском (включая сообщения об ошибках).
- **Деньги** — всегда `Decimal` (парсинг через `utils.get_decimal_from_money`).
- **Даты/время** — `datetime.datetime`.
- Ключи словаря `decompose_entry_to_dict` ↔ `get_columns_info` должны совпадать (`debug_extractor` это проверяет).
- Промежуточный текстовый файл разделяется **табуляцией** (`split_Sberbank_line`), табы от пробелов отличаются — важно при анонимизации.
- Поддержка иностранной валюты и многолинейных записей — типовые случаи в экстракторах.
- Ветки для PR: `git switch -c issue_xxx`.