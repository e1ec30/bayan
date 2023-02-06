def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def find_d(e, p, q):
    return pow(e, -1, (p-1)*(q-1))

def enc_rsa(x, e, N):
    return pow(x, e, N)

def dec_rsa(y, d, N):
    return pow(y, d, N)

def bruteforce_N(N):
    for i in range(N):
        for j in range(N):
            if i * j == N:
                return [i, j]

e = 1
p = 11
q = 23
N = p*q
t = 1

print(f"N: {N}")
print(f"hex N:{hex(N)}")

tot = (p-1) * (q-1)
print(f"tot(N): {tot}")

for x in range(tot):
    if gcd(x, tot) == 1 and x > 1:
        e = x
        break
    else:
        continue

print(f"e: {e}")

d = find_d(e, p, q)

print(f"d: {d}")

bob_msg_cipher = 0b00001111
bob_secret = dec_rsa(bob_msg_cipher, d, N)

assert bob_msg_cipher == enc_rsa(bob_secret, e, N)
print(f"bob_secret: {bob_secret}")

captured_cipher = 0b10100011
captured_N = 0xf7
captured_e = 7
captured_p, captured_q = bruteforce_N(captured_N)
captured_d = find_d(captured_e, captured_p, captured_q)

captured_plain = dec_rsa(captured_cipher, captured_d, captured_N)

assert captured_cipher == enc_rsa(captured_plain, captured_e, captured_N)

print(f"Alice_message: {captured_plain}, Bob P: {captured_p}, Bob Q: {captured_q}, Bob d: {captured_d}")

