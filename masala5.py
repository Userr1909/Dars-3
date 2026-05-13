# 5-masala. Foydalanuvchi ikkita so'z kiritadi, kiritilgan so'zlar anagram ekanini tekshiring.
# Anagram so'z deganda bir so'zning harflari o'rnini almashtirib ikkinchi so'zni hosil qilish mumkin bo'lishi.
# Input: soz1 = "listen", soz2 = "silent"
# Output: True
# Input: soz1 = "apple", soz2 = "angel"
# Output: False
# Input: soz1 = "thing", soz2 = "night"
# Output: True
import os
os.system("cls")

matn1 = input("birinchi so'z = ")
matn2 = input("ikkinchi so'z = ")

if sorted(matn1) == sorted(matn2):
    print(True)
else:
    print(False)