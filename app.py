name = input("Enter customer name: ")
customer_type = input("Enter customer type (R = Residential, C = Commercial): ").upper()
previous_reading = int(input("Enter previous meter reading: "))
current_reading = int(input("Enter current meter reading: "))
paid_late = input("Was the bill paid after the due date? (Y/N): ").upper()

if customer_type != "R" and customer_type != "C":
    print("Error: Invalid customer type. Please enter R (Residential) or C (Commercial).")

elif previous_reading < 0 or current_reading < 0:
    print("Error: Meter readings cannot be negative.")

elif current_reading < previous_reading:
    print("Error: Current reading cannot be less than the previous reading.")

else:
    units = current_reading - previous_reading

    if customer_type == "R":
        if units <= 100:
            energy = units * 10

        elif units <= 200:
            energy = (100 * 10) + (units - 100) * 15

        elif units <= 300:
            energy = (100 * 10) + (100 * 15) + (units - 200) * 20

        else:
            energy = (100 * 10) + (100 * 15) + (100 * 20) + (units - 300) * 25

    else:
        energy = units * 30

    if customer_type == "R":
        if units <= 200:
            fixed = 100
        else:
            fixed = 200

    else:
        fixed = 500

    gst = 0.18 * (energy + fixed)

    if paid_late == "Y":
        surcharge = 0.10 * (energy + fixed + gst)
    else:
        surcharge = 0

    total = energy + fixed + gst + surcharge

    if units <= 100:
        level = "Low"

    elif units <= 300:
        level = "Moderate"

    else:
        level = "High"

    if customer_type == "R":
        type_name = "Residential"
    else:
        type_name = "Commercial"

    print("\n==================================================")
    print("                 ELECTRICITY BILL")
    print("==================================================")
    print(f"Customer Name      : {name}")
    print(f"Customer Type      : {type_name}")
    print(f"Units Consumed     : {units}")
    print("--------------------------------------------------")
    print(f"Energy Charges    : Rs {energy:.2f}")
    print(f"Fixed Charge      : Rs {fixed:.2f}")
    print(f"GST (18%)         : Rs {gst:.2f}")
    print(f"Late Surcharge    : Rs {surcharge:.2f}")
    print("--------------------------------------------------")
    print(f"TOTAL PAYABLE     : Rs {total:.2f}")
    print(f"Consumption Level : {level}")
    print("==================================================")