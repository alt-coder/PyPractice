import implementation

def validate(tree):
    return helper(tree.left,float("-inf"),tree.value) and helper(tree.right,tree.value,float("inf"))

def helper(tree,mini,maxi):
    if tree is None:
        return True
    if tree.value < mini or tree.value > maxi :
        return False
    return helper(tree.left,mini,tree.value) and helper(tree.left,tree.value,maxi)
