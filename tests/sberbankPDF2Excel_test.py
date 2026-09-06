from pathlib import Path

import pytest
import pandas as pd

from Sberbank2Excel import exceptions
from Sberbank2Excel.sberbankPDF2Excel import sberbankPDF2Excel
from Sberbank2Excel.extractor_SBER_PAYMENT_DEBIT_2604b import SBER_PAYMENT_DEBIT_2604b


"""
no_github_module.py contains information, which is not shared via github due to confidential nature

Its structure is following:

SBER_DEBIT_old_not_supported_pdf = r"Path to some file on the drive"

SBER_DEBIT_2005_pdf = r"Path to some other file on the drive"
...

"""

HERE = Path(__file__).parent 

TEST_DATA: Path = HERE / "test_data" # A directory with test data files


@pytest.mark.private
def test_correctly_converts_SBER_CREDIT_2110_txt():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_CREDIT_2110_file_name_text)

class Test_SBER_DEBIT_2107:

    @pytest.mark.private
    def test_correctly_converts_SBER_DEBIT_2107_pdf(self):
        from . import no_github_module
        sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2107_pdf)
        
    def test_correctly_converts_SBER_DEBIT_2107_txt_anonim(self):
        sberbankPDF2Excel(str(TEST_DATA / "_SBER_DEBIT_2107_anonymized_reduced.txt"))

    @pytest.mark.private
    def test_correctly_converts_SBER_DEBIT_2107_Tinkoff_problem_pdf(self):
        from . import no_github_module
        sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2107_Tinkoff_problem_pdf)

@pytest.mark.private
def test_correctly_balance_error_SBER_DEBIT_2107_pdf():
    from . import no_github_module
    with pytest.raises(exceptions.BalanceVerificationError):
        sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2107_wrong_balance_txt)

@pytest.mark.private
def test_correctly_converts_SBER_DEBIT_2005_pdf():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2005_pdf)

@pytest.mark.private
def test_correctly_does_not_convert_SBER_DEBIT_old_not_supported():
    from . import no_github_module
    with pytest.raises(exceptions.InputFileStructureError):
        sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_old_not_supported_pdf)

@pytest.mark.private
def test_correctly_converts_SBER_PAYMENT_2208_txt():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_PAYMENT_2208_txt)

@pytest.mark.private
def test_correctly_converts_SBER_PAYMENT_2212_pdf():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_PAYMENT_2212_pdf)

@pytest.mark.private
def test_correctly_converts_SBER_DEBIT_2212_pdf():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2212_pdf)

@pytest.mark.private
def test_correctly_converts_SBER_SAVING_2303_EURO_pdf():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_SAVING_2303_EURO_pdf)

@pytest.mark.private
def test_correctly_converts_SBER_SAVING_2303_USD_pdf():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_SAVING_2303_USD_pdf)

@pytest.mark.private    
def test_correctly_converts_SBER_DEBIT_2303_CHELYABINSK_pdf():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2303_CHELYABINSK_pdf)

@pytest.mark.private
def test_correctly_converts_SBER_PAYMENT_2212_issue_31_simulation_txt():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_PAYMENT_2212_issue_31_simulation_txt)

@pytest.mark.private    
def test_correctly_converts_SBER_DEBIT_2212_issue_33_txt():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2212_issue_33_txt)

@pytest.mark.private
def test_correctly_converts_SBER_SAVING_2303_Activnoe_dolgolitie_issue_35_txt():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_SAVING_2303_Activnoe_dolgolitie_issue_35_txt)

@pytest.mark.private    
def test_correctly_converts_SBER_DEBIT_2212_issue_36_txt():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2212_issue_36_txt)

@pytest.mark.private    
def test_correctly_converts_SBER_DEBIT_2212_theoretical_case_for_issue_36_manually_created_line_22_txt():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2212_issue_36_theoretical_case_txt)

@pytest.mark.private    
def test_correctly_converts_SBER_DEBIT_2212_v20240413_issue_39():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2212_v20240413_issue_39)

@pytest.mark.private    
def test_correctly_converts_SBER_PAYMENT_2406_20231001_20240628_issue_42():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_PAYMENT_2406_20231001_20240628_issue_42)

# SBER_PAYMENT_2407__MIR_20240803__20240101_20240801_issue_44

@pytest.mark.private
def test_correctly_converts_SBER_PAYMENT_2407__MIR_20240803__20240101_20240801_issue_44():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_PAYMENT_2407__MIR_20240803__20240101_20240801_issue_44)

@pytest.mark.private    
def test_correctly_converts_SBER_PAYMENT_2407_issue52():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_PAYMENT_2407_issue52)

