import sys

isOrder = True
order = 0
currentLines = 0
neighbours = []
queue = []
dictionary = {}


def bfs(graph, node):
    visited = [node]
    queue.append(node)
    level_dictionary = {0: 0}

    while queue:
        s = queue.pop(0)
        current_level = level_dictionary[s]

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                if neighbour not in level_dictionary:
                    level_dictionary[neighbour] = current_level + 1
                    queue.append(neighbour)

    max_level = max(level_dictionary.values())
    for key, value in level_dictionary.items():
        if value == max_level:
            print('%d %d' % (max_level, key))
            break


lines = sys.stdin.readlines()
for line in lines:
    line = line.strip()

    if isOrder:
        order = int(line)
        isOrder = False
    else:
        if currentLines < order - 1:
            neighbours = [int(x) for x in line.split()]
            dictionary[currentLines] = neighbours
            currentLines += 1
        else:
            neighbours = [int(x) for x in line.split()]
            dictionary[currentLines] = neighbours
            isOrder = True
            currentLines = 0
            bfs(dictionary, 0)
            dictionary = {}
