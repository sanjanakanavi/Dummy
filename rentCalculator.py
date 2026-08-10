# Rent Calculator
total_rent = int(input("Enter the total rent amount: "))
food_ordered =  int(input("Enter the total food ordered amount: "))
electricity_unit_spent = int(input("Enter the total electricity unit spent: "))
charge_per_unit = int(input("Enter the charge per unit of electricity: "))
total_tenants = int(input("Enter the total number of tenants: "))

total_electricity_bill = electricity_unit_spent * charge_per_unit
rent_per_tenant = (total_rent + food_ordered + total_electricity_bill) // total_tenants
print(f"Rent per tenant: {rent_per_tenant}")



