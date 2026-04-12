from ast import Pass


class SegTree:

#================================================================================================================================================================================
# ███████╗███████╗ ██████╗ ███╗   ███╗███████╗███╗   ██╗████████╗      ████████╗██████╗ ███████╗███████╗
# ██╔════╝██╔════╝██╔════╝ ████╗ ████║██╔════╝████╗  ██║╚══██╔══╝      ╚══██╔══╝██╔══██╗██╔════╝██╔════╝
# ███████╗█████╗  ██║  ███╗██╔████╔██║█████╗  ██╔██╗ ██║   ██║            ██║   ██████╔╝█████╗  █████╗  
# ╚════██║██╔══╝  ██║   ██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║            ██║   ██╔══██╗██╔══╝  ██╔══╝  
# ███████║███████╗╚██████╔╝██║ ╚═╝ ██║███████╗██║ ╚████║   ██║            ██║   ██║  ██║███████╗███████╗
# ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝            ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
#=============================================================================================================================================================================================================
#🌴🌴🌴🌴🌴🌴🌴🌴🌴MY OWN SEGMENT TREE TEMPLATE (FUNCTIONAL STYLE)🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴
#=================================================================================================

#why to use segment tree?
# Like the prefix, everything would work well for finding the range sum query.
#  Like, find sum for indexes in range 2 to 6; we can find that easily by prefix[6] minus prefix[2]. 
# But this prefix error thing fails for finding something like max. We can find max in range (2 to 6) and max in range [3 to 7], which will be totally different. 



# SEGMENT TREE COMPLEXITIES
# Tree size        : ≤ 4 * n nodes
# Build time       : O(n)
# Query time       : O(log n)
# Update time      : O(log n)
# Recursion depth  : O(log n)

# Why 4*n ?  Worst-case segment tree expansion when n is not power of 2.
# usually sengmmet tree has  n + n//2 + n//4 + n//8 ------> n leaf node + n-1 non leaf node so its 2n 
#But the 2N thing fails for the non-power of 2, so it's better to take 4N as the preferred size for segment tree. 





#   ROADMAP-------------------------------------------------------------

#    why to use segment tree
#    why the size is 4n
#    buildtree, pointupdate, RSQ
        # buildtree i, l, r  ---- 
        # pointupdate idx, val, i, l, r  ----  go leftsubtree basesd on idx<=mid or else go to right subtree
        # RSQ start, end, i, l, r  ----  3 cases non-overlapping,  complete, partial 

    # then i see the code of segment tree in def __init__ style

    #then we see the range update with the help f lazy segment tree,, not the simple point update 

    # then i saw the code for the range max index query # that stores the index of maxiii,, instead of max value

#--------------------------------------------------------------------------------------------------------------------------





#==========================================================================================================================
    arr = [...] #nums or whatever array
    # arr = input array
    n = len(arr)
    # segment tree size
    segt = [0]*(4*n)


#========================================================
#1 BUILD TREE-----------------------------------------------
    def buildtree(i, l , r):

        if l==r: #BASE CASE
            segt[i] = arr[l] #or arr[r] #cause they are same
            return 

        mid = (l+r)//2
        #leftsubtree_________
        buildtree(2*i+1, l, mid)
        #rightsubtree____________________
        buildtree(2*i+2, mid+1, r)

        segt[i] = segt[2*i +1] + segt[2*i +2]
        #       = leftchild + rightchild
    #------------------------------------------------------------
    #Time   : O(4*n) #Segment tree has at most 4*n nodes 
    #Space  : O(4*n) for segment tree array + O(log n) recursion stack



#========================================================================================
#2 POINT UPDATE in segTREE -- updating at some   idx   new  val  -------------------------
    def pointupdate(idx, val, i, l, r):
        #basecase
        if l==r: #BASE CASE
            segt[i] = val #update
            return 

        mid = (l+r)//2

        if idx<=mid: #leftsubtree
            pointupdate(idx, val, 2*i+1,  l, mid)
        else:#rightsubtree
            pointupdate(idx, val, 2*i+2, mid+1, r)
        
        segt[i] = segt[2*i +1] + segt[2*i +2]
    #------------------------------------------------------------------------------------
    #Time   : O(log n) #Each update operation is performed on at most log n nodes. height
    #Space  : O(log n) recursion stack


#===========================================================================================================================================================
#3 RANGE SUM QUERY -- -------------------------------------------------
    def query( start, end , i , l, r):
        #        |     |         (l r)

        #outofbounds
        if end < l or start >r:   # |  |  (l-r)   or   (l-r)   | |
            return 0            #return identity element #+inf for minsegt , #-inf for maxsegt -1 FOR RMIQ


        #completeoveralp    # |  (l-r)  |         #ie |start [l--representedbysegt[i]--r] end|
        if start <= l and r<= end:     
            return segt[i]

        else:
            mid = (l+r)//2
            left =  query(start, end, 2*i+1,   l, mid)
            right = query(start, end, 2*i+2, mid+1, r)
            return left+right
    #-----------------------------------------------------------------
    #Time   : O(log n) # Reason : query touches at most ~4*log₂(n) nodes
    #Space  : O(log n) recursion stack


