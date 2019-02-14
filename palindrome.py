n=int(input())
num=n
pal=0
while  num>0:
     mod=num%10
     pal=(pal*10)+mod
     num=num//10
if pal==n:
	print("yes")
else :
	print("no")
