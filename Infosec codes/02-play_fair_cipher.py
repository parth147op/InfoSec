import numpy as np

matrix = None

def generateKeyMatrix():
    key = input("Enter Your key : ")
    key = key.upper()
    lst = []
    j = 0
    for i in key:
        if i not in lst:
            j = j + 1
            if i == 'J':
                lst.append('I')
            else:
                lst.append(i)
    alphabets = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for i in alphabets:
        if i not in lst:
            j = j + 1
            if j == 26:
                break
            lst.append(i)
    return np.array(lst).reshape(5, 5)

matrix = generateKeyMatrix()

def locateindex(c):
    for i in range(0,5):
        for j in range(0,5):
            if matrix[i][j] == c:
                return (i,j)

def encrypt():
    msg = str(input("Enter Plain Text: "))
    msg = msg.upper()
    msg = msg.replace(" ", "")

    i = 0
    for s in range(0, len(msg) + 1, 2):
        if s < len(msg) - 1:
            if msg[s] == msg[s + 1]:
                msg = msg[:s + 1] + 'X' + msg[s + 1:]
    if len(msg) % 2 != 0:
        msg = msg[:] + 'X'
    print("Cipher Text: ", end='')

    for i in range(0, len(msg), 2):
        loc1 = locateindex(msg[i])
        loc2 = locateindex(msg[i+1])

        if loc1[0] == loc2[0]: #in same row
            print(f"{matrix[loc1[0]][(loc1[1] + 1) % 5]}{matrix[loc2[0]][(loc2[1] + 1) % 5]}", end = " ")
        elif loc1[1] == loc2[1]: #same column
            print(f"{matrix[(loc1[0] + 1) % 5][loc1[1]]}{matrix[(loc2[0] + 1)% 5][loc2[1]]}", end=" ")
        else:
            print(f"{matrix[loc1[0]][loc2[1]]}{matrix[loc2[0]][loc1[1]]}", end=' ')
    
def decrypt():
    msg = str(input("Enter Cipher Text: "))
    msg = msg.upper()
    msg = msg.replace(" ", "")
    print("Plain Text: ", end='')
    i = 0
    for i in range(0, len(msg),2):
        loc = locateindex(msg[i])
        loc1 =locateindex(msg[i+1])
        if loc[1] == loc1[1]:
            print(f"{matrix[(loc[0] - 1) % 5][loc[1]]}{matrix[(loc1[0] -1) % 5][loc1[1]]}", end = "")
        elif loc[0] == loc1[0]:
            print(f"{matrix[loc[0]][(loc[1] -1) % 5]}{matrix[loc1[0]][(loc1[1] - 1) % 5]}", end="")
        else:
            print(f"{matrix[loc[0]][loc1[1]]}{matrix[loc1[0]][loc[1]]}",  end='')
        
encrypt()
print()
decrypt()








  