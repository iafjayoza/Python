#Graph Coloring problem with back tracing

col = []

def graph_coloring(graph,colors,l):
    if l == len(graph):
        print(graph)
        col.append(graph.copy())
    else:
        for i in range(l,len(graph)):
            for j in range(len(colors)):
                if i == len(graph) - 1:
                    if graph[i-1] != colors[j] and graph[i-2] != colors[j] and graph[0] != colors[j]:
                        graph[i] = colors[j]
                        graph_coloring(graph, colors, i + 1)
                        graph[i] = i
                elif i == 1:
                    if graph[i-1] != colors[j] and graph[i+1] != colors[j] and graph[i+2] != colors[j]:
                        graph[i] = colors[j]
                        graph_coloring(graph, colors, i + 1)
                        graph[i] = i

                elif graph[i-1] != colors[j] and graph[i+1] != colors[j]:
                    graph[i] = colors[j]
                    graph_coloring(graph, colors, i + 1)
                    graph[i] = i
                else:
                    j += 1
            else:
                break


graph = [1,2,3,4]
colors = ["red","green","blue"]
graph_coloring(graph,colors,0)
print(len(col))