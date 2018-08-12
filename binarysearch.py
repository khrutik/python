L=[-2,0,1,3,4,6,9,12,14,17,21]
k=12 # ค่าที่จะหา

result=[]
left=0
right=len(L)-1

while left<=right:
    # หาข้อมูลตรงกลาง
    mid=(left+right)//2
    m=L[mid]
    # หาข้อมูลตรงกลาง
    if k==m:
        result=mid
        right=-999
    # หาข้อมูลตรงกลาง
    if k<m:
        right=mid-1
    if k>m:
        left=mid+1

print(result)
