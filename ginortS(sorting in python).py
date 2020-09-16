print(*(sorted(input(),key = lambda y : (y.isdigit() and int(y)%2==0,y.isdigit(),y.isupper(),y.islower(),y))),sep='')

#best solution:
print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')
