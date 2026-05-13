# 3-masala. Sonlardan iborat ikkita set berilgan. Shu setlarning umumiy bo'lmagan elementlarini kamayish tartibida chiqaring.
# Input: set1 = {1,2,3,4,5,6}, set2 = {4,5,6,7,8,9}
# Output: 9 8 7 3 2 1
import os
os.system("cls")

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

set3 = set1 ^ set2
natija = sorted(set3,reverse=True)
for i in natija:
    print(i,end=" ")