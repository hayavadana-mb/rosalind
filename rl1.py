f=open("C:/Users/hayav/Downloads/xz.txt","r")
a=f.read()
j=0    
k=0
l=0
m=0
for i in a:
    if i == 'A':
        j=j+1
    elif i == 'C':
        k=k+1
    elif i == 'G':
        l=l+1
    elif i == 'T':
        m=m+1
            
print(j," ",k," ",l," ",m," ")
