def func(board):
    for i in range(9):                          # har row check karenge
        a=[]
        for j in range(9):                      # row ke har element ko check karenge
            if board[i][j]!=".":                # dot ko ignore karenge
                if board[i][j] in a:            # agar number pehle se hai
                    print("false")
                    return
                a.append(board[i][j])            # number ko list mein add karo
    for j in range(9):                          # har column check karenge
        a=[]
        for i in range(9):                      # column ke har element ko check karenge
            if board[i][j]!=".":                # dot ko ignore karenge
                if board[i][j] in a:            # duplicate number mila
                    print("false")
                    return
                a.append(board[i][j])            # number ko list mein add karo
    for i in range(0,9,3):                      # 3x3 boxes ki starting rows: 0,3,6
        for j in range(0,9,3):                  # 3x3 boxes ki starting columns: 0,3,6
            a=[]
            for x in range(i,i+3):              # box ki 3 rows
                for y in range(j,j+3):          # box ki 3 columns
                    if board[x][y]!=".":        # dot ko ignore karenge
                        if board[x][y] in a:    # duplicate number mila
                            print("false")
                            return
                        a.append(board[x][y])    # number ko list mein add karo
    print("true")                               # kahin duplicate nahi mila