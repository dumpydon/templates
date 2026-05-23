# 🎃PRIME🎃SIEVE🎃TEMPLATE🎃

#===================================================================
    #PRIME SIEVE TEMPLAATE--------------
        N = n #/ max(arr)    # 10**5 works, but beyond this is too much 
        isprime = [True]*(N+1) #initillytinking all are prime
        isprime[0] = isprime[1] = False

        for p in range(2, int(N**0.5) + 1): #FASTER
            if isprime[p]:
                for i in range(p*p, N+1, p):
                    isprime[i] = False
                    
    #-------------------------------------------
    #-------------------------------------------------------
        # p = 2
        # while p*p<=N:
        #     if isprime[p]:
        #         for i in range(p*p, N+1, p):
        #             isprime[i] = False
        #     p+=1
            
#===================================================================







#===============================================================================
#WHEN n <= 1000
#--------------------------------------------------
def isprime(n):
    for d in range(2, int(n**0.5)+1):
        if n%d==0:
            return False
    return True

#sqrt(1000)=31      #SUPER okay ✔
#===============================================================================




    



#------------------------------------------
#memoized primality testing
    # dp-based template for prime sieve faster
    #1)very FEW numbers 
    #2)numbers HUGE 
    #3)many DUPLICATES
        @cache
        def isprime(x):
            if x < 2: return False
            d = 2
            while d*d <= x:
                if x%d==0: return False
                d += 1
            return True
#--------------------------------------------------







#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Prime 🪜 SIEVE Template
#-----------------------------------------------------------------------------
#PRIME SIEVE TEMPLATE
        #N is the range till you want sieve to be 
def sieve(N):
        
    N = 5* 10**6     #or  max(arr 
    prime = [True]*(N+1)
    prime[0] = prime[1] = False

    for p in range(2, int(N**0.5) + 1):

        if prime[p]:
            for i in range(p*p, N+1, p):
                prime[i] = False
        
    return prime

#Time Complexity: O(N log log N)
#Space Complexity: O(N)
  
#-----------------------------------------------------------------------------
#PRIME SIEVE SLOWER TEMPLATE
        #N is the range till you want sieve to be 
        # N= 5*10**6*2   #❇️    #to be on safer side of length of sieve
        N = max(temp)

        prime = [True]*(N+1) #❇️ 
        prime[0] = prime[1] = False

        p = 2 #starting with the first prrime.   

        while p*p<=N:

            if prime[p]==True:
                for i in range(p*p , N+1, p): #❇️ 
                    prime[i]=False
            p+=1

        #printing prime number 
        # ls =  [i for i in range(2, N+1) if prime[i]==True] #❇️ 
#------------------------------------------------------------------------------

