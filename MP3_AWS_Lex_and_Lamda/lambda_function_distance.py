
graph = {"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}

edges = graph['graph'].split(',')
vertex = set()

for edge in edges:
    cities = edge.split('->')
    vertex.update(cities)


print(edges)
print(vertex)