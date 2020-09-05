def reachable_position(x,y):
    points = []
    j = 1
    for i in range(2,0,-1):
        if 0 <= x + i < 8 and 0 <= y + j < 8:
            points.append((x + i, y + j))
        if 0 <= x + i < 8 and 0 <= y - j < 8:
            points.append((x + i, y - j))
        if 0 <= x - i < 8 and 0 <= y + j < 8:
            points.append((x - i, y + j))
        if 0 <= x - i < 8 and 0 <= y - j < 8:
            points.append((x - i, y - j))
        j+=1
    #print(points)
    return points

def explore(source,target):
    board = [[0 for i in range(8)] for j in range(8)]
    board[source[0]][source[1]] = 1
    queue = [source]
    while queue != []:
        position = queue.pop()
        newpositions = reachable_position(position[0],position[1])
        for newposition in newpositions:
            if board[newposition[0]][newposition[1]] == 0:
                board[newposition[0]][newposition[1]] = 1
                queue.insert(0,newposition)

    print("Target is marked as",board[target[0]][target[1]])
    for i in board:
        print(i)
    print(" ")
    return (board[target[0]][target[1]])

explore((1,2),(1,5))
