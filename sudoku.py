r1 = [0,0,0,0,0,0,0,0,0]
r2 = [0,0,0,0,0,0,0,0,0]
r3 = [0,0,0,0,0,0,0,0,0]
r4 = [0,0,0,0,0,0,0,0,0]
r5 = [0,0,0,0,0,0,0,0,0]
r6 = [0,0,0,0,0,0,0,0,0]
r7 = [0,0,0,0,0,0,0,0,0]
r8 = [0,0,0,0,0,0,0,0,0]
r0 = [0,0,0,0,0,0,0,0,0]

board = [r0,r1,r2,r3,r4,r5,r6,r7,r8]
win = False
while not win:
    break_con = 0
    for i in range(9):
        print(board[i])

    r  = int(input("Enter the row: "))-1
    c =  int(input("Enter the column: "))-1
    no =  int(input("Enter the number(1-9): "))
    l = (r+1)//3
    if l==0:
        x = 2
    if l==1:
        x = 5
    if l==2:
        x=8
    m= (c+1)//3
    if m==0:
        y = 2
    if m==1:
        y = 5
    if m==2:
        y=8
    for j in range(x-2,x):
        for k in range(y-2,y):
            if no == board[j][k]:
                print("Number is already in the box")
                break_con = 1
                break
        if break_con == 1:
            break
    if no in board[r]:
            print("Number already in the row")
            break_con = 1
    for i in range(9):
        if no == board[i][c]:
            print("Number is already in the column")
            break_con = 1
            break
            
    if break_con == 1:
        continue
    board[r][c] = no

    for i in range(9):
        if 0 not in board[i]:
            win = True
    
