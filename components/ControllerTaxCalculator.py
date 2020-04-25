class ControllerTaxCalculator():

    def __init__(self, input_request):
        self.salary_with_tax = input_request.input_salary_with_tax()
        self.contract_type = input_request.input_contract_type()

# Weryfikowanie poprawności wprowadzonych danych wynagrodzenia
    def is_int_or_float_salary_with_tax(self):
        try:
            self.salary_with_tax = float(self.salary_with_tax)
        except ValueError:
            print('\nUruchom skrypt ponownie i podaj liczbę')
            exit()

# Weryfikowanie czy podane wynagrodzenie jest wartością dodatnią
    def is_negative_salary_with_tax(self):
        if self.salary_with_tax < 0:
            print(
                'Uruchom skrypt ponownie i podaj wynagrodzenie dodatnie.\nPS. Aż tak źle chyba nie jest ;)')
            exit()

# Wybieranie odpowiedniego algorytmu obliczeń wynagrodzenia netto w zależności od rodzaju umowy
    def switch_proper_calculator(self):
        if self.contract_type == 'P':
            from contracts.SalaryCalcContractOfEmployment import SalaryCalcContractOfEmployment
            return SalaryCalcContractOfEmployment(self.salary_with_tax).execute()
        elif self.contract_type == 'Z':
            from contracts.SalaryCalcContractOfMandate import SalaryCalcContractOfMandate
            return SalaryCalcContractOfMandate(self.salary_with_tax).execute()
        elif self.contract_type == 'D':
            from contracts.SalaryCalcContractOfSpecificWork import SalaryCalcContractOfSpecificWork
            return SalaryCalcContractOfSpecificWork(self.salary_with_tax).execute()
        else:
            print('Uruchom skrypt ponownie i podaj prawidłowy rodzaj umowy')
            exit()
