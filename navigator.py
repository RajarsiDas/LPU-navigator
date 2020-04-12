from collections import defaultdict
class Graph():
    def __init__(self):
       
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
       
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        
graph = Graph()
edges = [
    (0,1,7),
    (0,2 , 6),
     (0,3, 4.5),
      (1,3 ,4 ),
      (1,8 , 11),
      (2,4 , 3),
      (4,5 ,1 ),
      (4,3 , 2),
      (4,13,2.3),
      (3,6,3.67),
      (3,7,3.3),
      (3,8,1),
      (5,13,2),
      (6,7,7),
      (6,8,7.7),
      (6,9,8),
      (6,10,1),
      (7,10,2),
      (8,9,4),
      (9,10,5),
      (10,11,6),
      (10,15,3),
      (11,12,4),
      (12,16,4),
      (15,16,4),
      (15,17,8),
      (15,18,6),
      (17,19,2.98),
      (18,20,5.55),
      (19,21,6.5),
      (19,22,1.12),
      (19,20,2.23),
      (20,21,4),
      (20,23,2),
      (22,23,1),
      (22,24,6),
      (23,24,7),
      (13,14,8),
      (14,30,4.3),
      (25,26,5.4),
      (25,38,6.7),
      (26,27,3.4),
      (26,37,3.3),
      (27,28,0.2),
      (27,36,1.3),
      (27,35,11.7),
      (28,29,0.4),
      (28,36,6.8),
      (29,30,4.33),
      (29,36,0.5510),
      (30,31,0.3),
      (31,32,0.5),
      (32,33,0.4),
      (33,34,2.1),
      (33,36,9.543),
      (36,35,6.4),
      (36,37,4.32),
      (37,35,2.34),
      (37,38,4.33),
      (25,39,5.443),
      (25,41,50),
      (39,45,40),
      (39,40,4.3),
      (41,42,7),
      (42,45,7),
      (45,46,9),
      (46,47,6),
      (48,47,5),
      (47,49,2),
      (47,50,30),
      (48,49,0.44),
      (48,50,30),
      (40,50,2.0),
      (40,53,2.2),
      (53,54,0.2),
      (54,55,0.6),
      (55,56,0.3),
      (56,57,0.3),
      
    
]

for edge in edges:
    graph.add_edge(*edge)
def pathfinder(graph,initial,end):
   
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
                 
            
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
       
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
   
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    
    path = path[::-1]
    
    
    
    for i in path:
        
        if i==path[-1]:
            print(i)
        else:
            print(i,'  MOVE TO  BLOCK ',end=' ')
    print('THE TOTAL DISTANCE THAT YOU TRAVEL IS ->',weight*100,'meters')
    return path
print("Welcome to LPU NAVIGATION SOFTWARE")
n=int(input("Enter 1 to find the route ->"))
if n==1:
    src=int(input("PLEASE CHECK THE BUILDING NUMBER YOU WANT AND INPUT IT ->"))
    dest=int(input("ENTER THE BLOCK NUMBERR OF YOUR DESTINATION BUILDING ->"))
    pathfinder(graph,src,dest)
else:
    print("Wrong option Thank You For Using Us")
    
