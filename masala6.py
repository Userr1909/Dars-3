# 6-masala. Ikkita set berilgan, bu setlarning umumiy bo'lmagan elementlari yig'indisidan, umumiy elementlari yig'indisini ayiring.
# Input: set1={4,5,6,7,8,9}, set2={5,6,7,10,11}
# Output: 24 (chunki, umumiy bo'lmagan elementlari yig'indisi (4+8+9+10+11) 42 va umumiy elementlari (4+5+6) 18
import os
os.system("cls")

set1={4,5,6,7,8,9}
set2={5,6,7,10,11}

umumiy_emas = set1 ^ set2
umumiy = set1 & set2
print(sum(umumiy_emas) - sum(umumiy))