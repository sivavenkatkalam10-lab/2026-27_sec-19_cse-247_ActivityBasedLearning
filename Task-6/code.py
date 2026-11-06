
# Railway Fare and Reservation Calculator

print("===== RAILWAY FARE CALCULATOR =====")


classes = {
    "Sleeper": 1.0,
    "AC 3 Tier": 1.5,
    "AC 2 Tier": 2.0,
    "AC First Class": 3.0
}

RESERVATION_FEE = 50
CANCELLATION_RATE = 0.25


def calculate_fare(distance):

    if distance <= 100:
        fare = distance * 1

    elif distance <= 300:
        fare = (100 * 1) + (distance - 100) * 1.5

    else:
        fare = (100 * 1) + (200 * 1.5) + (distance - 300) * 2

    return fare



n = int(input("Enter number of passengers: "))


if n <= 0:
    print("Invalid number of passengers!")

else:

    total_fare = 0
    total_refund = 0

    for i in range(n):

        print("\n----- Passenger", i + 1, "-----")

        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        distance = float(input("Enter journey distance (km): "))

        print("\nAvailable Classes:")
        for cls in classes:
            print(cls)

        travel_class = input("Enter travel class: ")

        
        if age < 0 or distance <= 0 or travel_class not in classes:
            print("Invalid passenger details!")
            continue

        
        basic_fare = calculate_fare(distance)

        
        class_fare = basic_fare * classes[travel_class]

        
        if age < 5:
            concession = class_fare
        elif age >= 60:
            concession = class_fare * 0.20
        else:
            concession = 0

        discounted_fare = class_fare - concession
        final_fare = discounted_fare + RESERVATION_FEE

        
        print("\n===== TICKET DETAILS =====")
        print("Passenger Name:", name)
        print("Age:", age)
        print("Distance:", distance, "km")
        print("Travel Class:", travel_class)
        print("Basic Fare: Rs.", round(basic_fare, 2))
        print("Class Fare: Rs.", round(class_fare, 2))
        print("Age Concession: Rs.", round(concession, 2))
        print("Reservation Fee: Rs.", RESERVATION_FEE)
        print("Final Ticket Fare: Rs.", round(final_fare, 2))

    
        cancel = input("Cancel ticket? (yes/no): ").lower()

        if cancel == "yes":

            penalty = final_fare * CANCELLATION_RATE
            refund = final_fare - penalty

            print("\nTicket Cancelled")
            print("Cancellation Penalty: Rs.", round(penalty, 2))
            print("Refund Amount: Rs.", round(refund, 2))

            total_refund += refund

        elif cancel == "no":

            print("Ticket Confirmed")
            total_fare += final_fare

        else:
            print("Invalid cancellation choice. Ticket treated as confirmed.")
            total_fare += final_fare

    
    print("\n===== FINAL RESERVATION SUMMARY =====")
    print("Total Confirmed Ticket Fare: Rs.", round(total_fare, 2))
    print("Total Refund Amount: Rs.", round(total_refund, 2))

    print("Reservation process completed!")

