import numpy as np
x = np.array([[[ ], [ ], [ ]],
              [[ ], [ ], [ ]],
              [[ ], [ ], [ ]]])
print(x)
a=0
for i in range (0,9) :
    if (i + 1)%2!= 0 :
        print("Hello, Player X")
        row = int(input("Enter the row number of your entry")) - 1
        col = int(input("Enter the column number of your entry")) - 1
        x[row, col] = ['X']
    elif (i+1)%2==0:
        print("Hello, Player O")
        row = int(input("Enter the row number of your entry")) - 1
        col = int(input("Enter the column number of your entry")) - 1
        x[row, col] = ['O']

    if i >= 4 :
        if x[0,0] == x[0,1] and x[0,1] == x[0,2] :
            print("Player" + x[0,0] + "has won")
            print(x)
            a = 1
            break
        elif x[1,0] == x[1,1] and x[1,1] == x[2,2] :
            print("Player" + x[1,0] + "has won")
            print(x)
            a = 1
            break
        elif x[2,0] == x[2,1] and x[2,1] == x[2,2] :
            print("Player" + x[2,0] + "has won")
            print(x)
            a = 1
            break
        elif x[0,0] == x[1,0] and x[1,0] == x[2,0] :
            print("Player" + x[1,0] + "has won")
            print(x)
            a = 1
            break
        elif x[0,1] == x[1,1] and x[1,1] == x[2,1] :
            print("Player" + x[0,1] + "has won")
            print(x)
            a = 1
            break
        elif x[0,2] == x[1,2] and x[1,2] == x[2,2] :
            print("Player" + x[0,2] + "has won")
            print(x)
            a = 1
            break
        elif x[0,0] == x[1,1] and x[1,1] == x[2,2] :
            print("Player" + x[0,0] + "has won")
            print(x)
            a = 1
            break
        elif x[0,2] == x[1,1] and x[1,1] == x[2,0] :
            print("Player" + x[0,2] + "has won")
            print(x)
            a = 1
            break

    if i == 8 and a == 0 :
        print("Draw")
        print(x)
