
# Progressive Electricity Billing System

bills = []
months = []

def calculate_bill(units):

    
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    
    fixed_charge = 50

    subtotal = energy_charge + fixed_charge

    
    surcharge = 0
    rebate = 0

    if units > 300:
        surcharge = subtotal * 0.05

    elif units < 100:
        rebate = subtotal * 0.05

    final_bill = subtotal + surcharge - rebate

    return energy_charge, fixed_charge, surcharge, rebate, final_bill

n = int(input("Enter number of months: "))

for i in range(n):

    print("\nMonth", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units: "))

    if units < 0:
        print("Invalid units!")
        continue

    energy, fixed, surcharge, rebate, bill = calculate_bill(units)

    months.append(month)
    bills.append(bill)

    print("Energy Charge: Rs.", round(energy, 2))
    print("Fixed Charge: Rs.", round(fixed, 2))
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Final Bill: Rs.", round(bill, 2))

print("\n===== MONTHLY BILL COMPARISON =====")

for i in range(len(bills)):

    print(months[i], ": Rs.", round(bills[i], 2))

    if i > 0:

        increase = bills[i] - bills[i - 1]

        if bills[i - 1] > 0:
            percentage = (increase / bills[i - 1]) * 100
        else:
            percentage = 0

        print("Bill Change:", round(percentage, 2), "%")

        if percentage > 30:
            print("WARNING: Unusual increase detected!")

        else:
            print("Normal bill change.")


total = sum(bills)

print("\nTotal Electricity Bill: Rs.", round(total, 2))

if bills:
    print("Average Monthly Bill: Rs.", round(total / len(bills), 2))