@pytest.mark.private    
def test_correctly_converts_SBER_SAVING2407_issue47():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_SAVING_2407_issue47)

@pytest.mark.private    
def test_correctly_converts_SBER_DEBIT_2408_issue_48():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2408_issue_48)
    
class Test_SBER_CREDIT_2409:    
    
    @pytest.mark.private
    def test_correctly_converts_SBER_CREDIT_2409_issue_50(self):
        from . import no_github_module
        sberbankPDF2Excel(no_github_module.path2_SBER_CREDIT_2409_issue_50)
    
    @pytest.mark.private    
    def test_correctly_converts_SBER_CREDIT_2409_issue_54(self):
        from . import no_github_module
        sberbankPDF2Excel(no_github_module.path2_SBER_CREDIT_2409_issue_54)
    
    @pytest.mark.private    
    def test_does_not_convert_wrong_SBER_CREDIT_2409_issue_54(self):
        from . import no_github_module
        with pytest.raises(RuntimeError) as excinfo:
            sberbankPDF2Excel(no_github_module.path2_SBER_CREDIT_2409_issue_54_wrong)
            
        assert isinstance(excinfo.value.__cause__, exceptions.InputFileStructureError)

    @pytest.mark.private
    def test_correctly_converts_SBER_CREDIT_2409_issue_56_simulated_txt(self):
        from . import no_github_module
        sberbankPDF2Excel(no_github_module.path2_SBER_CREDIT_2409_issue_56_simulated_txt)

@pytest.mark.private    
def test_correctly_converts_SBER_DEBIT_2510_issue_69():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2510_issue_69)
    
@pytest.mark.private    
def test_correctly_converts_SBER_PAYMENT_2510():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_PAYMENT_2510_issue70)
    
class Test_SBER_CREDIT_2511:
    @pytest.mark.private
    def test_correctly_converts_SBER_CREDIT_2511_pdf(self):
        from . import no_github_module
        sberbankPDF2Excel(no_github_module.path2_SBER_CREDIT_2511_pdf)
        
    @pytest.mark.private
    def test_correctly_converts_SBER_CREDIT_2511_simulate_local_currency(self):
        from . import no_github_module
        sberbankPDF2Excel(no_github_module.path2_SBER_CREDIT_2511_simulate_local_currency)
        
    @pytest.mark.private
    def test_correctly_converts_SBER_CREDIT_2511_simulate_more_lines(self):
        from . import no_github_module
        sberbankPDF2Excel(no_github_module.path2_SBER_CREDIT_2511_simulate_more_lines)
        
    @pytest.mark.private
    def test_correctly_converts_SBER_CREDIT_2511_issue_79(self):
        from . import no_github_module
        sberbankPDF2Excel(no_github_module.path2_SBER_CREDIT_2511_issue_79)

@pytest.mark.private    
def test_correctly_converts_SBER_DEBIT_2603_issue_80():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_DEBIT_2603_issue_80)

@pytest.mark.private
def test_correctly_converts_SBER_PAYMENT_2604_issue_81():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_PAYMENT_2604_issue_81)
    
@pytest.mark.private
def test_correctly_converts_SBER_SAVING_2604_issue_82():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2__SBER_SAVING_2604_issue_82)

@pytest.mark.private
def test_correctly_converts_SBER_PAYMENT_2604b_issue_83():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_PAYMENT_2604b_issue_83)

@pytest.mark.private
def test_correctly_converts_SBER_PAYMENT_DEBIT_2604b_debit_issue84():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_PAYMENT_DEBIT_2604b_debit_issue84)
    
@pytest.mark.private
def test_correctly_converts_SBER_PAYMENT_DEBIT_2604b_payment_issue87():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_PAYMENT_DEBIT_2604b_payment_issue87)
    
@pytest.mark.private
def test_correctly_converts_SBER_CREDIT_2605_issue87():
    from . import no_github_module
    sberbankPDF2Excel(no_github_module.path2_SBER_CREDIT_2605_issue87)


