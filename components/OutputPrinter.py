
class OutputPrinter():

    # Metoda zwracająca pełną nazwę rodzaju umowy
    def return_full_name_of_contract_type(self, contract_type):
        if contract_type == 'P':
            return 'UMOWA O PRACĘ'
        elif contract_type == 'D':
            return 'UMOWA O DZIEŁO'
        elif contract_type == 'Z':
            return 'UMOWA ZLECENIE'
        else:
            None

    # Wyświetlanie wyników
    def print_results(self, salary_with_tax, salary_without_tax, full_name_of_contract_type):
        print('-' * 45, '\nTwoje wynagrodzenie brutto wynosi {}.\nPracujesz na podstawie {}.\nTwoje wynagrodzenie netto wynosi {}\n'.format(
            salary_with_tax, full_name_of_contract_type, salary_without_tax), '-' * 45)
