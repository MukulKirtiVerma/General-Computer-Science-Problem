
arr=[1,1,2,-100,4,5,45,9]
k=5
a=[0]*len(arr)
i=0
j=1
a[0]=arr[0]
count=1
while(j<len(arr)):
    #print(count,k,j)
    if(count>k-1): 
        print(a[j-1],arr[i])
        a[j]=a[j-1]-arr[i]+arr[j]
        i+=1
    else:
        a[j]=a[j-1]+arr[j]
        count+=1
    print(a)
    j+=1
print(max(a[k:]))

