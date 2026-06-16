#Sort is define using { } and used to remote duplicates & retun only unique values
ls={1,1,2,3,4,5,5,5,6,7,7,8}
print(set(ls))




print("Start small. Ship something.")

ls=[1,1,2,3,4,5,5,5,6,7,7,8]    #lists are defined using [] and set is defined as { }, range of index cannot be used for set. 
    #0 1 2 3 4 5 6 7 8 9 10 11
#print(set(ls))

# for i in ls:    #Element based for loop
#     #print(ls)
#     print(i)
    
    
for i in range(0,3):   #index based for loop
    print(ls[i])
    



ls=[1,1,2,3,4,5,5,5,6,7,7,8]
    #0 1 2 3 4 5 6 7 8 9 10 11
#print(set(ls))

# for i in ls:
#     #print(ls)
#     print(i)
    
    
# for i in range(len(ls)):
#     print(ls[i])
i=0
while i<len(ls):   *while can access index but cannot access through elements 
    print(ls[i])
    i=i+1
