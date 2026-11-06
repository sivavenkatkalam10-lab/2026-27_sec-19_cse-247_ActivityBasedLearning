
# Manufacturing Cost and Profitability Analysis

print("=== MANUFACTURING COST ANALYSIS ===")

product_name = input("Enter product name: ")
quantity = int(input("Enter production quantity: "))

material_cost = float(input("Enter material cost: Rs."))
labour_cost = float(input("Enter labour charges: Rs."))
machine_cost = float(input("Enter machine cost: Rs."))

wastage_percentage = float(input("Enter wastage percentage: "))
selling_price = float(input("Enter selling price per unit: Rs."))
target_profit = float(input("Enter target profit percentage: "))

if (quantity <= 0 or material_cost < 0
        or labour_cost < 0 or machine_cost < 0
        or selling_price < 0
        or not 0 <= wastage_percentage <= 100
        or target_profit < 0):

    print("Invalid input! Please enter valid values.")

else:
    
    wastage_cost = material_cost * wastage_percentage / 100

    
    total_material_cost = material_cost + wastage_cost

    
    total_cost = (
        total_material_cost
        + labour_cost
        + machine_cost
    )

  
    total_revenue = selling_price * quantity

    
    profit = total_revenue - total_cost

    
    if total_cost > 0:
        profit_percentage = (profit / total_cost) * 100
    else:
        profit_percentage = 0

  
    print("\n======= MANUFACTURING REPORT =======")
    print("Product Name             :", product_name)
    print("Production Quantity      :", quantity)
    print("Material Cost            : Rs.", round(material_cost, 2))
    print("Wastage Cost             : Rs.", round(wastage_cost, 2))
    print("Total Material Cost      : Rs.", round(total_material_cost, 2))
    print("Labour Charges           : Rs.", round(labour_cost, 2))
    print("Machine Cost             : Rs.", round(machine_cost, 2))
    print("Total Manufacturing Cost : Rs.", round(total_cost, 2))
    print("Selling Price Per Unit   : Rs.", round(selling_price, 2))
    print("Total Revenue            : Rs.", round(total_revenue, 2))
    print("Profit / Loss            : Rs.", round(profit, 2))
    print("Profit Percentage        :", round(profit_percentage, 2), "%")

    print("------------------------------------")

    if profit < 0:
        print("Result: Production is running at a LOSS.")
    elif profit_percentage >= target_profit:
        print("Result: Profit target ACHIEVED.")
    else:
        print("Result: Profit target NOT ACHIEVED.")

    print("Target Profit Percentage :", target_profit, "%")
    print("====================================")