#=============================================================================================
#4 USAGE
    buildtree(0, 0, n-1)
    # query range sum
    ans = query(start, end, 0, 0, n-1)
    # update index
    pointupdate(idx, val, 0, 0, n-1)

#############################################################################################################################################################################################
#############################################################################################################################################################################################

#HOW TO MODIFY FOR DIFFERENT PROBLEMS  (SEGMENT TREE MERGE STEP)
     
        #Only change the MERGE line inside build() and update():
        #       segt[i] = min(segt[2*i+1], segt[2*i+2])
        #and change the identity element returned in NO OVERLAP case.
        

        # Range SUM segmenttree---------------------------------------------
        # merge step:  segt[i] = segt[2*i+1] + segt[2*i+2]
        # identity element:   return 0

        # Range MINIMUM segmenttree---------------------------------------------
        # merge step:      segt[i] = min(segt[2*i+1], segt[2*i+2])
        # identity element:   return 10**14
        

        # Range MAXIMUM segmenttree---------------------------------------------
        # merge step:      segt[i] = max(segt[2*i+1], segt[2*i+2])
        # identity element:   return -10**14
#############################################################################################################################################################################################




    """ #DEFINE INNIT STYLE """
# def __init__() style
#DONT USE THE BELOW ONE , its stupid def __init__(self, arr):style

class SegmentT:

    def __init__(self, arr):
        self.arr = arr                     # original array 
        self.n = len(arr)                  # array size
        # segment tree size (4*n is safe upper bound)
        self.segt = [0] * (4*self.n)
        # build the tree immediately
        self.buildtree(0, 0, self.n-1)

# BUILD TREE-------------------------------------------------------------------------
    def buildtree(self, i, l, r):

        if l == r: #BASE CASE → leaf node
            self.segt[i] = self.arr[l]     # or arr[r], both same when l==r
            return

        mid = (l+r)//2
        self.buildtree(2*i+1, l, mid)
        self.buildtree(2*i+2, mid+1, r)
       
        self.segt[i] = self.segt[2*i+1] + self.segt[2*i+2]  #MERGE STEP


# UPDATE TREE (POINT UPDATE)-------------------------------------------------------------------------
    def pointupdate(self, idx, val, i, l, r):

        if l == r:  #BASE CASE → leaf node
            self.segt[i] = val
            return

        mid = (l+r)//2
        #go to correct subtree
        if idx <= mid: #go to left subtree
            self.pointupdate(idx, val, 2*i+1, l, mid)
        else: #go to right subtree
            self.pointupdate(idx, val, 2*i+2, mid+1, r)
        
        self.segt[i] = self.segt[2*i+1] + self.segt[2*i+2]  #MERGE STEP


# RANGE QUERY-------------------------------------------------------------------------
    def query(self, start, end,  i, l, r):
        #           |       |       (l r)

        #OUT BOUNDS#  |  |  (l---r)    or     (l---r)  |  |
        if l > end or  r < start:
            return 0                 # identity element for SUM tree # +inf for MIN tree  # -inf for MAX tree

        #COMPLETE OVERLAP # |  (l---r)  |
        if l >= start and r <= end:
            return self.segt[i]

        #PARTIAL OVERLAP
        else:
            mid = (l+r)//2
            left = self.query(start, end, 2*i+1, l, mid)
            right = self.query(start, end, 2*i+2, mid+1, r)
            return left + right
            #return min(left, right)  # for MIN segtree
            #return max(left, right)  # for MAX segtree


#############################################################################################################################################################################################
#############################################################################################################################################################################################
###########################################################################################################################################################################################








#############################################################################################################################################################################################
#we use lazy propogation for the range update thing ,, not just the normal point update(log n)
#    we can apply point update x times but it will take x*log n time in worst case it will go nlogn thats bad
# 
#   # ██╗      █████╗ ███████╗██╗   ██╗    ███████╗███████╗ ██████╗ ███╗   ███╗███████╗███╗   ██╗████████╗
    # ██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝    ██╔════╝██╔════╝██╔════╝ ████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
    # ██║     ███████║  ███╔╝  ╚████╔╝     ███████╗█████╗  ██║  ███╗██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
    # ██║     ██╔══██║ ███╔╝    ╚██╔╝      ╚════██║██╔══╝  ██║   ██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
    # ███████╗██║  ██║███████╗   ██║       ███████║███████╗╚██████╔╝██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
    # ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   

