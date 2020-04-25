from contracts.ContractTemplate import ContractTemplate


class SalaryCalcContractOfSpecificWork(ContractTemplate):
    # przyjęto, że kwota podstawy wynagrodzenia w skali roku nie przekroczy 85 528 zł oraz że pracownik pracuje w miejscu zamieszkania

    # Obliczanie kosztów uzyskania przychodu
    def calc_tax_deductible_cost(self):
        return self.gross_salary * self.coefficient_tax_deductible_cost

# Obliczanie podstawy do opodatkowania
    def calc_tax_base(self, tax_deductible_cost):
        return round(self.gross_salary - tax_deductible_cost, 0)

# Obliczanie podatku dochodowego
    def calc_income_tax(self, tax_base):
        return round(tax_base * self.coefficient_income_tax, 0)

# Obliczanie wynagrodzenia netto
    def calc_net_salary(self, income_tax):
        return self.gross_salary - income_tax

# Metoda wykonawcza
    def execute(self):
        tax_deductible_cost = self.calc_tax_deductible_cost()
        tax_base = self.calc_tax_base(
            tax_deductible_cost)
        income_tax = self.calc_income_tax(
            tax_base)
        return self.calc_net_salary(income_tax)
