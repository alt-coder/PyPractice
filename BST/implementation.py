from typing import Counter


class BST:
    def __init__(self,value):
        self.value= value
        self.left = None
        self.right  = None
    
    def insert(self,value):
        currentnode = self
        while True:
            if value < currentnode.value:
                if currentnode.left is None:
                    currentnode.left = BST(value)
                    break
                else:
                    currentnode = currentnode.left
            else:
                if currentnode.right is None:
                    currentnode.right = BST(value)
                    break
                else:
                    currentnode = currentnode.right
        return self
    
    def contains(self,value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif  value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False
    
    def remove(self,value):
        currentnode=self
        pararntnode= None
        while (currentnode != None):
            nd = currentnode
            if value < currentnode.value:
                currentnode = currentnode.left
            elif value > currentnode.value:
                currentnode = currentnode.right
            elif value == currentnode.value:
                break
            pararntnode = nd
        while (currentnode is not None):
            node = None
            if(currentnode.right is not None):
                node = currentnode.right
            else:
                node = currentnode.left
            
            if node is not None:
                currentnode.value = node.value
            else:
                if pararntnode.left is currentnode:
                    pararntnode.left = None
                else: pararntnode.right = None
                break
            pararntnode = currentnode
            currentnode  = node
        return self

    def remove_2(self,value):
        #Another approach
            currentnode=self
            pararntnode= None
            #finding the node
            while (currentnode != None):
                node = currentnode
                if value < currentnode.value:
                    currentnode = currentnode.left
                elif value > currentnode.value:
                    currentnode = currentnode.right
                elif value == currentnode.value:
                    break
                pararntnode = node
            # if not found return
            if currentnode is None:
                return self
            else:
                marknode = currentnode      #store the node
            if currentnode.right is not None:
                pararntnode = currentnode
                currentnode = currentnode.right
                while(currentnode.left is not None):
                    pararntnode = currentnode
                    currentnode = currentnode.left
            
                if currentnode.right is None:
                    marknode.value = currentnode.value
                    if currentnode == pararntnode.left :pararntnode.left = None
                    else : pararntnode.right = None
                else:
                    marknode.value = currentnode.right.value
                    currentnode.right = None
            else:
                if(currentnode == self): 
                    self = self.left
                    return self
                if currentnode == pararntnode.left:
                    pararntnode.left = currentnode.left
                else:
                    pararntnode.right = currentnode.left
            
            return self
            
       
def preorder(node):
    if node  is None:
        return None
    else: print(node.value,end= " ")
    preorder(node.left)
    preorder(node.right)
def inorder(node,arr):
    if node  is not None:

        inorder(node.left,arr)
        arr.append(node.value)
        inorder(node.right,arr)
    return arr

def postorder(node,arr):
    if node  is not None:

        postorder(node.left,arr)
        postorder(node.right,arr)
        arr.append(node.value)
    return arr
    
# def dfs(x):
#     print()
#     preorder(x)

if __name__ == "__main__":
        a = BST(12)
        res=[]
        for i in [5,15,2,6,13,22,1,14]:
            a.insert(i)
        d = inorder(a,res)
        print(d)
        a.remove(12)
        # dfs(a)
        a.remove(1)
        # dfs(a)
        a.insert(12)
        # dfs(a)