num = 1
i = 1
while num > 0:
    # לולאה ראשית שרצה כל עוד המספר אינו שלילי או 0

    num = int(input("Enter a number: "))
    i = 0

    while num > i:
        #לולאה משנית שמדפיסה את כל המספרים מ-1 ועד המספר שהוזן בסדר עולה
        print(i)
        i = i + 1

else:
    print ("stop")