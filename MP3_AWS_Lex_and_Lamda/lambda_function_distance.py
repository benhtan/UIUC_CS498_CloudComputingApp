import json
import boto3

def lambda_handler(event, context):
    # graph = {"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette,Lafayette->XX,XX->Springfield"}
    # graph = {"graph": "New York->New Jersey,New Jersey->Boston,Boston->Philadelphia,New York->Washington,New York->Miami,New Jersey->Houston,Boston->Houston,Miami->Austin,Los Angeles->New Jersey,Los Angeles->Philadelphia,San Francisco->Las Vegas,Las Vegas->Washington,Houston->Las Vegas,Chicago->New Jersey,Los Angeles->Chicago"}
    graph = event

    # split edges from string
    edges = graph['graph'].split(',')
    vertex = set()  # to store unique vertex (city)
    distances = {}  # to store distances between vertex (city), from a given graph
    distances_calculated = {} # to store distances between vertex (city), calculated by program

    # enter edges with length 1 to dict distances
    for edge in edges:
        cities = edge.split('->')   # get just the cities
        distances[cities[0] + '->' + cities[1]] = 1  # enter the distance between to edge
        distances[cities[1] + '->' + cities[0]] = 1  # enter the distance between to edge, the reverse
        vertex.update(cities)   # enter unique cities to set

    # print(find_neighbour('New Jersey', distances))

    vertex = list(vertex)   # convert set to list
    for i in range(len(vertex)):
        for j in range(i, len(vertex)):
            # if origin and destination is the same city
            if vertex[i] == vertex[j]:
                distances_calculated[vertex[i] + '->' + vertex[j]] = 0
            elif vertex[i]+vertex[j] not in distances_calculated:
                pass
                dist = calc_distance(vertex[i], vertex[j], distances)
                distances_calculated[vertex[i] + '->' + vertex[j]] = dist
                distances_calculated[vertex[j] + '->' + vertex[i]] = dist
                # print(f'{vertex[i]}->{vertex[j]}: {dist}')

    distances.update(distances_calculated)
        

    # print(edges)
    # print(vertex)
    # print(distances)
    # print(find_neighbour('Chicago', distances))
    # print(calc_distance('Miami', 'Philadelphia', distances))
    
    # DynamoDB
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    table_CS498_MP3_Distance = dynamodb.Table('CS498-MP3-Distance')
    
    try:
        table_CS498_MP3_Distance.put_item(Item={'route': json.dumps(graph)}) # save original request packet
        
        with table_CS498_MP3_Distance.batch_writer() as batch:
            for route in distances:
                # table_CS498_MP3_Distance.delete_item(Key={'route': route}) # delete existing entree
                #table_CS498_MP3_Distance.put_item(Item={'route': route, 'source': route.split('->')[0], 'destination': route.split('->')[1], 'distance': distances[route]}) # insert new entree
                batch.put_item(Item={'route': route, 'source': route.split('->')[0], 'destination': route.split('->')[1], 'distance': distances[route]})    # batch insert
        
        return {
        'statusCode': 200,
        'body': 'Success'
        }
    except Exception as e:
        print(e)
        return {
        'statusCode': 500,
        'body': 'Error Saving'
        }

    
    
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
    # print(neighbour_dist)
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