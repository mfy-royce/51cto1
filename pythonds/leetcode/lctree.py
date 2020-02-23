#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: lctree.py
@time:  15:16
@welcom to learn ai
"""

def maxDeep(root):
    if root ==None:
        return 0
    return 1 + max(maxDeep(root.left),maxDeep(root.right))

def validBST(root,min,max):
    if root == None:
        return True
    if min != None and root.val <min:
        return False
    if max != None and root.val >max:
        return False
    return validBST(root.left,min,root.val) and validBST(root.right,root.val,max)

def isSymmetric(root):
    if root == None:
        return True
    return symmetricTree(root.left,root.right)

def symmetricTree(left,right):
    if left ==None and right == None:
        return True
    if left ==None and right !=None:
        return False
    if left != None and right == None:
        return False
    if left.val != right.val:
        return False
    return symmetricTree(left.right,right.left) and symmetricTree(left.left,right.right)

def traversalByLevel(root):
    if root==None:
        return []
    lastLevel = [root]
    result = [[root.val]]
    while len(lastLevel):
        nextLevelValue=[]
        temp =[]
        for node in lastLevel:
            if node.left != None:
                temp.append(node.left)
                nextLevelValue.append(node.left.val)
            if node.right != None:
                temp.append(node.right)
                nextLevelValue.append(node.right.val)
        lastLevel = temp.copy()
        if len(nextLevelValue):
            result.append(nextLevelValue)
    return result

from pythonds.test import BinaryTreeNode
def creatBBST(iList):
    if len(iList)== 0:
        return None
    rootIndex = len(iList)//2
    leftTree = creatBBST(iList[:rootIndex])
    rightTree = creatBBST(iList[rootIndex+1:])
    root = BinaryTreeNode(iList[rootIndex],leftTree,rightTree)
    return root

if __name__=="__main__":
    from pythonds.test import creatBinaryTree,showBinaryTreeByLevel
    import sys
    # root = creatBinaryTree([9, 3, 20, 1, None, 8, 21])
    # showBinaryTreeByLevel(root)
    # print("maxDeep is {}".format(maxDeep(root)))
    #
    # print("validBST is {}".format(validBST(root, None, None )))

    # root = creatBinaryTree([9, None, None])
    # showBinaryTreeByLevel(root)
    # print("isSymmetric is {}".format(isSymmetric(root)))

    #print("traversalByLevel is {}".format(traversalByLevel(root)))

    root = creatBinaryTree([9, 3, 20, 1, None, 8, 21])
    showBinaryTreeByLevel(root)
    showBinaryTreeByLevel(creatBBST([1,2,3,4,5,6]))