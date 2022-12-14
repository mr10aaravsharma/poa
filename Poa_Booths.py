def compliment(num):
    num1 = [] 
    for i in num:
        if i is 0: 
            num1.append(1)
        elif i is 1: 
            num1.append(0)
    return num1

def sum(num1, num2):
    n1 = [str(integer) for integer in num1] 
    a1 = "".join(n1)
    n2 = [str(integer) for integer in num2] 
    a2 = "".join(n2)
    s = bin(int(a1, 2) + int(a2, 2))
    s = s.replace("b", "0")
    s = s[::-1]
    s = s[0 : len(num1)]
    s = s[::-1]
    S = list(map(int, s))
    return S

def asr(num):
    temp = num[0] 
    temp2 = num[0:-1] 
    d = [] 
    d.append(temp) 
    d.extend(temp2) 
    return d

m = input("Enter multiplicand (M) in binary (same length as multiplizer): ") 
M = list(map(int, m))
num = []
for i in range(len(M) - 1):
    num.append(0) 
num.append(1)

if M[0] is 0:
    M1 = compliment(M) 
    M2 = sum(M1, num)
elif M[0] is 1:
    temp = M[1:]
    temp = compliment(temp) 
    M = M[0:1] 
    M.extend(temp)
    M = sum(M, num)
    M1 = M
    temp = compliment(M1) 
    M2 = sum(temp, num)
    
print("Positive M: ", M)
print("Negative M: ", M2)
q = input("Enter multiplizer (Q) in binary (same length as multiplicand): ") 
Q = list(map(int, q))

if Q[0] is 1:
    temp = Q[1:]
    temp = compliment(temp) 
    Q = Q[0:1] 
    Q.extend(temp)
    Q = sum(Q, num)
print("Positive Q: ", Q) 
q1 = 0
A = []
for i in range(0, len(Q)):
    A.append(0) 
product = []
n = len(Q) 
n1 = len(Q) 
while n > 0:
    product.clear()
    if Q[n1 - 1] == 1 and q1 == 0:
        A = sum(A, M2)
    elif Q[n1 - 1] == 0 and q1 == 1:
        A = sum(A, M) 
    product.extend(A) 
    product.extend(Q) 
    product.append(q1) 
    product = asr(product)
    n2 = len(product)
    A = product[0:n1]
    Q = product[n1:n2 - 1] 
    q1 = product[n2 -1]
    n = n- 1
    
product = product[0:n2 - 1] 
num2 = []
for i in range(0, len(product) - 1):
    num2.append(0) 
num2.append(1)
if product[0] is 1:
    product = compliment(product) 
    product = sum(product, num2)
    s = [str(integer) for integer in product] 
    a_string = "".join(s)
    res = int(a_string, 2)
    print("Answer (in binary) = -", a_string)
    print("Answer = -", res)
else:
    s = [str(integer) for integer in product] 
    a_string = "".join(s)
    res = int(a_string, 2)
    print("Answer (in binary) = ", a_string) 
    print("Answer = ", res)