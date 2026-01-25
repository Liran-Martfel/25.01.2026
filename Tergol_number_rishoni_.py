num = int(input("Enter a number: "))
i = 2
if num <= 1:
    print("The number is less than or equal to 1, no prime")
while num%i !=0:
    #while num is Ezugi.
    i = i + 1
    if num == i:
        print("The prime number is ", num)
    else:
        print(i, "is not prime")

