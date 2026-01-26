num = int(input("Enter a number: "))
i = 2
if num <= 1:
    print("The number is less than or equal to 1, no prime")
while num%i !=0:
    #while modulo num is Ezugi.

    i = i + 1
    if num == i:
        #check if num equal to himself and for being Ezugi

        print(num, "is a prime number")
    else:
        print(i, "is not a prime number for",num)

