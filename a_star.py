class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def __str__(self):
        return str(self.adjacency_list)

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, v):
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
        return H[v]

    def a_star(self, start, stop):
        open_list = set([start])
        closed_list = set([])

        it = 0
        parents = {}
        parents[start] = None 

        g = {}
        g[start] = 0

        while len(open_list) > 0:
            it += 1
            n = None

            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print('Path doesnt exist')
                return

            if n == stop:
                path = []
                while parents[n] != None:
                    path.append(n)
                    n = parents[n]
                path.append(start)
                path.reverse()

                print('Path found: ', path)
                return

            for m, weight in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            
            closed_list.add(n)
            open_list.remove(n)

    def dijkstra(self, start, stop):
        Q = set([v for v in self.adjacency_list])
        D = dict([(v, float('inf')) for v in self.adjacency_list])

        D[start] = 0

        parents = {}
        parents[start] = None

        while len(Q) > 0:
            n = None 

            for v in Q:
                if n == None or  D[v] < D[n]:
                    n = v

            if D[n] == float('inf'):
                print('Path not found')
                return

            if n == stop:
                path = []
                while parents[n] != None:
                    path.append(n)
                    n = parents[n]
                path.append(start)
                path.reverse()
                print('Path found: ', path)
                return
            
            for m, weight in self.get_neighbors(n):
                if  D[n] + weight < D[m]:
                    D[m] = D[n] + weight
                    parents[m] = n

            Q.remove(n)

        print('Path not found')




if __name__ == "__main__":
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
graph.a_star('Arad', 'Buchares')
graph.dijkstra('Arad', 'Buchares')

