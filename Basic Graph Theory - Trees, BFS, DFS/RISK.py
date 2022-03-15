# cook your dish here
direction = [[0,1],[1,0],[-1,0],[0,-1]]
def inside(mat,x,y,n,m):
    if x>=0 and x<n and y>=0 and y<m:
        return True
    else:
        return False


def bfs_landfill(mat,i,j,n,m):
    size=0
    queue=[]
    mat[i][j]=0
    queue.append((i,j))
    while len(queue)!=0:
        x,y = queue.pop(0)
        size+=1
        for el in direction:
            x1,y1 = x+el[0],y+el[1]
            if inside(mat,x1,y1,n,m) and mat[x1][y1]==1:
                mat[x1][y1]=0;
                queue.append((x1,y1))
    return size
                
        
    
    

for _ in range(int(input())):
    n,m = map(int,input().split())
    mat = []
    for _ in range(n):
        li = list(map(int,input()))
        
        mat.append(li)
    
    land=[]
    for i in range(n):
        for j in range(m):
            if mat[i][j]==1:
                land.append(bfs_landfill(mat,i,j,n,m))
    
    land.sort(reverse=True)
    
    chef=0
    for k in range(1,len(land),2):
        chef+=land[k]
    print(chef)
    
    
    
    
    
        
