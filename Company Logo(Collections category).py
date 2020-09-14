    #My Solution
    from collections import Counter,OrderedDict
    s = input()
    s = Counter(s)
    b = OrderedDict(sorted(s.items(), key=lambda t: t[0]))
    b = Counter(OrderedDict(sorted(b.items(), key=lambda t: t[1],reverse=True))).most_common(3)
    b = dict(b)
    for x,y in b.items():
        print(x,y)
    
#best Solution
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