class Test_SBER_PAYMENT_DEBIT_2604b:

    ENTRY_INCOME_INTEGER = (
        "05.09.2026\t19:27\tВнесение наличных\t+47 200,00\t75 661,14\n"
        "05.09.2026\t164041\tATM 60005717 TVER RUS. Операция по карте ****4321"
    )

    ENTRY_INCOME_FRACTION = (
        "31.08.2026\t19:34\tПеревод СБП\t+104,78\t36 720,14\n"
        "31.08.2026\t499148\tПеревод из Alfa-Bank. Операция по карте ****4321"
    )

    ENTRY_EXPENSE_INTEGER = (
        "04.09.2026\t22:20\tПеревод СБП\t1 000,00\t26 461,14\n"
        "04.09.2026\t839553\tПеревод в T-Bank. Операция по карте ****4321"
    )

    ENTRY_EXPENSE_FRACTION = (
        "04.09.2026\t12:04\tПеревод с карты\t600,60\t27 128,14\n"
        "04.09.2026\t205945\tПеревод для Л. Михаил Игоревич. Операция по карте\n"
        "****4321"
    )

    ENTRY_NAME_2_LINES = (
        "04.09.2026\t12:04\tПеревод с карты\t600,00\t27 128,14\n"
        "04.09.2026\t205945\tПеревод для К. Анна Павловна. Операция по карте ****4321"
    )

    ENTRY_NAME_3_LINES = (
        "04.09.2026\t12:04\tПеревод с карты\t600,00\t27 128,14\n"
        "04.09.2026\t205945\tПеревод для К. Анна Павловна. Операция по карте\n"
        "****4321"
    )

    ENTRY_NO_NAME = (
        "04.09.2026\t22:20\tПеревод СБП\t1 000,00\t26 461,14\n"
        "04.09.2026\t839553\tПеревод в T-Bank. Операция по карте ****4321"
    )

    def _extractor(self) -> SBER_PAYMENT_DEBIT_2604b:
        txt = (TEST_DATA / "_SBER_PAYMENT_DEBIT_2604b_anonymized_reduced.txt").read_text(encoding='utf-8')
        return SBER_PAYMENT_DEBIT_2604b(txt)

    def test_income_is_positive_integer(self):
        result = self._extractor().decompose_entry_to_dict(self.ENTRY_INCOME_INTEGER)
        assert result['income'] == 47200
        assert result['expense'] is None

    def test_income_fraction_rounded(self):
        result = self._extractor().decompose_entry_to_dict(self.ENTRY_INCOME_FRACTION)
        assert result['income'] == 105
        assert result['expense'] is None

    def test_expense_is_unsigned_integer(self):
        result = self._extractor().decompose_entry_to_dict(self.ENTRY_EXPENSE_INTEGER)
        assert result['expense'] == 1000
        assert result['income'] is None

    def test_expense_fraction_rounded(self):
        result = self._extractor().decompose_entry_to_dict(self.ENTRY_EXPENSE_FRACTION)
        assert result['expense'] == 601
        assert result['income'] is None

    def test_accounting_date_equals_operation_date(self):
        result = self._extractor().decompose_entry_to_dict(self.ENTRY_INCOME_INTEGER)
        assert result['accounting_date'] == result['operation_date'] == "05.09.2026"

    def test_name_reordered(self):
        result = self._extractor().decompose_entry_to_dict(self.ENTRY_NAME_2_LINES)
        assert result['name'] == "Анна Павловна К."

    def test_name_empty_when_no_person(self):
        extractor = self._extractor()
        result = extractor.decompose_entry_to_dict(self.ENTRY_NO_NAME)
        assert result['name'] == ""

    def test_name_from_multiline_description(self):
        result = self._extractor().decompose_entry_to_dict(self.ENTRY_NAME_3_LINES)
        assert result['name'] == "Анна Павловна К."

    def test_columns_info_exact(self):
        extractor = self._extractor()
        expected = {'operation_date': 'Дата операции',
                    'accounting_date': 'Дата учёта',
                    'income': 'Приход',
                    'expense': 'Расход',
                    'name': 'Имя',
                    'value_account_currency': 'value_account_currency'}
        assert extractor.get_columns_info() == expected
        assert list(extractor.get_columns_info().keys()) == list(expected.keys())

    def test_balance_column_name(self):
        assert self._extractor().get_column_name_for_balance_calculation() == 'value_account_currency'

    def test_internal_columns(self):
        assert self._extractor().get_internal_columns() == ['value_account_currency']

    def test_correctly_converts_SBER_PAYMENT_DEBIT_2604b_txt_anonim(self):
        sberbankPDF2Excel(str(TEST_DATA / "_SBER_PAYMENT_DEBIT_2604b_anonymized_reduced.txt"))

    def test_output_file_has_exact_five_columns(self):
        output_stem = sberbankPDF2Excel(
            str(TEST_DATA / "_SBER_PAYMENT_DEBIT_2604b_anonymized_reduced.txt"))
        df = pd.read_excel(output_stem + ".xlsx")

        assert list(df.columns) == ['Дата операции', 'Дата учёта', 'Приход', 'Расход', 'Имя']

        first = df.iloc[0]
        assert first['Дата операции'] == '05.09.2026'
        assert first['Дата учёта'] == '05.09.2026'
        assert first['Приход'] == 47200
        assert pd.isna(first['Расход'])  # empty cell when the entry is income


if __name__ == "__main__":
    print("Running tests")
