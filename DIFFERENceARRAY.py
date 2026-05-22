#---------------------------
    #difference array technique template 
    diff = [0]*(n)
    
    # x = 1
    for u, v, x in queries:
        
        diff[u] += x
        if v+1 <n:
            diff[v+1] -= x
    
    #-----------------------------------
    #CUMMULATING DIFFERENCE ARRAY WE MADE

    for i in range(1,n):
        diff[i] += diff[i-1]
    # print(diff) #= [0, 1, 2]
    #-----------------------------------



    # res= []
    # curr = 0 
    # for delta in diff:
    #     curr += delta
    #     res.append(curr)
    # print(res) #= [0, 1, 2]
    #-----------------------------------





        
        
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