#=============================================================================================================================================================================================================
    
    # LAZY PROPAGATION IDEA
    # we maintain:
    #       segt[]  → segment tree values this will tell us the vauliue of [l---r]
    #       lazy[] array → pending updates not yet pushed to children
    #query size earlier X point update O(NlogN)❌   but with lazy propagation, we can do it in O(logN)✅


    #==========================================================================================================================
    # ⭐ LAZY PROPAGATION — 
    # suppose we want RANGE UPDATE:      add +x to every element in range [L,R]
    # If we perform this using point updates:     update(L), update(L+1), ..., update(R)
    # complexity becomes:      O((R-L+1) * log n) → worst case ≈ O(n log n) ❌

    # Lazy Propagation fixes this by DELAYING updates instead of applying them immediately.

    
    # A segment tree node represents an entire segment [l,r].
    # If the entire segment receives +x, we can update the node directly:
    #       segt[i] += (r-l+1) * x
    
    # But updating every child node right now is unnecessary and expensive.  Instead we RECORD the update and propagate it later.
    
    # This is where the lazy[] array comes in.
    # lazy[i] means:     "There is a pending update that still needs to be applied to this node's children."
    
    # So when a range update completely covers a node:
    #       1️ update segt[i] immediately      #SO we immediately update the segt[i] with the new value
    #       2 store the pending update in lazy[child nodes]
    
    # Later, whenever we VISIT that node (during query or deeper update),
    # we PUSH the lazy value downward:
    #       segt[i] += (r-l+1) * lazy[i]
    #       lazy[left child]  += lazy[i]
    #       lazy[right child] += lazy[i]
    #       lazy[i] = 0 #reset clearint that now nothing is pending 
    
    # This ensures children eventually receive the update only when necessary.
    

    # lazy[] stores those delayed updates that must still be applied.



    # Real-world analogy (salary coupon):
    # Boss: "Everyone gets +10 salary".
    # Instead of updating every employee salary value immediately,
    # Boss writes a note: lazy[employee] += 10. for all those employees
    # When someone checks their salary later, the pending bonus is applied.
      
    
#==========================================================================================================================
   


lazy = [0] *(4*n)
segt = [0] *(4*n) 


class LazySegTree:
#==========================================================================================================
    #It is exactly the same buildtree as it is. 
    def buildtree(arr, i, l, r):#EXACTLY THE SAME 
    #EXACTLY THE SAME 
    #EXACTLY THE SAME 
        if l == r:
            segt[i] = arr[l]
            return
        mid = (l+r)//2
        buildtree(arr, 2*i+1, l, mid)
        buildtree(arr, 2*i+2, mid+1, r)
        segt[i] = segt[2*i+1] + segt[2*i+2]

#=======================================================================================================================================================================================
    
    # LAZY RANGE UPDATE  (no the point update)
    def LazyRangeUpdate(start, end, val, i, l, r ):
        #-------------------------------------------------------------
        #BASE CASE⭐️ PUSH LAZY VALUE DOWN
        if lazy[i] != 0:

            segt[i] += (r-l+1) * lazy[i]
            if l != r:
                lazy[2*i+1] += lazy[i]
                lazy[2*i+2] += lazy[i]

            lazy[i] = 0 #reset
        #--------------------------------------------------------------


        #NO OVERLAP
        if end <l or start >r:
            return #simply

        #--------------------------------------------------------------
        #COMPLETE OVERLAP
        if start<=l and r<=end:
            segt[i] += (r-l+1)*val

            #storing for children nodes in lazy array
            if l != r: #if child nodes exists lazy propogate
                lazy[2*i+1] += val
                lazy[2*i+2] += val
            return

        #--------------------------------------------------------------
        # PARTIAL OVERLAP
        mid = (l+r)//2
        LazyRangeUpdate(start, end, val,   2*i+1, l, mid)
        LazyRangeUpdate(start, end, val,   2*i+2, mid+1, r)
        segt[i] = segt[2*i+1] + segt[2*i+2]
        
#======================================================================================================================================================================================
#############################################################################################################################################################################################
#############################################################################################################################################################################################





















# RANGE MAX INDEX QUERY VERSION (INDEX BASED)
# RANGE MAX INDEX QUERY VERSION (INDEX BASED)
# ██████╗ ███╗   ███╗ ██╗   ██████╗ 
# ██╔══██╗████╗ ████║ ██║  ██╔═══██╗
# ██████╔╝██╔████╔██║ ██║  ██║   ██║
# ██╔══██╗██║╚██╔╝██║ ██║  ██║▄▄ ██║
# ██║  ██║██║ ╚═╝ ██║ ██║  ╚██████╔╝ 
# ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═╝    ═▀▀▀▀▀▀
#                            

