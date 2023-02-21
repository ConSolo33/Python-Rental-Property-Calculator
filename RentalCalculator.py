class RentalCalculator():
    
    def __init__(self):
        self = self

    def calculateIncome(self):
        print("What is the total monthly income from this property?")
        rental_income = int(input("Rental Income: $"))
        laundry_income = int(input("Laundry Income: $"))
        storage_income = int(input("Storage Income: $"))
        misc_income = int(input("Misc. Income: $"))
        total_income = rental_income + laundry_income + storage_income + misc_income
        return total_income

    def calculateExpenses(self):
        print("What are the total monthly expenses from this property?")
        taxes = int(input("Taxes: $"))
        insurance = int(input("Insurance: $"))
        utilities = int(input("Utilities: $"))
        repairs = int(input("Repairs: $"))
        mortgage = int(input("Mortgage: $"))
        total_expenses = taxes + insurance + utilities + repairs + mortgage
        return total_expenses

    def calculateInvestment(self):
        print("What is your total investment for this property?")
        down_payment = int(input("Down Payment: $"))
        closing_cost = int(input("Closing Costs: $"))
        rehab = int(input("Rehab Costs: $"))
        misc_investments = int(input("Misc: $"))
        total_investment = down_payment + closing_cost + rehab + misc_investments
        return total_investment
    
    def run(self):
        annual_cash_flow = (RentalCalculator.calculateIncome(self) - RentalCalculator.calculateExpenses(self)) * 12
        ROI = (annual_cash_flow / RentalCalculator.calculateInvestment(self)) * 100
        print(f"Your Cash on Cash ROI for this property is: {ROI}%")


condo = RentalCalculator()
condo.run()


        
    











    