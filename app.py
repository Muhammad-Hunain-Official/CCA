C_name=input()
C_type=input("R/C").upper()
Previous_M_read=int(input())
Current_M_read=int(input())
Bill_Paid=input("[Y/N]").upper()
if C_type != 'R' and C_type != 'C':
    print("Do not calculate the bill") 
    exit()
if Current_M_read < Previous_M_read or Current_M_read < 0 or Previous_M_read < 0:
    print("Do not calculate the bill") 
    exit()
unit_consumed=Current_M_read-Previous_M_read
# 
if  C_type == 'C':
    Energy_charges= unit_consumed * 30
    Fixed_charges=500

if C_type == 'R' and unit_consumed <= 100:
    Energy_charges= unit_consumed * 10
    Fixed_charges=100
    Consumption_level="low"
elif C_type == 'R' and unit_consumed > 100 and unit_consumed <=200:
    rem_units= unit_consumed-100
    Energy_charges= (100*10)+ (rem_units*15)
    Fixed_charges=100
    Consumption_level="Moderate"

elif C_type == 'R' and unit_consumed > 200 and unit_consumed <=300:
    rem_units=unit_consumed-200
    Energy_charges= (100*10) + (100*15) +(rem_units *20)
    Fixed_charges=200
    Consumption_level="Moderate"
elif C_type == 'R' and unit_consumed > 300 :
    rem_units=unit_consumed-300
    Energy_charges= (100*10) + (100*15) + (100*20) +(rem_units * 25)
    Fixed_charges=200
    Consumption_level="High"
Total_Before_GST=Energy_charges+Fixed_charges
GST=(Total_Before_GST/100)*18

if Bill_Paid == 'Y':
    Total_before_Surcharge=Energy_charges +Fixed_charges +GST
    latePayment_surcharge = (Total_before_Surcharge /100)*10
else:
    latePayment_surcharge =0
    # print("No late Charges ")

Total_Payable=Energy_charges +Fixed_charges+ GST +latePayment_surcharge
print(GST)
print(Energy_charges)
print(Fixed_charges)
print(latePayment_surcharge)
print(Total_Payable)
print(Consumption_level)