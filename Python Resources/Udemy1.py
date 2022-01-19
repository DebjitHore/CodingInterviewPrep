str= "It was a bright cold day in April, and the clocks were striking thirteen"
x_ind= str.index(",")
str2= ""

for i in range(x_ind):
    str2= str2+str[i]
print (str2)
