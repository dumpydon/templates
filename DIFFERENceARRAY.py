# Difference array is applied when we have to repeatedly do the range addition things. 
 # And we have to query fewer times. 


#DIFFERENCE ARRAY TECHNIQUE-----------------------------------------
    #--------------------------------------------------------
    n = len(arr)
    
    temp  = [0]*(n+1) #or n or n+5 whatever
    
    for a,b, x in queries:
        temp[a]   +=x
        temp[b+1] -=x
    
    #--------------------------------------------------------
    #ACCUMULATION STEP 
    arr = list(accumulate(temp))
 
    diff = list(accumulate(temp))
    
    #PREFIX SUM WAY
    #----------------------------------------
    # for i in range(1,n)
    #     temp[i]+=temp[i-1]
    # arr = temp[:]
        
    #------------------------------------
    # arr = []
    # curr=0
    # for el in temp:
    #     curr+=el
    #     arr.append(curr)
    #--------------------------------------------------









"""
# For example,
#---------------------------------------------------------------------------------------------------------
arr = [2, 9, 4, 5, 21, 4] 
       0  1  2  3   4  5 

querry = [[1,2,+1],  [0,4,-1],  [3,5,+3]]
           a b  x     a b x      a b x

arr = [2,  9,  4,  5,  21,  4] 
          +1  +1
      -1  -1  -1  -1  -1 
                  +3  +3   +3 
#--------------------------------------
diff =[-1  0  0  +2   +2   +3]
#--------------------------------------
newarr=[1, 9, 4,  7,   23,   7]
#--------------------------------------


to do this we can do like 
#DIFFERENCE ARRAY TECHNIQUE--------------------------------------------
       
arr = [2,  9,  4,  5,  21,  4] 

temp = [0, 0,  0,  0,  0,   0,  0 ]
convertit to
       [-1 +1      +2       +1   -2  #THIS IS WHAT DIFFERENCE ARRAY DO
accumulate
diff   [-1  0  0   +2  +2   +3   -1]

diff = list(accumulate(temp)))
#--------------------------------------
diff =[-1  0  0  +2   +2   +3]
#--------------------------------------
#---------------------------------------------------------------------------------------------------------
"""
 











        
        
    #BELOW THIS USE THE ABOVE DIFFERNCE ARRAY CODE AND WRITE SOLUTION
    #-----------------------------------------------------
    #2381. Shifting Letters II
    #-----------------------------------------------------
    # #CREATING NEW CH
    # ans = []
    # for i in range(n):
    #     ch = s[i]
    #     neword =  ( ord(ch)-97 + res[i] )%26  +97

    #     newch = chr(neword)
    #     ans.append(newch)
    
    # return "".join(ans)
    #-----------------------------------------------------
