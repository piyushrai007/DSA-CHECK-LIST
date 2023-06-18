a = [-2,-3.4,-1,-2,1,5]
max = float('-inf')
for i in range(len(a)):
  for j in range(i,len(a)):
    sum = sum(a[i:j])
    max = max(max,sum)
print(max)    
    
    
    
    
    
    
