#===============================================================================================================
adj = [[] for _ in range(n)]    #n+1?     #Create adjacency list

for u, v in edges:
    adj[u].append(v)                        #u -> v  
    # adj[v].append(u)  #only if undirected #v -> u  


#===============================================================
#we sometimes use dictionaries to store the adjacency list, but not good might cause TLE because of hash collisions
adj = defaultdict(list)      #Create adjacency list

for u, v , d in edges:
    adj[u].append((v,d))                      #u -> v  
    adj[v].append((u,d))  #only if undirected #v -> u  



#=========================================================================================================
adjMatrix = [[0 for _ in range(n)] for _ in range(n)]
adjMatrix = [[0]*n for _ in range(n)]   #n+1?  #Create adjacency matrix
#[[0000],0000],[0000],[0000],0000],[0000]]

adjMatrix = [[0 for _ in range(m)] for _ in range(n)]
adjMatrix = [[0]*m for _ in range(m)]  


for u, v in edges:
    adjMatrix[u][v] = 1 #or weight instead of 1  if weighted #u -> v  
    adjMatrix[v][u] = 1  #only if undirected                 #v -> u  



#======================================================================================================

 #this is the code you can use to convert adjlist to edges[u,v]
n= len(adj)      #this is the code you can use to convert adjlist to edges[u,v]

#Code to create edges from adjacency list. 
edges = []
for u in range(n):
    for v in adj[u]:
        edges.append((u,v))

##=========================================
edges = []

for i , ls in enumerate(adj):
    l = len(ls)
    if l>0:
        for j in range(l):
            edges.append([i, ls[j]])
##=========================================================================================================

#====================================================================================================================================================================


visi = [0]*(n+1) #same
# visi = [0 for _ in range(n+1)]



#====================================================================================================================================================================
#=================================================================================================================
#connected components using visited array (DFS)  #count 
visi = [0]*n  #visited array

def dfs(node):
    visi[node] = 1 #mark visited
    # cur.append(node)
    for nei in adj[node]:  
        if visi[nei] == 0:
            dfs(nei)    
#--------------------------------------------
components = 0 #count of connected components

for i in range(n):
    if visi[i] == 0: #if not visited
        dfs(i)         #call for dfs/bfs
        components += 1
# return components

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
visi = [0]*n  #visited array
comps = []                  #list of components (each as list of nodes)

def dfs(node):
    visi[node] = 1 #mark visited
    temp.append(node)
    for nei in adj[node]:  
        if visi[nei] == 0:
            dfs(nei)    
#-------------------------------------------
for i in range(n):
    if visi[i] == 0: #ifnot visited
        temp = []
        dfs(i)
        comps.append(temp)
# return comps

#====================================================================================================================================================================
#====================================================================================================================================================================

#=================================================================================================================
# 😈😈😈😈😈😈😈😈 BFS 😈😈😈😈😈😈 (Breadth-First Search) 😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈
#=================================================================================================================
#====================================================================================================================================================================
#BFS (Breadth-First Search)
#we use a visi = [0]*(n)
    #we use a q = deque(src)
    #we mark the visi[src] as 1
    #while q:
    #   node = q.popleft()
    #   for nei in adj[node]: #push the nei of popped node in the q
    #       if visi[nei] == 0:  
    #           visi[nei] = 1  #mark nei
    #           q.append(nei)  #push

visi = [0]*(n) 

def bfs(src): 
    q = deque([src])     #q initiated with source node
    visi[src] = 1        #mark visited

    while q:
        node = q.popleft()
        for nei in adj[node]:
            if visi[nei] == 0: #if not visited
                q.append(nei)  
                visi[nei] = 1

for i in range(n):   #for all nodes checking calling bfs if not visited
    if visi[i] == 0:
        bfs(i)

#-----------------------------------------------------------------------------------

#SPACE  COMPLEXITY :O(n)  #visited array + queue 
#TIME COMPLEXITY of BFS is O(V+2E) or O(n) + O(2E).\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Every vertex is being pushed into the queue, then we pop it in a for loop for all its in degrees. 
# And we know that the sum of the in-degree plus out-degree is equal to the O(2E) edges, be it directed or undirected. 
#So, in total, every vertex is being visited once and every edge is being visited twice (once for each of its endpoints).
#O(n) for visiting all nodes and 
# O(2E) for visiting all adjacent nodes.
#-------------------------------------------------------------------------------------------------------------------
#PRINTING THE BFS TRAVERSAL

visi = [0]*(n) 

def bfs(src): 
    q = deque([src])     
    visi[src] = 1        
    temp = [] #*************************
        
    while q:
        node = q.popleft()
        temp.append(node) #****************
        for nei in adj[node]:
            if visi[nei] == 0: 
                visi[nei] = 1
                q.append(nei)  
    return temp #*************************

for i in range(n):   
    if visi[i] == 0:
        bfs(i)

#------------------------------------------------------------------------------------
#=====================================================================================================================================================

#BFS FOR MATRIX 2D GRID

