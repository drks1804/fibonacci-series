num = int(input("enter any number :"))
a, b = 0, 1
sum =0
if num<=0:
    print('enter number greater than 0')
else:
    for i in range(0, num):
        print(sum, end=" ")
        a = b
        b = sum
        sum = a + b
