customer_name = input("Enter Customer Name: ")
customer_type = input("Enter Customer Type (R/C): ").upper()

previous_meter_reading = int(input("Enter Previous Meter Reading: "))
current_meter_reading = int(input("Enter Current Meter Reading: "))

paid_after_due_date = input("Paid After Due Date? (Y/N): ").upper()

if customer_type != 'R' and customer_type != 'C':
    print("Error: Invalid Customer Type.")
    exit()

if previous_meter_reading < 0 or current_meter_reading < 0:
    print("Error: Meter readings cannot be negative.")
    exit()

if current_meter_reading < previous_meter_reading:
    print("Error: Current reading cannot be less than previous reading.")
    exit()

if paid_after_due_date != 'Y' and paid_after_due_date != 'N':
    print("Error: Invalid payment status.")
    exit()

units_consumed = current_meter_reading - previous_meter_reading

if customer_type == 'C':
    energy_charges = units_consumed * 30
    fixed_charges = 500

elif customer_type == 'R':
    if units_consumed <= 100:
        energy_charges = units_consumed * 10
        fixed_charges = 100

    elif units_consumed <= 200:
        remaining_units = units_consumed - 100
        energy_charges = (100 * 10) + (remaining_units * 15)
        fixed_charges = 100

    elif units_consumed <= 300:
        remaining_units = units_consumed - 200
        energy_charges = (100 * 10) + (100 * 15) + (remaining_units * 20)
        fixed_charges = 200

    else:
        remaining_units = units_consumed - 300
        energy_charges = (100 * 10) + (100 * 15) + (100 * 20) + (remaining_units * 25)
        fixed_charges = 200

if units_consumed <= 100:
    consumption_level = "Low"
elif units_consumed <= 300:
    consumption_level = "Moderate"
else:
    consumption_level = "High"

total_before_gst = energy_charges + fixed_charges
gst_amount = total_before_gst * 0.18

total_before_surcharge = total_before_gst + gst_amount

if paid_after_due_date == 'Y':
    late_payment_surcharge = total_before_surcharge * 0.10
else:
    late_payment_surcharge = 0

total_payable = total_before_surcharge + late_payment_surcharge

print("\n========== ELECTRICITY BILL ==========")
print(f"Customer Name: {customer_name}")

if customer_type == 'R':
    print("Customer Type: Residential")
else:
    print("Customer Type: Commercial")

print(f"Previous Meter Reading: {previous_meter_reading}")
print(f"Current Meter Reading: {current_meter_reading}")
print(f"Units Consumed: {units_consumed}")
print("--------------------------------------")
print(f"Energy Charges: Rs {energy_charges:.2f}")
print(f"Fixed Charges: Rs {fixed_charges:.2f}")
print(f"GST (18%): Rs {gst_amount:.2f}")
print(f"Late Payment Surcharge: Rs {late_payment_surcharge:.2f}")
print("--------------------------------------")
print(f"Total Payable: Rs {total_payable:.2f}")
print(f"Consumption Level: {consumption_level}")
print("======================================")
