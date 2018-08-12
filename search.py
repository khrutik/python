L=[12,8,5,10,4,6,10,7]
k=10 # ค่าที่จะหา

result=[]

for i in range(len(L)):
    if L[i]==k:
        ##result="found"
        result.append(i)

print(result)
