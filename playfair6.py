import numpy as np
def Matrix(key):
    k=''
    for i in key.upper():
        if i not in k:
            k+=i
    for j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        if j not in k:
            k+=j
    return np.array([list(k)]).reshape(6,6)

def digram(a):
    k=""
    a = a.replace(" ","").upper()
    i=0
    while i<len(a):
        try:
            if a[i]!=a[i+1]:
                k+=f"{a[i]+a[i+1]}"
                i+=2
            else:
                k+=f"{a[i]}X"
                i+=1
        except:
            k+=f"{a[i]}X"
            i+=1
    return list(k)

def search(matrix,element):
    for i in range(6):
        for j in range(6):
            if matrix[i][j]==element:
                return i,j

def encryption(plain_text,key):
    cipher_text=''
    d=digram(plain_text)
    v=Matrix(key)
    for i in range(0,len(d),2):
        a=d[i:i+2]
        r1,c1 = search(v,a[0])
        r2,c2 = search(v,a[1])
        if r1 == r2:
            first = v[r1][0] if c1+1 > 5 else v[r1][c1+1]
            second = v[r2][0] if c2+1 > 5 else v[r2][c2+1]
            cipher_text=cipher_text+first+second
        elif c1 == c2:
            first = v[0][c1] if r1+1 > 4 else v[r1+1][c1]
            second = v[0][c2] if r2+1 > 4 else v[r2+1][c2]
            cipher_text=cipher_text+first+second
        else:
            first,second =v[r1][c2],v[r2][c1]
            cipher_text=cipher_text+first+second
    return cipher_text
    for i in range(0,len(d),2):
        a=d[i:i+2]
        i,j=search(v,a[0])
        c,k=search(v,a[1])
        if i==c:
            cipher_text+=rowrule(v,i,j,k)
        elif j==k:
            cipher_text+=colrule(v,i,c,j)
        else:
            cipher_text+=boxrule(v,i,j,c,k)
    return cipher_text
def decryption(cipher_text,key):
    decrypted_text=''
    v=Matrix(key)
    for i in range(0,len(cipher_text),2):
        a=cipher_text[i:i+2]
        r1,c1 = search(v,a[0])
        r2,c2 = search(v,a[1])
        if r1 == r2:
            first = v[r1][-1] if c1-1 < 0 else v[r1][c1-1]
            second = v[r2][-1] if c2-1 < 0 else v[r2][c2-1]
            decrypted_text=decrypted_text+first+second
        elif c1 == c2:
            first = v[-1][c1] if r1-1 < 0 else v[r1-1][c1]
            second = v[-1][c2] if r2-1 < 0 else v[r2-1][c2]
            decrypted_text=decrypted_text+first+second
        else:
            first,second = v[r1][c2],v[r2][c1]
            decrypted_text=decrypted_text+first+second
    return decrypted_text

plain_text=input('Enter a text: ')
print(digram(plain_text))
key=input('Enter a key: ')
print(Matrix(key))
cipher_text=encryption(plain_text,key)
print('Ciphered text: ',cipher_text)
print('Decrypted text: ',decryption(cipher_text,key))