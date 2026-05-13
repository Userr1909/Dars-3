# 4-masala. Ikki do'st alohida shaharlar ro'yxatini to'pladi: 
# 	ali = {"Toshkent", "Samarqand", "Buxoro", "Andijon"}
# 	vali = {"Toshkent", "Farg'ona", "Buxoro", "Xiva"}
# Ikkala do'st ham borgan shaharlarni va faqat ali borgan shaharlarni chiqaring.
import os
os.system("cls")

ali = {"Toshkent", "Samarqand", "Buxoro", "Andijon"}
vali = {"Toshkent", "Farg'ona", "Buxoro", "Xiva"}

set3 = ali & vali
hos = ali - vali

print(set3)
print(hos)