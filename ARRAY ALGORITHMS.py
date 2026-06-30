#ARRAYS ALGORITHMS

# TWO SMALLEST MINIMUMS---------------------------------in sinlge pass 
mia = 10**14 # smallest
mib = 10**14 

for el in nums:
    if el <=mia:
        mib = mia
        mia = el
    elif mia < el < mib:
        mib = el

print(f"{mia=}, {mib=}")
nums.sort()
mia = nums[0]
mib = nums[1]


#======================================================================================
#1 DUTCH NATIONAL FLAG  ALGORITHM  🟥 ⬜️ 🟦
#======================================================================================
        #this is a Dutch national flag thing   # see leetcode 75 sort colors 
        # https://leetcode.com/problems/sort-colors/submissions/1895885650
#------------------------------------------------------------------------------------

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
#=================================================================================================================================================






#======================================================================================================
#2 BOOYER MOORE VOTING  ALGORITHM ,,, tell which el appears more than n/2 times
#======================================================================================================
        # 169. Majority Element https://leetcode.com/problems/majority-element/submissions/2018060019
        # 229. Majority Element II https://leetcode.com/problems/majority-element-ii/solutions/8305029/boyer-moore-n3-voting-algo-explained-bru-gpnm
        # nums = [2,2,1,1,1,2,2]  len =7 , 2 appears 4 times so its >n/2 appearance
#-----------------------------------------------------------------------------------------------------
       
        #voting step-----------------------------
        candid = None
        count = 0 
        for el in nums:
            if count == 0:
                candid = el
                count =1
            elif el ==candid:
                count+=1
            else:
                count-=1
        # return candid


        #verification step-----------------------------
        verif = nums.count(candid)
        # verif = sum(x==candid for x in nums)
        return candid if verif>n/2 else -1


#=================================================================================================================================================================










#======================================================================================================
#3 KADANE's  ALGORITHM, tells
#======================================================================================================
        # 169. Majority Element https://leetcode.com/problems/majority-element/submissions/2018060019
        # nums = [2,2,1,1,1,2,2]  len =7 , 2 appears 4 times so its >n/2 appearance
#-----------------------------------------------------------------------------------------------------
       
        #voting step-----------------------------
        

        #verification step-----------------------------
        

#=================================================================================================================================================================



















































