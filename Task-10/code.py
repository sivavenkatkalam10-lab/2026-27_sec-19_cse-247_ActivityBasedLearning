
# Campus Event Financial Planning

participants = int(input("Enter expected number of participants: "))

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))


fixed_cost = venue + equipment + transport

variable_cost = (catering + certificate) * participants

total_cost = fixed_cost + variable_cost


shortfall = max(0, total_cost - sponsorship)


if participants > 0:
    contribution = shortfall / participants
else:
    contribution = 0


per_person_cost = catering + certificate

if sponsorship >= fixed_cost:
    if per_person_cost > 0:
        minimum_participants = 0
    else:
        minimum_participants = 0
elif per_person_cost > 0:
    minimum_participants = int(
        (fixed_cost - sponsorship + per_person_cost - 1)
        // per_person_cost
    )
else:
    minimum_participants = -1


print("\n----- CAMPUS EVENT FINANCIAL REPORT -----")

print("Fixed Cost:", fixed_cost)
print("Variable Cost:", variable_cost)
print("Total Event Cost:", total_cost)
print("Sponsorship Amount:", sponsorship)
print("Sponsorship Shortfall:", shortfall)
print("Participant Contribution:", round(contribution, 2))

if minimum_participants == -1:
    print("Break-even registration is not possible.")
else:
    print("Minimum Registrations Required:",
          minimum_participants)

print("-----------------------------------------")

