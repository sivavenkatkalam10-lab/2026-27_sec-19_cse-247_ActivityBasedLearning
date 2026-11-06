
# Multi-Plan Telecommunications Cost Optimization

print("===== MOBILE PLAN OPTIMIZATION SYSTEM =====")


plans = [
    {
        "name": "Plan A",
        "price": 199,
        "data": 2,
        "calls": 100,
        "sms": 100,
        "validity": 28
    },
    {
        "name": "Plan B",
        "price": 299,
        "data": 3,
        "calls": 200,
        "sms": 200,
        "validity": 28
    },
    {
        "name": "Plan C",
        "price": 399,
        "data": 5,
        "calls": 300,
        "sms": 300,
        "validity": 56
    }
]


data_needed = float(input("Enter required data (GB): "))
calls_needed = int(input("Enter required call minutes: "))
sms_needed = int(input("Enter required SMS count: "))
validity_needed = int(input("Enter minimum validity (days): "))
budget = float(input("Enter maximum budget: Rs. "))


if (data_needed < 0 or calls_needed < 0 or
    sms_needed < 0 or validity_needed <= 0 or budget < 0):

    print("Invalid input! Enter valid positive values.")

else:

    eligible_plans = []

    
    for plan in plans:

        if plan["validity"] >= validity_needed:

            
            extra_data = max(0, data_needed - plan["data"])
            extra_calls = max(0, calls_needed - plan["calls"])
            extra_sms = max(0, sms_needed - plan["sms"])

            
            data_charge = extra_data * 20
            call_charge = extra_calls * 1
            sms_charge = extra_sms * 0.50

            
            total_cost = (
                plan["price"] +
                data_charge +
                call_charge +
                sms_charge
            )

            print("\n", plan["name"])
            print("Base Price: Rs.", plan["price"])
            print("Extra Data Charge: Rs.", data_charge)
            print("Extra Call Charge: Rs.", call_charge)
            print("Extra SMS Charge: Rs.", sms_charge)
            print("Total Cost: Rs.", total_cost)

            
            if total_cost <= budget:

                eligible_plans.append({
                    "name": plan["name"],
                    "cost": total_cost,
                    "validity": plan["validity"]
                })

                print("Status: Eligible")

            else:
                print("Status: Exceeds Budget")

        else:
            print("\n", plan["name"], "- Invalid Validity")

    
    print("\n===== PLAN COMPARISON RESULT =====")

    if eligible_plans:

        eligible_plans.sort(
            key=lambda x: (x["cost"], -x["validity"], x["name"])
        )

        best = eligible_plans[0]

        print("Most Economical Plan:", best["name"])
        print("Total Cost: Rs.", round(best["cost"], 2))
        print("Validity:", best["validity"], "days")

        print("\nAll Eligible Plans:")

        for plan in eligible_plans:
            print(plan["name"], "- Rs.", round(plan["cost"], 2))

    else:
        print("No eligible mobile plan found.")
        print("Please increase your budget or change requirements.")




