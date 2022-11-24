import numpy as np

def enc(text, key):
    cols = len(key)
    rows = int(np.ceil(len(text) / cols))
    text += 'abcdefghijklmnopqrstuvwxyz'
    text = text.replace(' ', '')
    matrix = np.ndarray((rows, cols), dtype='<U16')
    k = 0;
    for i in range(0, rows):
        for j in range(0, cols):
                matrix[i][j] = text[k]
                k += 1

    keyDec = {}
    for i in range(0, len(key)):
        keyDec[int(key[i])] = i
    ciper = ""
    for i in range(1, cols+1):
        j = keyDec[i]
        for k in range(0, rows):
            ciper += matrix[k][j]
    return ciper

def dec(cipher, key):
    cols = len(key)
    rows = int(np.ceil(len(cipher) / cols))
    keyDec = {}
    for i in range(0, len(key)):
        keyDec[i] = int(key[i])

    matrix = np.ndarray((rows, cols), dtype='<U16')
    
    map = {}
    i = 0
    j = 0
    while j < len(cipher):
        st = ""
        for k in range(0,rows):
            st += cipher[j]
            j += 1
        map[i] = st;
        i += 1

    j = 0    
    for i in range(0, len(key)):
        st = map[keyDec[i]-1]
        t = 0
        for k in range(0, rows):
            matrix[k][j] = st[t]
            t = t+1
        j += 1

    res = ""
    for i in range(0, rows):
        for j in range(0, cols):
            res += matrix[i][j]

    return res

# print(enc("Attack postponed until twoam", '4312567'))
print("Decrypted message is: ")        
print(dec("ttnaaptmtsuoAodwcoiaknlbpetc" , '4312567'))
