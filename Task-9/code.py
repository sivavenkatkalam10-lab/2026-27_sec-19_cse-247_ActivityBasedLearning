
# Multi-Currency Travel Budget Analysis

print("=== MULTI-CURRENCY TRAVEL BUDGET ===")

budget = float(input("Enter planned travel budget in INR: Rs."))
fee_percentage = float(input("Enter conversion fee percentage: "))
n = int(input("Enter number of expense categories: "))

expenses = []

if budget < 0 or not 0 <= fee_percentage <= 100 or n <= 0:
    print("Invalid input! Please enter valid values.")

else:
    for i in range(n):
        print(f"\nExpense Category {i + 1}")

        category = input("Enter category name: ")
        amount = float(input("Enter expense amount: "))
        currency = input("Enter currency code (USD/EUR/INR): ").upper()
        exchange_rate = float(input("Enter exchange rate to INR: "))

        if amount < 0 or exchange_rate <= 0:
            print("Invalid amount or exchange rate!")
            continue

        
        converted_amount = amount * exchange_rate

        
        conversion_fee = converted_amount * fee_percentage / 100

    
        total_expense = converted_amount + conversion_fee

        expenses.append({
            "category": category,
            "currency": currency,
            "amount": amount,
            "converted": converted_amount,
            "fee": conversion_fee,
            "total": total_expense
        })

    if not expenses:
        print("\nNo valid expenses entered.")

    else:
    
        total_spending = sum(item["total"] for item in expenses)

        
        largest_expense = max(expenses, key=lambda x: x["total"])

        print("\n========== TRAVEL BUDGET REPORT ==========")
        print("Category      Currency   Amount   INR Value   Fee    Total")

        for item in expenses:
            print(
                f"{item['category']:<13} "
                f"{item['currency']:<9} "
                f"{item['amount']:>7.2f} "
                f"{item['converted']:>10.2f} "
                f"{item['fee']:>7.2f} "
                f"{item['total']:>9.2f}"
            )

        print("------------------------------------------")
        print(f"Planned Budget       : Rs.{budget:.2f}")
        print(f"Total Travel Spending: Rs.{total_spending:.2f}")

        if total_spending > budget:
            print(f"Budget Exceeded      : Rs.{total_spending - budget:.2f}")
            print("Status: OVER BUDGET")

        elif total_spending < budget:
            print(f"Remaining Budget     : Rs.{budget - total_spending:.2f}")
            print("Status: WITHIN BUDGET")

        else:
            print("Status: EXACTLY ON BUDGET")

        print("Largest Expense Category:", largest_expense["category"])
        print(f"Largest Expense Amount  : Rs.{largest_expense['total']:.2f}")
        print("==========================================")

