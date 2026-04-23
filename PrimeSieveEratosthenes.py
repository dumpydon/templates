
#-----------------------------------------------------------------------------
#PRIME SIEVE TEMPLATE
        #N is the range till you want sieve to be 
        N= 5*10**6      #❇️ 5 * 10**6 is very big    cant go 10**7 in python  

        prime = [True]*(N+1) #❇️ 
        #-----------------------------------------------
        p = 2 #starting with the first prrime.   
        while p*p<=N:

            if prime[p]==True:
                for i in range(p*p , N+1, p): #❇️ 
                    prime[i]==False
            p+=1

        #printing prime number 
        #-----------------------------------------------
        # ls =  [i for i in range(2, N+1) if prime[i]==True]   #❇️ 
#------------------------------------------------------------------------------

