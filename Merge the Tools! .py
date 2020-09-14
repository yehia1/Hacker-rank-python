#to make the texted wraped so you can print the string in the width you want
import textwrap 
#to make the string s remove the dublicates
from collections import OrderedDict

def merge_the_tools(s, k):
    for i in range(0,len(s),k):
         x = "".join(OrderedDict.fromkeys(s[i:i+k]))
         wrapper = textwrap.TextWrapper(width=len(x))
         string = wrapper.fill(text=x) 
         print (string)



if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    

