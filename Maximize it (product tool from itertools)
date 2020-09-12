from itertools import product
l,k = map(int,input().split())
list1= []
for i in range(l):
    # we start from index number one cause index number 0 represents how many elements in the list so not important
    list1.append(list(map(int,input().split()))[1:])

results = map(lambda x: sum(i**2 for i in x)%k, product(*list1))
print(max(results))
