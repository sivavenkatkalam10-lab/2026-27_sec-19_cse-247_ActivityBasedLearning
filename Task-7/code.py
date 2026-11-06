
# Retail Billing with Multiple Discount Rules

tax_rates = {
    "electronics": 18,
    "clothing": 5,
    "grocery": 0
}

products = []

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nEnter details for Product {i + 1}")

    name = input("Product name: ")
    category = input("Category (electronics/clothing/grocery): ").lower()
    price = float(input("Price per unit: "))
    quantity = int(input("Quantity: "))

    if category not in tax_rates:
        print("Invalid category!")
        continue

    if price <= 0 or quantity <= 0:
        print("Price and quantity must be positive!")
        continue

    gross = price * quantity

    
    quantity_discount = 0

    if quantity >= 5:
        quantity_discount = gross * 0.05

    amount_after_quantity_discount = gross - quantity_discount

    products.append({
        "name": name,
        "category": category,
        "quantity": quantity,
        "gross": gross,
        "quantity_discount": quantity_discount,
        "amount": amount_after_quantity_discount
    })

if not products:
    print("\nNo valid products entered.")

else:
    
    subtotal = sum(p["amount"] for p in products)


    if subtotal >= 10000:
        threshold_rate = 0.10
    elif subtotal >= 5000:
        threshold_rate = 0.05
    else:
        threshold_rate = 0

    threshold_discount = subtotal * threshold_rate

    
    total_discount = (
        sum(p["quantity_discount"] for p in products)
        + threshold_discount
    )
    allowed_discount = min(total_discount, 1500)

  
    if total_discount > 0:
        discount_factor = allowed_discount / total_discount
    else:
        discount_factor = 0

    total_tax = 0
    final_subtotal = 0

    print("\n============== RETAIL INVOICE ==============")
    print("Product       Qty   Gross   Discount   Tax   Total")

    for p in products:
        gross = p["gross"]

        
        q_discount = p["quantity_discount"] * discount_factor

      
        threshold_part = (
            threshold_discount
            * (p["amount"] / subtotal)
            if subtotal > 0 else 0
        )

        threshold_part *= discount_factor

        item_discount = q_discount + threshold_part

        taxable_amount = gross - item_discount

        tax_rate = tax_rates[p["category"]]
        tax = taxable_amount * tax_rate / 100

        item_total = taxable_amount + tax

        total_tax += tax
        final_subtotal += taxable_amount

        print(
            f"{p['name']:<12} "
            f"{p['quantity']:>3} "
            f"{gross:>9.2f} "
            f"{item_discount:>9.2f} "
            f"{tax:>7.2f} "
            f"{item_total:>9.2f}"
        )

    grand_total = final_subtotal + total_tax

    print("--------------------------------------------")
    print(f"Original Subtotal       : Rs.{sum(p['gross'] for p in products):.2f}")
    print(f"Quantity + Threshold Discount: Rs.{allowed_discount:.2f}")
    print(f"Taxable Subtotal        : Rs.{final_subtotal:.2f}")
    print(f"Total Tax               : Rs.{total_tax:.2f}")
    print(f"Grand Total             : Rs.{grand_total:.2f}")
    print("============================================")

