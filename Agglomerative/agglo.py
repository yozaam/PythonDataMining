edges = [[0, 1, 2, 2, 3], [1, 0, 2, 4, 3], [2, 2, 0, 1, 5], [2, 4, 1, 0, 3],
         [3, 3, 5, 3, 0]]

vertii = ['A', 'B', 'C', 'D', 'E']
#          0   1   2   3   4

pos = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

#hard coded all edges!
n = 5
d = 0  #threshold
k = n  # no of clusters
clusters = [[val] for val in vertii]

print("<", d, ",", k, ",", clusters, ">")

while k > 1:
    oldk = k
    d = d + 1
    #now i have to merge them somehow!
    #for each clusters
    #go through the edges find if anyone has a distance of <=d
    for i in range(0, len(clusters)):
        cluster = clusters[i]
        for vertex in cluster:
            for j in range(0, len(clusters)):
                if i != j:
                    othercluster = clusters[j]
                    for othervertex in othercluster:
                        if othervertex != vertex:
                            distance = edges[pos[vertex]][pos[othervertex]]
                            #get edge value from graph!
                            if distance <= d:
                                clusters[i] = cluster + othercluster
                                clusters[j] = []
                                #delte old guy and put the merge!
                #checking all my neighbours if any of them
                #is inside the distance threshold
                #that cluster and add it to my cluster!

    #remove all empty clusters
    clusters = [cluster for cluster in clusters if cluster != []]
    k = len(clusters)
    print("<", d, ",", k, ",", clusters, ">")

    #BAD COMPLEXITY! Should try union find!
    #OUTPUT:
# < 0 , 5 , [['A'], ['B'], ['C'], ['D'], ['E']] >
# < 1 , 3 , [['A', 'B'], ['C', 'D'], ['E']] >
# < 2 , 2 , [['A', 'B', 'C', 'D'], ['E']] >
# < 3 , 1 , [['A', 'B', 'C', 'D', 'E']] >
