# (2,2) (3,4) 
# -> (2,2) (2,3) (2,4) (3,2) (3,3) (3,4)
# 시간 초과

def main():
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    for _ in range(m):
        x1,y1,x2,y2 = map(int, input().split())
        print(graphSum(graph,x1,y1,x2,y2))

def graphSum(graph,x1,y1,x2,y2):
    numSum = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            numSum += graph[x-1][y-1]
    return numSum

if __name__== "__main__":
    main()