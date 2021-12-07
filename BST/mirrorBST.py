from implementation import BST, inorder
from bstFromSortedArr import construct

def mirror(bst):
    if bst is None:
        return
    if bst.left is None and bst.right is None:
        return None
    bst.left,bst.right = bst.right,bst.left
    mirror(bst.left)
    mirror(bst.right)

if __name__ == "__main__" :
    arr = [1,2,5,7,10,13,14,15,22]
    a = construct(arr)
    res=[]
    z=inorder(a,res)
    print(res)
    mirror(a)
    res.clear()
    inorder(a,res)
    print(res)