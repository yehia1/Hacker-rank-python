#My solution
from collections import Counter,OrderedDict
import re
x = int(input())
list1 = (input() for i in range(x))
list3 = Counter(list1)
print(len(list3))
list3=str(list3.values()) 
l = list3[13:-2]
l = re.sub(',','',l)
print(l)


#best solution
from collections import Counter
list3 = Counter(input() for i in range(int(input())))
print(len(list3))
print(*list3.values())
