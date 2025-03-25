dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
nums={}

#concatenate 3 dictionaries
dic2.update(dic1)
dic3.update(dic2)
nums=dic3
print(nums)

#add new key and value
nums[7]=70
print(nums)

#update key 3 with value 80
nums[3]=80
print(nums)

#remove third item
del nums[3]
print(nums)

#sum all items
add=sum(nums.values())
print('sum=',add)

#multiply all items
pro=1
for value in nums.values():
    pro*=value
print('product=',pro)
#max and min values
mx=max(nums.values())
mn=min(nums.values())
print('maximum=',mx)
print('minimum=',mn)