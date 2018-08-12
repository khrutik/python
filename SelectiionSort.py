L=[32,14,45,8,16]
S=[]
while L!=[]:
# หาข้อมูลที่น้อยที่สุด
    m=L[0]
    for x in L:
        if x<m:
            m=x

# ลบข้อมูลใน L
    i=L.index(m)
    m=L.pop(i)

# m เก็บข้อมูลที่น้อยที่สุดใน L
    S.append(m)

print(S)


