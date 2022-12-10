def horizontalGoalState(dim):
    return [(x + 1) % (dim * dim) for x in range(dim * dim)]

def verticalGoalState(dim):
    return [((dim * (i % dim) + (i // dim) + 1) % (dim * dim)) for i in range(dim * dim)]

def spiralGoalState(dim, moveAxis='x'):
    goalState = [0 for i in range(dim * dim)]
    moves = {"x": (1, -1), "y": (dim, -dim)}
    moveIndex = {"x": 0, "y": 0}
    seen = []
    lastIndex = -moves[moveAxis][moveIndex[moveAxis]]
    while len(seen) < len(goalState):
        for _ in range(dim):
            lastIndex += moves[moveAxis][moveIndex[moveAxis]]
            if lastIndex >= dim * dim or lastIndex < 0 or goalState[lastIndex] in seen:
                lastIndex -= moves[moveAxis][moveIndex[moveAxis]]
                break
            goalState[lastIndex] = (len(seen) + 1) % (dim * dim)
            seen.append(goalState[lastIndex])
        moveIndex[moveAxis] = (moveIndex[moveAxis] + 1) % 2
        moveAxis = "x" if moveAxis == "y" else "y"
    return goalState

def yMajorSpiralGoalState(dim):
    return spiralGoalState(dim, moveAxis='y')

def xMajorSpiralGoalState(dim):
    return spiralGoalState(dim)