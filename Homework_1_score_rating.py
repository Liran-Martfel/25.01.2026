num: int = int(input("Enter a number: "))
if num > 199 or num < 0:
    print ("INVALID NUMBER")
elif num >= 80 and num <= 100:
    print ("VERY GOOD")
elif num >= 60 and num < 80:
    print ("NOT BAD")
elif num >= 40 and num < 60:
    print ("BAD")
else:
    print ("RALLY BAD")