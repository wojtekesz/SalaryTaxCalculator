def main():
    from components.ControllerTaxCalculator import ControllerTaxCalculator
    from components.InputAdapter import InputAdapter
    a = ControllerTaxCalculator(InputAdapter)
    a.is_int_or_float_salary_with_tax()
    a.is_negative_salary_with_tax()
    salary_without_tax = a.switch_proper_calculator()
    from components.OutputPrinter import OutputPrinter
    full_name_of_contract_type = OutputPrinter().return_full_name_of_contract_type(
        a.contract_type)
    return OutputPrinter().print_results(a.salary_with_tax,
                                         salary_without_tax, full_name_of_contract_type)


if __name__ == '__main__':
    main()
