# 1-masala. Ikkita set berilgan, ularning umumiy elementlari yig'indisidan,
# faqat birinchi setga tegishli elementlar yig'indisining ayirilganini chiqaring.
# Input: set1={1,2,3,4,5,6}, set2={4,5,6,7,8,9}
# Output: 9 (chunki umumiy qiymatlari yig'indisi (4+5+6) 15 va faqat birinchi setga tegishli elementlar yig'indisi (1+2+3) 6, 15-6=9)
import os
os.system("cls")

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

set3 = set1 & set2
hos = set1 - set2
natija = sum(set3) - sum(hos)
print(natija)
