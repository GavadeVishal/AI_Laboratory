def minimax(node, depth, is_maximizing_player):
    if depth == 0 or is_terminal(node):
        return evaluate(node)

    if is_maximizing_player:
        best_value = -float('inf')
        for child in get_children(node):
            value = minimax(child, depth - 1, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for child in get_children(node):
            value = minimax(child, depth - 1, True)
            best_value = min(best_value, value)
        return best_value

def is_terminal(node):
    pass

def evaluate(node):
    pass

def get_children(node):
    pass
