def read_adj(n):
 graph={}
 for i in range(n):
  print("Enter nodes reachable by node", i,end=":")
  nodes=list(input("").split())
  graph[str(i)]=nodes
 return graph
def dfs(visited, graph, node):
 if node not in visited:
  print (node,end=" ")
  visited.add(node)
  for neighbour in graph[node]:
   dfs(visited, graph, neighbour)
n=int(input("Enter the number of nodes:"))
graph=read_adj(n)
for i in range(n):
 visited = set() # Set to keep track of visited nodes.
 print("Nodes visited from Node",i,end=": ")
 dfs(visited, graph,str(i))
 print()

