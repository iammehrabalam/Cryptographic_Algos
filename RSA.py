import sys
def FastMod(a,x,p):
    temp = 1
    while(x > 0):
        if( x % 2 != 0):
            temp = (temp * a) % p;
        a = (a * a) % p;
        x /= 2;
    return temp;
    
def inverse(a,b):
    t=0
    nt=1
    r=b
    nr=a
    while nr > 0:
        q=r//nr
        t,nt=nt,t-q*nt
        r,nr=nr,r-q*nr
    if r==1:
        return t+b
    else:
        return 'not'

def gcd(n,m):
    if n%m==0 and m==1:
    	return True
    elif n%m==0 and m!=1:
    	return False
    return gcd(m,n%m)
while True:
    print 'Enter Two Prime Number '
    p=int(raw_input('Enter 1st prime no'))
    q=int(raw_input('Enter 2nd prime no'))
    if p>10 and q>=11:
        break
    else:
        print 'Please enter Large prime i,e greater than 15'
message = raw_input('Enter your message')

n 	= p*q
qp  =   (p-1)*(q-1)
e=1
for i in range(2,qp):
	if gcd(i,qp):
		e=i
		break

mod = inverse(e,qp)
PublicKey1 , PublicKey2 = e,n
PrivateKey1 , PrivateKey2 = mod,n

Decrpt_text=[]
Encrpt_text=[]

print 'Encript message::  ',
for i in message:
    l=FastMod(ord(i),PublicKey1,PublicKey2)
    Encrpt_text.append(l)
    sys.stdout.write(str(l))
    sys.stdout.flush()

print '\n Decrpt message:: ',
for i in Encrpt_text:
    l=FastMod(i,PrivateKey1,PublicKey2)
    Decrpt_text.append(l)
    sys.stdout.write(chr(l))
    sys.stdout.flush()
print '\n'
