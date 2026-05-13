# 2-masala. Uchta set berilgan, birinchi va ikkinchi set uchun umumiy bo'lgan lekin uchinchi setda mavjud bo'lmagan elementlarni chiqaring.
# Input:  set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
# 	set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
# 	set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}
# Output: youtube, anor
import os
os.system("cls")

set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}

set4 = set1 & set2
set4 -= set3
print(set4)