def bfs(r,c):
    q = deque()  #FIFO
    q.append((r,c,0))

    visi= [[0 for _ in range(n)] for _ in range(m)] #visited matrix created
    visi[r][c]=1     #marked in the visited array

    while q:
        row, col, dis = q.popleft()

        # If we reach a 0 → nearest 0 found
        if mat[row][col] == 0:
            return dis

        directions = [ (0,-1),
                 (-1,0),     (1,0),
                       (0,1) ]

        for delr , delc in directions:
            nrow , ncol = row+delr, col+delc
            
            if 0<=nrow<m and 0<=ncol<n:
                if visi[nrow][ncol]==0:
                    visi[nrow][ncol]= 1 #marking it 1
                    q.append((nrow,ncol,dis+1))

    return -1




#====================================================================================================================================================================
#=================================================================================================================
# 😈😈😈😈😈😈😈😈 DFS 😈😈😈😈😈😈 (Depth-First Search) 😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈
# DFS (Depth-First Search)
#====================================================================================================================================================================

# adj = .....

visi = [0]*(n)

def dfs(node):
    visi[node] = 1
    for nei in adj[node]:       
        if visi[nei] == 0:
            dfs(nei) #recursive calling for nei

for i in range(n):   #for all nodes checking calling dfs if not visited
    if visi[i] == 0:
        dfs(i)



#================================================================================================================
#2D GRID DFS



visi= [[0 for _ in range(n)]for _ in range(m)]  #visited matrix created_____

directions = [ (0,-1),
        (-1,0),      (1,0),
                (0,1) ]

#-------------------------------------------------------------------
def dfs(r,c):

    visi[r][c]=1                    #marking in the visited array

    
    for dr, dc in directions:

        nr, nc = r+dr, c+dc

        if 0<=nr<m and 0<=nc<n:     #check valid range of coordinates
            if grid[nr][nc]=='O' and visi[nr][nc]==0: #and not visited
                dfs(nr, nc)         #recursive calling____________



 #-----------------------------------------------------------
        def dfs(r,c):
            size =1    #RIGHT

            visi[r][c] = 1 #marking it visited 
            
            for dr, dc in directions:
                nr , nc = r+dr, c+dc

                if 0<=nr<n and 0<=nc<m:
                    if visi[nr][nc] == 0 and grid[nr][nc] ==1 :
                        # ⭐️size+=1❌ #I WAS DOING THIS WRONG HERE  THIS IS SHIT 
                        size += dfs(nr, nc) #recursice calling dfs

            return size



#=====================================================================================================================================================================================================


directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#                     ↑  
#                   ←   →
#                     ↓



directions = [ [-1,-1],[-1,0],[-1,1],  [0,-1],[0,0],[0,1],  [1,-1],[1,0],[1,1]]       #[0,0]    is useless as it will give the same orignial point only
#                            ↖ ↑ ↗
#                            ← 0 →
#                            ↙ ↓ ↘



#================================================================================================================
visi = [[0 for _ in range(m)] for _ in range(n)]


#--------------------------------------------------------------------------------
count= 0 
def dfs(r,c):
    # nonlocal #count 
    visi[r][c] = 1 #marking it 1
    count+=1

    dir = [(-1,0),
    (0,-1),       (0,1),
            (1,0) ]
#-----------------------------------------------------------------
    for dr,dc in dir:
        nr, nc = r+dr, c+dc

        if 0<=nr<n and 0<=nc<m: #check valid range of coordinates
        #---------------------------------------------
            if grid[nr][nc]==1 and visi[nr][nc]==0:
                dfs(nr, nc) #recursive calling






#============================================================================================================================================================
visi= [[0 for _ in range(n)] for _ in range(m)] #visited matrix created

# BFS from all boundary land cells
def bfs(r,c):
    visi[r][c]=1     #marked in the visited array

    q = deque()  #FIFO
    q.append((r,c))
    
    while q:
        r, c = q.popleft()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]   
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <=nr< m and 0 <= nc < n: #in boundary check

                if grid[nr][nc]==1 and visi[nr][nc]==0:
                    visi[nr][nc]=1
                    q.append((nr, nc))
#----------------------------------------------------------------------------------------------------------------------------

def bfs(r,c):
    q = deque() #dont initilize like q = deque((r,c))❌   deque([(r,c)])✅ rather use append below
    q.append((r,c))
    visi[r][c]=1   #marking it visited only do it here 
    size = 0

    while q:
        r,c = q.popleft()
        # visi[r][c]=1 #WRONG NOT HERE
        
        size+=1

        for dr, dc in dir:
            nr, nc = r+dr, c+dc

            if 0<=nr<n and 0<=nc<m:
                if visi[nr][nc]==0 and grid[nr][nc]==1:
                    visi[nr][nc]=1 #mark visited 
                    q.append((nr,nc))
    return size

#MISTAKES I WAS DOING 
# 1. I WAS MARKING IT VISITED WHEN I APPENDED IT TO THE QUEUE INSTEAD OF WHEN I POPPED IT FROM THE QUEUE
# 2. I WAS INITIALIZING THE DEQUE WITH (r,c)❌   deque([(r,c)])✅ rather use append below
#================================================================================================================











#=====================================================================================================================================================================================================






#================================================================================================================



#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------




#================================================================================================================


#=====================================================================================================================================================================================================




#--------------------------------------------------------------------------------



#================================================================================================================

#--------------------------------------------------------------------------------



#=====================================================================================================================================================================================================




#================================================================================================================

#--------------------------------------------------------------------------------







#=====================================================================================================================================================================================================



#--------------------------------------------------------------------------------




#================================================================================================================


