import sys

def evaluate(graph, values, i):
    if values[i] not in ["/", "*", "+", "-"]:
        return int(values[i])

    if values[i] == "+":
        answer = 0
    elif values[i] == "*":
        answer = 1
    for x in range(len(graph[i])):
        if values[i] == "/":
            answer = answer / evaluate(graph, values, graph[i][x])
        elif values[i] == "*":
            answer = answer * evaluate(graph, values, graph[i][x])
        elif values[i] == "+":
            answer = answer + evaluate(graph, values, graph[i][x])
        elif values[i] == "-":
            answer = answer - evaluate(graph, values, graph[i][x])
    return answer


line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
while line2 != "":
    graph = list()
    pred = line1.split(",")
    values = line2.split(",")
    pred = [int(num) for num in pred]
    for predicate in range(len(pred)):
        graph.append(list())
    root = 0
    for predicate in range(len(pred)):
        if pred[predicate] != -1:
            graph[pred[predicate]].append(predicate)
        else:
            root = predicate
    print(evaluate(graph, values, root))
    line1 = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()