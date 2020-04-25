class ContractTemplate():

    def __init__(self, gross_salary):
        self.gross_salary = gross_salary
        self.coefficient_pension_contribution = 0.0976
        self.coefficient_disability_pension_contribution = 0.015
        self.coefficient_sickness_contribution = 0.0245
        self.coefficient_healthcare_contribution_total = 0.09
        self.coefficient_healthcare_contribution_reduced = 0.0775
        self.tax_deductible_cost = 250
        self.taxfree_amount = 43.76
        self.coefficient_income_tax = 0.17
        self.coefficient_tax_deductible_cost = 0.2

# Obliczenie podstawy ubezpieczenia zdrowotnego 
    def calc_basis_of_health_insurance(self):
        return self.gross_salary * (1 - (self.coefficient_pension_contribution + self.coefficient_disability_pension_contribution + self.coefficient_sickness_contribution))

# Obliczanie składki zdrowotnej całej
    def calc_healthcare_contribution_total(self, basis_of_health_insurance):
        return round(basis_of_health_insurance * self.coefficient_healthcare_contribution_total, 2)

# Obliczanie składki zdrowotnej podlegającej odliczeniu
    def calc_healthcare_contribution_subtracted(self, basis_of_health_insurance):
        return round(basis_of_health_insurance * self.coefficient_healthcare_contribution_reduced, 0)

# Obliczanie podstawy opodatkowania
    def calc_tax_base(self, basis_of_health_insurance):
        return round(basis_of_health_insurance - self.tax_deductible_cost, 0)

# Obliczanie podatku dochodowego
    def calc_income_tax(self, tax_base):
        return tax_base * self.coefficient_income_tax

# Obliczanie podatku dochodowego pomniejszonego o kwote wolna od podatku
    def calc_income_tax_reduced(self, income_tax):
        return income_tax - self.taxfree_amount

# Obliczanie zaliczki na podatek dochodowy
    def calc_advance_for_income_tax(self, income_tax_reduced, healthcare_contribution_subtracted):
        return round(income_tax_reduced - healthcare_contribution_subtracted, 0)
        
# Obliczanie wynagrodzenia netto
    def calc_net_salary(self, basis_of_health_insurance, healthcare_contribution_total, advance_for_na_income_tax):
        return (basis_of_health_insurance - healthcare_contribution_total - advance_for_na_income_tax)

# Obliczanie kosztu uzyskania przychodu
    def calc_tax_deductible_cost(self, basis_of_health_insurance):
        return basis_of_health_insurance * self.coefficient_tax_deductible_cost

