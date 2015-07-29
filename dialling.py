import re

pref_A = [1,268,46,4620,468,4631,4673,46732]
price_A = [0.9,5.1,0.17,0.0,0.15,0.15,0.9,1.1]

pref_B = [1,44,46,467,48]
price_B = [0.92,0.5,0.2,1.0,1.2]

def find_op(num) :
	lista = []
	listb = []

	for i in pref_A :
		if (str(i) in num) and (num.index(str(i)) == 0) :				
			lista.append(str(i))
		
	for j in pref_B : 
		if (str(j) in num) and (num.index(str(j)) == 0) :
			listb.append(str(j))
	for k in lista : 
		for f in listb : 
			if num == k and num == f: 
				lista[:] = []
				lista.append(num)
				listb[:] = []
				listb.append(num)
			elif num == k and num != f: 
				listb[:] = []
				lista[:] = []
				lista.append(num)
			elif num != k and num == f: 
				lista[:] = []
				listb[:] = []
				listb.append(num)
	l1 = lista
	l2 = listb
	return l1, l2

def cheapest(p1,p2) : 
	if p1 < p2 : 
		print 'Price for the operator A is cheaper = %.2f \n'%(p1)
	elif p1 > p2 : 
		print 'Price for the operator B is cheaper = %.2f \n'%(p2)
	elif p1 == p2 : 
		print 'Same price for both operator'

def get_price(l1,l2) : 
		
	if (len(l1) > 0) and (len(l2) > 0) : 
		print '\nPrefix was found in both operator\n'
		len1 = int(max(l1,key=len))
		len2 = int(max(l2,key=len))
		p1 = pref_A.index(len1)
		p2 = pref_B.index(len2)
		if (len1 > len2) : 
			
			print 'Prefix found in Operator A, price = %.2f \n'%(price_A[p1])
		elif (len1 < len2 ) :
			print 'Prefix found in Operator A, price = %.2f \n'%(price_B[p2])
		else : 
			print 'Price for the operator A is %.2f \n'%(price_A[p1])
			print 'Price for the operator B is %.2f \n'%(price_B[p2])
			cheapest(price_A[p1],price_B[p2])
	elif (len(l1) > 0) and (len(l2) == 0) : 
		print '\nPrefix found only in  A'
		p1 = pref_A.index(int(max(l1,key=len)))
		
		print '\nPrice for the operator A is %.2f \n'%(price_A[p1])
	elif (len(l1) == 0) and (len(l2) > 0) : 
		print '\nPrefix found only in  B'
		p2 = pref_B.index(int(max(l2,key=len)))
		print '\nPrice for the operator B is %.2f \n'%(price_B[p2])
	elif (len(l1) == 0) and (len(l2) == 0) : 
		print 'Number Not found'
	
number = raw_input("give me number to call : ")
if number.isdigit() :
	l1,l2 = find_op(number)
	get_price(l1,l2)
	#print max(l1,key=len)
	#print max(l2,key=len)
else : 
	print 'check your number please'
	
