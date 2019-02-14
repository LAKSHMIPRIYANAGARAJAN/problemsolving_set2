n=int(input())
num=n
pal=0
if n>1000:
	print("invalid")
else:
    while num<=1000 and num>0:
	     mod=num%10
	     pal=(pal*10)+mod
	     num=num//10
if pal==n:
	print("yes")
else :
	print("no")
