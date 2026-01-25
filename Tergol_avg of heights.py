i: int = 0
sum_: int = 0
while i<20:
#loop of 20 heights

    height: int = int(input("Enter a height: "))
    if height >= 140 and height <= 190:
        i = i + 1
        sum_ = sum_ + height
    else:
        print("Not a valid height")
else:
    print (sum_ / 20)
    #avg calculate
