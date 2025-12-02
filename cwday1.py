apple=15.5
orange=20
grape=10.25

total_volume=apple+orange+grape
print("Total Volume Sold : ", total_volume)

total_volume_int=int(total_volume)
print("Total Volume in Integer : ", total_volume_int)

total_volume_str=str(total_volume)
print(total_volume_str+" litres of juice are sold")

import random
bonus = random.randint(5, 10)
final_total = total_volume + bonus
print("Final total with bonus:", final_total)