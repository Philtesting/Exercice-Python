ch ="erodslqazrdsa212309"

n = 5

a= 0
b = n             
lt = []                
while a < len(ch):
	if b > len(ch): 
		b = len(ch)
	dec = ch[a:b]     
	lt.append(dec)       
	a = b
	b = b + n      
print(lt)

ch = ""              
i = len(lt)            
while i > 0 :
	i = i - 1        
	ch = ch + lt[i]
print(ch)