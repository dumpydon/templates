"""
See LeetCode 1314 Submission Matrix Blocks from Using the 2D Prefix Grid Matrix Approach 
You can also have a look at LeetCode 304 in some query immutable. 
Define get rectangle query. 
https://leetcode.com/problems/matrix-block-sum/description/
https://leetcode.com/problems/matrix-block-sum/solutions/8439492/2d-prefixgrid-00-firstrow-firstcol-inner-vmtf
"""



def getPREFIX2D( grid: List[List[int]]) -> List[List[int]]:
	n = len(grid)
	m = len(grid[0])
	
	
#GRID PREFIX SUM MANNUAL #2D PREFIX SUM (RECTANGULAR GRID)
#=========================================================================================
	pref = [[0]*m for _ in range(n)]
	
	pref[0][0] = grid[0][0] #[0][0] #🔥
	
	for i in range(1,n): #copy first column
	  pref[i][0] = pref[i-1][0] + grid[i][0] 
	
	for j in range(1,m):  #copy first row
	  pref[0][j] = pref[0][j-1] + grid[0][j]
	
	for i in range(1,n): 
	  for j in range(1,m): #INNER FILLING
		  pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1]     + grid[i][j] #🔥
	
# Time: O(n*m) , Space: O(n*m)
#=========================================================================================
	
	
	
	
	

# GRID PREFIX sum using ACCUMULATE for row thign then manual column prefix
#=========================================================================
	from itertools import accumulate
	#RowPrefix-----------------------------------------------------------
	pref = [ list(accumulate(row)) for row in grid ]
	
	#ColPrefix------------------------------------------------------------
	for j in range(m):
	  for i in range(1, n):
		  pref[i][j] += pref[i-1][j] #just above element
# Time: O(n*m) , Space: O(n*m)
#===========================================================================

	
	
	

# GRID PREFIX two passs first pass rows second pass columns
#===============================================================
	pref = [row[:] for row in grid]      #make a copy of grid #🔥
	#RowPrefix-----------------------------------------
	for i in range(n):
	  for j in range(1, m):
		  pref[i][j] += pref[i][j-1]   #just left element
	
	#ColPrefix--------------------------------------
	for j in range(m):
	  for i in range(1, n):
		  pref[i][j] += pref[i-1][j] #just above element
# Time: O(n*m) , Space: O(n*m)
#=================================================================



	
#PREFIX SUM FILLING FOR SQUARE GRID WITH PADDING
#====================================================================================================
	# Extra first row and first column are all zeros.
	# No boundary checks required.
	pref = [[0]*(m+1) for _ in range(n+1)]
	
	for i in range(1,n+1):
	  for j in range(1,m+1):
		  pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1]     + grid[i-1][j-1] #🔥

# Time: O(n*m)  , Space: O(n*m)
#======================================================================================================




	
	
def getquery(pref, r1, c1, r2, c2):

	tot = pref[r2][c2]

	if r1 > 0:
		tot -= pref[r1-1][c2]
	if c1 > 0:
		tot -= pref[r2][c1-1]
	if r1 > 0 and c1 > 0:
		tot += pref[r1-1][c1-1]

	return tot
	
		
		
