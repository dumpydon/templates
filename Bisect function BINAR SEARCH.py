

BISECT FUNCTION NOTES   BISECT_LEFT(NUMS, X, Key = )   BISECT_RIGHT(NUMS, X, Key = )


#=================================================================================================================
    First element ≥ x
    1. bisect_left (Lower Bound)
        bisect_left(nums, x, key = checkcount(funciton))
                    (arr  val key)
        

        First element ≥ x
        bisect_left lowerbound

            nums=[2,5,7,9] ..,, first element>=6? is 7 at index 2 so bisect left return index 2
                  0 1 2 3 

            idx = bisect_left(nums,6)
            ANS=====>2


            nums=[1,2,2,5,5,5,7,9] ..,, first element>=3 ???==>> is 5 at index 3 so bisect left return index 3
                  0 1 2 3 4 5 6 7 

            idx = bisect_left(nums,3)
            ANS=====>3


#=================================================================================================================
    Bisect function always works on sorted increasing arrays 
    Bisect function doesn't work on decreasingly sorted arrays. 
    If the array is given in decreasing order, you have to reverse it once,
    


     Yeahhh
     Time : O(log n)
     Space : O(1)
    Works ONLY on sorted arrays.
               
        nums = [1,2,2,2,4,5]
                0 1 2 3 4 5
                  L-----R
                  |2 2 2|

        bisect_left(nums,2)  -->>> ans = 1 ,, index of first 2 
        bisect_right(nums,2) -> ans = 4 ,,,index  after last occurence of  2

        count = bisect_right(nums,x) - bisect_left(nums,x)
              =      4 - 1 
              =      3     as [2] appeared thrice in our nums array
                    

        ans = bisect_left( range(high+1),  target,  key=checkfunction  )

        ==================================================
        bisect_left  = first index where nums[i] >= x   
        bisect_right = first index where nums[i] > x

        ========================================
            idx = bisect_left       >=
            idx = bisect_right      >
        =========================================

        bisect_left(nums, x,  key = checkcount(funciton))
        bisect_right(nums, x, key = checkcount(funciton))
                   (arr, val, key)            
        ==================================================

#=================================================================================================================



    First element > x
    2. bisect_right (Upper Bound)
        bisect_right(nums, x, key = checkcount(funciton))
                    (arr  val key)

        First element > x
        bisect_right gives upper bound

            nums=[2,5,5,5,7,9] ..,, first element>5 ???===>> is 7 at index 4 so bisect_right returns index 4
                  0 1 2 3 4 5
            idx = bisect_right(nums,5)
            ANS=====> 4

        
            nums=[1,2,2,5,5,5,7,9] ..,, first element>3 ???==>> is 5 at index 3 so bisect_right return index 3
                  0 1 2 3 4 5 6 7 
            idx = bisect_right(nums,5)
            ANS=====> 3
# =================================================================================================================
