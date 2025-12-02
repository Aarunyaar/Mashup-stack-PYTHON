rice_price=45
sugar_price=40
oil_price=130

rice_qty=3
sugar_qty=2.5
oil_qty=1.8

total_rice_price=rice_price*rice_qty
total_sugar_price=sugar_price*sugar_qty
total_oil_price=oil_price*oil_qty

print("Total rice price: ",total_rice_price)
print("Total sugar price: ",total_sugar_price)
print("Total oil price: ",total_oil_price)

total_bill=total_rice_price+total_sugar_price+total_oil_price
print("Total Bill: ",total_bill)

total_bill_int=int(total_bill)
print("Total bill in integer: ",total_bill_int)

total_bill_str=str(total_bill)
print("Total bill is ",total_bill_str," rupees")

import random
delivery_charge=random.randint(5,10)

total_bill_dlvry=total_bill+delivery_charge

print("Delivery Charge: ",delivery_charge)
print("Total bill with delivery charge: ",total_bill_dlvry)