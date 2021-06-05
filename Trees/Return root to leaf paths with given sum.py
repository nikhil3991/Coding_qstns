
class Node:
    # constructor to create tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printPaths(root):

    path = []

    printPathsRec(root, path, 0)





def printPathsRec(root, path, pathLen):

    if root is None:
        return


    if (len(path) > pathLen):
        path[pathLen] = root.data
    else:
        path.append(root.data)


    pathLen = pathLen + 1

    if root.left is None and root.right is None:

        # leaf node then print the list
        # printArray(path, pathLen)



        print(path)






    else:
        # try for left and right subtree
        printPathsRec(root.left, path, pathLen)
        printPathsRec(root.right, path, pathLen)



    # Helper function to print list in which


# root-to-leaf path is stored
def printArray(ints, len):
    for i in ints[0: len]:
        print(i, " ", end="")
    print()


# Driver program to test above function
""" 
Constructed binary tree is 
			10 
		/ \ 
		8	 2 
	/ \ / 
	3 5 2 
"""
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

printPaths(root)




# This code has been contributed by Shweta Singh.
