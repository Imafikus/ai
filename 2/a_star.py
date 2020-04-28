

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
    
    def __str__(self):
        return str(self.adjacency_list)

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def dijkstra(self, start, stop):
        Q = set([v for v in self.adjacency_list])
        print(Q)

        D = dict([(v, float('inf')) for v in self.adjacency_list])
        print(D)

        D[start] = 0

        parent = {}
        parent[start] = None

        iteration = 0

        while len(Q) > 0:
            
            current_best_node = None
            iteration += 1

            for w in Q:
                if current_best_node is None or (D[w] != float('inf') and D[w] < D[current_best_node]):
                    current_best_node = w

            if D[current_best_node] == float('inf'):
                print('Path doesnt exist')
                print('Num of iterations: ', iteration)
                return None

            if current_best_node == stop:
                path = []
                while current_best_node != None:
                    path.append(current_best_node)
                    current_best_node = parent[current_best_node]
                
                path.reverse()
                print('Path found: ', path)
                print('Num of iterations: ', iteration)
                return path

            
            for (m, weight) in self.adjacency_list[current_best_node]:
                if D[m] == float('inf') or D[current_best_node] + weight < D[m]:
                    D[m] = D[current_best_node] + weight
                    parent[m] = current_best_node
            
            Q.remove(current_best_node)

        print('No path found')

    def h(self, n):
        H = {
                'Oradea': 380,
                'Zerind': 374,
                'Arad': 366,
                'Timisoara' : 329,
                'Lugoj' : 244,
                'Mehadia' : 241,
                'Drobeta' : 242,
                'Sibiu' : 253,
                'Fagaras': 176,
                'Rimnicu Vilacea' : 193,
                'Pitesti' : 100,
                'Craiova' : 160,
                'Buchares' : 0
                }

        return H[n]

    def a_star(self, start, stop):
        open_list = set([start])
        closed_list = set([])

        g = {}
        g[start] = 0

        parent = {}
        parent[start] = start

        iteration = 0

        while len(open_list) > 0:
            current_best = None
            iteration += 1

            for v in open_list:
                if current_best is None or g[v] + self.h(v) < g[current_best] + self.h(current_best):
                    current_best = v
            
            if current_best == None:
                print('Path doesnt exist. Number of iterations: ', iteration)
                return
            
            if current_best == stop:
                path = []

                while parent[current_best] != current_best:
                    path.append(current_best)
                    current_best = parent[current_best]

                print('Path found: ', path)
                print('Number of iterations: ', iteration)
                return path
            
            for m, weight in self.get_neighbors(current_best):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parent[m] = current_best
                    g[m] = g[current_best] + weight

                else:
                    if g[m] > g[current_best] + weight:
                        g[m] = g[current_best] + weight

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(current_best)
            closed_list.add(current_best)

        print('Path doesnt exist')

        

        


def main():
    adjacency_list = {
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Arad': [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
    'Timisoara' : [('Lugoj', 111), ('Arad', 118)],
    'Lugoj' : [('Mehadia', 70), ('Timisoara', 111)],
    'Mehadia' : [('Drobeta', 75), ('Lugoj', 70)],
    'Drobeta' : [('Craiova', 120), ('Mehadia', 75)],
    'Sibiu' : [('Fagaras', 99), ('Rimnicu Vilacea', 80), ('Arad', 140)],
    'Fagaras': [('Buchares', 211), ('Sibiu', 99)],
    'Rimnicu Vilacea' : [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Pitesti' : [('Rimnicu Vilacea', 97), ('Craiova', 138), ('Buchares', 101)],
    'Craiova' : [('Rimnicu Vilacea', 146), ('Pitesti', 138), ('Drobeta', 120)],
    'Buchares' : [('Fagaras', 211), ('Pitesti', 101)]
    }

    graph = Graph(adjacency_list)

    print(graph.get_neighbors('Oradea'))

    graph.dijkstra('Oradea', 'Timisoara')
    graph.a_star('Oradea', 'Timisoara')

if __name__ == "__main__":
    main()