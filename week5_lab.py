# Author: Sami Ali
# Business domain: Purchase requests for office equipment


def calculate_order(quantity, unit_price):
    subtotal = unit_price * quantity
    tax = subtotal * 0.07
    total = subtotal + tax
    requires_approval = total > 1000
    return subtotal, tax, total, requires_approval


def main():
    product_name = "Laptop"
    status = "Pending"
    quantity = 3
    unit_price = 450.00
    is_over_limit = unit_price * quantity > 1000

    print(type(product_name), type(quantity), type(unit_price), type(is_over_limit))

    subtotal, tax, total, requires_approval = calculate_order(quantity, unit_price)

    print("=== Purchase Request Summary ===")
    print(f"Product:  {product_name}")
    print(f"Status:   {status}")
    print(f"Qty:      {quantity}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax:      ${tax:.2f}")
    print(f"Total:    ${total:.2f}")
    print(f"Requires approval: {requires_approval}")

    user_qty = int(input("Enter a new quantity: "))
    _, _, new_total, new_approval = calculate_order(user_qty, unit_price)
    print(f"New total for {user_qty} units: ${new_total:.2f}")
    print(f"Requires approval: {new_approval}")


if __name__ == "__main__":
    main()
