import random
max_PrimLength = 1000000000000

# calculates the modular inverse from e and phi
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# calculates the gcd of two ints
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# checks if a number is a prime
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


# Generate Random Prime Integer
def generateRandomPrim():
    while(1):
        ranPrime = random.randint(0, max_PrimLength)
        if is_prime(ranPrime):
            return ranPrime


# Function to generate Key Pairs
def generate_keyPairs():
    p = generateRandomPrim()
    q = generateRandomPrim()

    n = p*q
    phi = (p-1) * (q-1)

    e = random.randint(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)

    d = egcd(e, phi)[1]
    d = d % phi
    if(d < 0):
        d += phi

    return ((e, n), (d, n))


# Function to Encrypt
def encrypt(text, public_key):
    key, n = public_key
    ctext = [pow(ord(char), key, n) for char in text]
    return ctext


# Function to Decrypt
def decrypt(ctext, private_key):
    try:
        key, n = private_key
        text = [chr(pow(char, key, n)) for char in ctext]
        return "".join(text)
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    while True:
        string = input("Enter Text: ")
        if string != 'exit':
            public_key, private_key = generate_keyPairs()
            print("Public: ", public_key)
            print("Private: ", private_key)
            ctext = encrypt(string, private_key)
            print("encrypted:", ctext)
            plaintext = decrypt(ctext, public_key)
            print("decrypted: " + plaintext + "\n")
        else:
            break