#############################################################################################################################################################################################
#############################################################################################################################################################################################
#🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴 RANGE MAXIMUM INDEX QUERY (DERIVED FROM RANGE MAX QUERY) 🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴
#############################################################################################################################################################################################
        # WHAT IS RANGE MAXIMUM QUERY ?
        # A Range Maximum Query Segment Tree stores:
        #       segt[i] = maximum value in the range [l,r]
        # Example:       arr = [5,2,9,3,7]
        # Query:       max(1,4) → 9
        
        #---------------------------------------------------------------------------------------------------
        # WHAT IS RANGE MAXIMUM INDEX QUERY ?
        # Instead of returning the VALUE of the maximum element,\\\ we return the INDEX where the maximum element occurs.
        
        # Example:       arr = [5,2,9,3,7]
        # Query:       max_index(1,4) → 2
        # Because:     arr[2] = 9
        #---------------------------------------------------------------------------------------------------
        # KEY IDEA:
        # Instead of storing the VALUE in the segment tree,
        # we store the INDEX of the maximum value.
        # Meaning:       segt[i] = index of maximum element in that segment
        # During merge we compare:
        #       arr[left_index]  vs  arr[right_index]
        # And store the index of the larger one.
        #---------------------------------------------------------------------------------------------------
        # COMPLEXITIES
        # Build Time       : O(n)
        # Query Time       : O(log n)
        # Update Time      : O(log n)
        # Tree Size        : ≤ 4*n
    
#=============================================================================================================================================================================================================
# SEGMENT TREE TEMPLATE
class SegTree:

    arr = [...] 
    n = len(arr)

    segt = [0]*(4*n)

#==========================================================================================================================

# BUILD TREE
    def buildtree(i, l, r):

        if l == r:
            segt[i] = l #earlier it was arr[l] in normal RMQ but we store l in RMIQ
            return

        mid = (l+r)//2
        buildtree(2*i+1, l, mid)
        buildtree(2*i+2, mid+1, r)
        #--------------------------------------------------------------------
        #RMQ RANGE MAX QUERY VERSION # segt[i] = max(segt[2*i+1], segt[2*i+2])
        # RANGE MAX INDEX QUERY VERSION (INDEX BASED)
        left_index  = segt[2*i+1]
        right_index = segt[2*i+2]

        # segt[i] = left_index if arr[left_index] >= arr[right_index] else right_index
        segt[i] = max(left_index, right_index, key=lambda x: arr[x])
        # if arr[left_index] >= arr[right_index]:
        #     segt[i] = left_index
        # else:
        #     segt[i] = right_index
        #------------------------------------------------------------------------------------------------


#===================================================================================================================================

# RANGE QUERY
    def query(start, end, i, l, r):

        #---------------------------------------------------------
        # NO OVERLAP
        if end < l or start > r:
            # RMQ# return -float('inf')
            # RANGE MAX INDEX QUERY
            return -1

        #-----------------------------------------------
        # COMPLETE OVERLAP
        if start <= l and r <= end:
            return segt[i] #this is fine because its a RMIQ only and the segt[i] stores the maximum index only thats right 

        #--------------------------------------------------------------
        # PARTIAL OVERLAP
        mid = (l+r)//2

        left  = query(start, end, 2*i+1, l, mid)
        right = query(start, end, 2*i+2, mid+1, r)
    
        # RMQ# return max(left, right)
        # RANGE MAX INDEX QUERY VERSION
        if left == -1:
            return right
        if right == -1:
            return left

        if arr[left] >= arr[right]:
            return left
        else:
            return right



#========================================================================================================================================================

# UPDATE
    def update(idx, val, i, l, r):

        if l == r: #BASE CASE → leaf node
            segt[i] = idx 
            return

        mid = (l+r)//2
        if idx <= mid: #that means it lies in left subtree
            update(idx, val, 2*i+1, l, mid)
        else: #that means it lies in right subtree
            update(idx, val, 2*i+2, mid+1, r)
        #--------------------------------------------------------------------------
        # RMQ # segt[i] = max(segt[2*i+1], segt[2*i+2])
        
        # RANGE MAX INDEX QUERY VERSION
        left_index  = segt[2*i+1]
        right_index = segt[2*i+2]
        if arr[left_index] >= arr[right_index]:
            segt[i] = left_index
        else:
            segt[i] = right_index
        #---------------------------------------------------------------------------------------------------

#==========================================================================================================
# USAGE
    buildtree(0,0,n-1) 
    # get index of max element in range
    max_index = query(l,r,0,0,n-1)
    # actual value
    max_value = arr[max_index]
#==========================================================================================================


#############################################################################################################################################################################################
#############################################################################################################################################################################################
