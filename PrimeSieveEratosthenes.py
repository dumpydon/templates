# Prime 🪜 SIEVE Template
#-----------------------------------------------------------------------------
#PRIME SIEVE TEMPLATE
        #N is the range till you want sieve to be 
def sieve(N):
        
    N = 5* 10**16     #or  max(arr 
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

