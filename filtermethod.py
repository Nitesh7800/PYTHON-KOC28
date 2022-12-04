def isEven(i):
    return i%2==0

list1= [3,9,8,7,4,5,6]

output =list(filter(lambda i: i%2==0,list1))
output2=map(lambda i:i**2,list1)
print(output)