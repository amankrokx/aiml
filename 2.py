class Graph:
    def __init__(self, graph, heuristic, start):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.parent = {}
        self.status = {}
        self.solution = {}
     
    def apply_ao_star(self):        
        self.ao_star(self.start, False)

    def get_neighbors(self, v):     
        return self.graph.get(v, [])

    def get_status(self, v):         
        return self.status.get(v, 0)
    
    def set_status(self, v, val):    
        self.status[v] = val
    
    def get_heuristic(self, n):
        return self.heuristic.get(n, 0)    
 
    def set_heuristic(self, n, value):
        self.heuristic[n] = value            
        
    def print_solution(self):
        print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", self.start)
        print("------------------------------------------------------------")
        print(self.solution)
        print("------------------------------------------------------------")
    
    def compute_minimum_cost_children(self, v):      
        min_cost = float('inf')
        min_cost_nodes = []

        for node_info_list in self.get_neighbors(v):  
            cost = sum(self.get_heuristic(c) + weight for c, weight in node_info_list)
            
            if cost < min_cost:
                min_cost = cost
                min_cost_nodes = [c for c, _ in node_info_list]

        return min_cost, min_cost_nodes
    
    def ao_star(self, v, back_tracking):
        print("HEURISTIC VALUES  :", self.heuristic)
        print("SOLUTION GRAPH    :", self.solution)
        print("PROCESSING NODE   :", v)
        print("-----------------------------------------------------------------------------------------")
        
        if self.get_status(v) >= 0:
            min_cost, child_nodes = self.compute_minimum_cost_children(v)
            self.set_heuristic(v, min_cost)
            self.set_status(v, len(child_nodes))
            
            solved = all(self.get_status(child) != -1 for child in child_nodes)
            if solved:
                self.set_status(v, -1)
                self.solution[v] = child_nodes  
            
            if v != self.start:
                if self.parent.get(v):
                    self.ao_star(self.parent[v], True)
                
            if not back_tracking:
                for child_node in child_nodes:   
                    self.set_status(child_node, 0)   
                    self.ao_star(child_node, False)
                    
h1 = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}  
graph1 = {                                       
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],      
    'B': [[('G', 1)], [('H', 1)]],               
    'D': [[('E', 1), ('F', 1)]]             
}

G1 = Graph(graph1, h1, 'A')               
G1.apply_ao_star()
G1.print_solution()