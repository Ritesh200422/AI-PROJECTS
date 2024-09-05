def adjread(n):

    graph ={}

    for i in range(n):
        print("Enter number of nodes reachable from ",i,end=":")
        nodes = list(input("").split())
        graph[str(i)] = nodes
    return graph

def dfs(visited,graph,node):
   if node not in visited:
       print(node,end=" ")
       visited.add(node)
       for neighbour in graph[node]:
           dfs(visited,graph,neighbour)

n = int(input("Enter number of nodes"))

graph = adjread(n)

for i in range(n):
    visited = set()

    print("nodes reachable ",i,end=":")
    dfs(visited,graph,str(i))
    print()