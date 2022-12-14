def ones_comp(num): 
    comp = ''
    for el in num:
        if el=='1': 
            comp+='0'
        else: 
            comp+='1'
    return comp

def twos_comp(num): 
    num=ones_comp(num) 
    n=len(num)-1
    while n>=0 and num[n]=='1':
        n-=1 
    if n<0:
        return '0'*len(num) 
    else:
        return num[:n]+'1'+num[n+1:]
    
def Add(A,M): 
    n = len(A)-1 
    ans='' 
    carry=0 
    while n>=0:
        if carry==0:
            if A[n]=='1' and M[n]=='0' or A[n]=='0' and M[n]=='1':
                ans = '1' + ans
                carry=0
            elif A[n]=='0' and M[n]=='0':
                ans = '0' + ans
                carry=0
            else:
                ans = '0' + ans
                carry=1
        else:
            if A[n]=='1' and M[n]=='0' or A[n]=='0' and M[n]=='1':  
                ans = '0' + ans
                carry=1
            elif A[n]=='0' and M[n]=='0': 
                ans = '1' + ans
                carry=0
            else:
                ans = '1' + ans 
                carry=1
        n-=1
    return ans

def left_shift(A, Qcon):
    ans = A + Qcon
    ans = ans[1:]
    return ans[:len(A)], ans[len(A):]

Q=int(input("Q: ")) 
M=int(input('M: '))

binary_Q = int("{0:08b}".format(Q)) 
binary_M = int("{0:08b}".format(M))

n = len(str(binary_Q))
if len(str(binary_M))<n + 1:
    binary_M = '0'*(n+1-len(str(binary_M))) + str(binary_M)
neg_M = twos_comp(binary_M) 
Qcon = str(binary_Q)
A = '0'*len(binary_M) 
print("A\tQ\tn")


for i in range(n):
    print(A, Qcon,'\t', n-i-1) 
    A, Qcon = left_shift(A, Qcon) 
    A = Add(A, neg_M)
    if A[0]=='1':
        Qcon=Qcon+'0'
        A=Add(A, binary_M)
    else:
        Qcon=Qcon+'1'
        
print(f"Quotient: {int(Qcon, 2)}") 
print(f"Remainder: {int(A, 2)}")