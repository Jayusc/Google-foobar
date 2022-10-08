def solution(h, q):
    # Your code here
    # Perform a binary search into the tree
    # Backtracking parent nodes
    top_node = 2 ** h - 1
    return [getParent(top_node, target) for target in q]


def getParent(top_node, target):
    prev_node = -1
    cur_node = top_node
    sub_tree = top_node
    while cur_node:
        # into the next level
        sub_tree = sub_tree >> 1
        left_node = cur_node - sub_tree - 1
        right_node = cur_node - 1
        if target == cur_node:
            return prev_node
        elif target <= left_node:
            prev_node = cur_node
            cur_node = left_node
            continue
        else:
            prev_node = cur_node
            cur_node = right_node
