def calc_distance(origin, dest, distances):
    neighbour_q = [origin]  # queue
    visited = []    # tracking visited
    curr_dist = 0   # distance from origin
    neighbour_dist = {origin:curr_dist} # tracking destination and its distance from origin
    # print(neighbour_q)
    while neighbour_q:
        # print(neighbour_q)
        visit = neighbour_q.pop(0)
        visited.append(visit)
        
        neighbours = find_neighbour(visit, distances)
        curr_dist = neighbour_dist[visit] + 1
        for n in neighbours:
            if n not in visited:
                neighbour_q.append(n)
            if n not in neighbour_dist:
                neighbour_dist[n] = curr_dist
        
        # print(visit)  
        # print(neighbour_dist)
                
    # print(visited)
    print(neighbour_dist)
    if dest in neighbour_dist:
        return neighbour_dist[dest]

    return -1

def find_neighbour(city, distances):
    edges = distances.keys()
    edges = filter(lambda edge: f'{city}->' in edge and distances[edge] != 0, edges)
    edges = list(edges)
    neighbour = []
    for edge in edges:
        neighbour.append(edge[edge.index('->')+2:])
    # print(neighbour)
    return neighbour

graph = {"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette,Lafayette->XX,XX->Springfield"}

# split edges from string
edges = graph['graph'].split(',')
vertex = set()  # to store unique vertex (city)
distances = {}  # to store distances between vertex (city)

# enter edges with length 1 to dict distances
for edge in edges:
    cities = edge.split('->')   # get just the cities
    distances[cities[0] + '->' + cities[1]] = 1  # enter the distance between to edge
    distances[cities[1] + '->' + cities[0]] = 1  # enter the distance between to edge, the reverse
    vertex.update(cities)   # enter unique cities to set

vertex = list(vertex)   # convert set to list
for i in range(len(vertex)):
    for j in range(len(vertex)):
        # if origin and destination is the same city
        if vertex[i] == vertex[j]:
            distances[vertex[i] + '->' + vertex[j]] = 0
        elif vertex[i]+vertex[j] not in distances:
            pass
            # dist = calc_distance(vertex[i], vertex[j], distances)
            # distances[vertex[i] + '->' + vertex[j]] = dist
            # distances[vertex[j] + '->' + vertex[i]] = dist
    

# print(edges)
# print(vertex)
# print(distances)
# find_neighbour('Chicago', distances)
print(calc_distance('Springfield', 'Lafayette', distances))