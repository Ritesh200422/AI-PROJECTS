def read_adj(n):
 graph={}
 for i in range(n):
  print("Enter nodes reachable by node", i,end=":")
  nodes=list(input("").split())
  graph[str(i)]=nodes
 return graph
def bfs(visited, graph, node):
 visited.append(node)
 queue.append(node)
 while queue:
  s = queue.pop(0)
  print (s, end = " ")
  for neighbour in graph[s]:
   if neighbour not in visited:
      visited.append(neighbour)
      queue.append(neighbour)
n=int(input("Enter the number of nodes:"))
graph=read_adj(n)
for i in range(n):
 visited = [] # List to keep track of visited nodes.
 queue = [] #Initialize a queue
 print("Nodes visited from Node",i,end=": ")
 bfs(visited, graph,str(i))
 print()
