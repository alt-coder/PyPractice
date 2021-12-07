from implementation import BST, inorder
import implementation as im

def construct(arr):
    if len(arr) == 0:
        return
    mid = int(len(arr)/2)
    root = BST(arr[mid])
    root.left = construct(arr[:mid])
    root.right = construct(arr[mid+1:])
    return root
if __name__ == "__main" :
    arr = [1,2,5,7,10,13,14,15,22]
    a = construct(arr)
    res=[]
    im.inorder(a,res)
    print(res)
