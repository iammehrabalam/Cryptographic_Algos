# 2D Matrix
Lookup_Table = [[str(0) for x in range(96)] for x in range(96)] 

def Vigenere_table():
	j=1
	for i in range(32,127):
		Lookup_Table[0][j]=str(i)
		Lookup_Table[j][0]=str(i)
		j=j+1
	for i in range(1,96):
		k=int(Lookup_Table[i][0])
		for j in range(1,96):
			if k > 126:
				k=32
			Lookup_Table[i][j]=chr(k)
			k=k+1
			
def Decrept(etext,key,length):
	j=0
	D_message=''
	for i in etext:
		if j==length:
			j=0
		k=1
		while True:
			if Lookup_Table[k][ord(key[j])-31]==i:
				D_message=D_message+chr(31+k)
				break
			k=k+1
		j=j+1
	return D_message
def Encrept(text,key,length):
	j=0
	E_message=''
	for i in text:
		if j==length:
			j=0
		E_message=E_message+Lookup_Table[ord(i)-31][ord(key[j])-31]
		j=j+1
	return E_message

if __name__	==	'__main__':

	# Making Table
	Vigenere_table()

	key=raw_input('enter key::')
	text=raw_input('enter message ( ascii range 32 to 126 )::')
	etext=Encrept(text,key,len(key))

	print "Encrepted Text\n%s\n\n%s\n"%('-'*15,etext)

	dtext=Decrept(etext,key,len(key))

	print "Decrepted Text\n%s\n\n%s\n"%('-'*15,dtext)