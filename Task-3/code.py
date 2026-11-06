
# Hospital Billing and Patient Classification System

print("===== HOSPITAL BILLING SYSTEM =====")


name = input("Enter patient name: ")
age = int(input("Enter patient age: "
consultation = float(input("Enter consultation charges: Rs. "))
diagnostic = float(input("Enter diagnostic charges: Rs. "))
treatment = float(input("Enter treatment charges: Rs. "))

if age < 0:
    print("Invalid age!")

elif consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges! Charges cannot be negative.")

else:
    subtotal = consultation + diagnostic + treatment
    senior_discount = 0
    extra_discount = 0

    
    if age >= 60:
        senior_discount = subtotal * 0.10

    amount_after_senior = subtotal - senior_discount

    
    if subtotal > 10000:
        extra_discount = amount_after_senior * 0.05

    
    total_discount = senior_discount + extra_discount
    final_bill = subtotal - total_discount

    
    print("\n===== BILL DETAILS =====")
    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Consultation Charges: Rs.", consultation)
    print("Diagnostic Charges: Rs.", diagnostic)
    print("Treatment Charges: Rs.", treatment)
    print("Subtotal: Rs.", subtotal)
    print("Senior Discount: Rs.", senior_discount)
    print("Additional Discount: Rs.", extra_discount)
    print("Total Discount: Rs.", total_discount)
    print("Final Bill: Rs.", round(final_bill, 2))

  
    paid = float(input("\nEnter amount paid: Rs. "))

    if paid < 0:
        print("Invalid payment amount!")

    else:

        # Patient payment classification
        if paid == 0:
            status = "UNPAID"
            balance = final_bill

        elif paid < final_bill:
            status = "PARTIALLY PAID"
            balance = final_bill - paid

        elif paid == final_bill:
            status = "FULLY PAID"
            balance = 0

        else:
            status = "OVERPAID"
            balance = paid - final_bill

      
        print("\n===== PAYMENT CLASSIFICATION =====")
        print("Patient Name:", name)
        print("Payment Status:", status)

        if status == "OVERPAID":
            print("Extra Amount: Rs.", round(balance, 2))
        else:
            print("Remaining Balance: Rs.", round(balance, 2))

        print("\nThank you!")

