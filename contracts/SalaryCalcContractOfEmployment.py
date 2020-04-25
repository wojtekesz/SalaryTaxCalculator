from contracts.ContractTemplate import ContractTemplate


class SalaryCalcContractOfEmployment(ContractTemplate):
    # przyjęto, że kwota podstawy wynagrodzenia w skali roku nie przekroczy 85 528 zł oraz że pracownik pracuje w miejscu zamieszkania

    # metoda wykonawcza
    def execute(self):
        basis_of_health_insurance = self.calc_basis_of_health_insurance()
        healthcare_contribution_total = self.calc_healthcare_contribution_total(
            basis_of_health_insurance)
        healthcare_contribution_subtracted = self.calc_healthcare_contribution_subtracted(
            basis_of_health_insurance)
        tax_base = self.calc_tax_base(
            basis_of_health_insurance)
        income_tax = self.calc_income_tax(
            tax_base)
        income_tax_reduced = self.calc_income_tax_reduced(
            income_tax)
        advance_for_income_tax = self.calc_advance_for_income_tax(
            income_tax_reduced, healthcare_contribution_subtracted)
        return round(self.calc_net_salary(basis_of_health_insurance, healthcare_contribution_total, advance_for_income_tax), 2)
