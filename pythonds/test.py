#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: test.py
@time:  16:43
@welcom to learn ai
"""
import random

def randomList(n):
    iList = []
    for i in range(n):
        iList.append(random.randrange(0,100))
    return iList

def sortVerify(times,length,sortFunc):
    # iList = randomList(length)
    # sortedList = sortFunc(iList,0,len(iList)-1)

    equl =True
    for i in range(times):
        iList = randomList(length)
        refiList = sorted(iList)
        sortedList = sortFunc(iList, 0, len(iList) - 1)


        print("iList is      {},id is {}".format(iList,id(iList)))
        print("refiList is   {},id is {}".format(refiList, id(refiList)))
        print("sortedList is {},id is {}".format(sortedList,id(sortedList)))

        if refiList != sortedList:
            equl=False
            print("{}th is {}".format(i, equl))
            break
    if equl :
        print("verify is ok")






def doubleListRemoveOne(iList):
    num  = random.choice(iList)
    cList = iList.copy()
    doubleList = iList * 2
    doubleList.remove(num)
    return  doubleList

def randomZero(iList,n):
    for i in range(n):
        p = random.randint(0,len(iList))
        iList.insert(p,0)

def randomMatrix(n):
    Matrix = []
    for i in range(n):
        Matrix.append(randomList(n))
    return Matrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def printLink(head):
    p = head
    while p != None :
        if p != head:
            print("name {},index {},count {}".format(p[4], p[0], p[1]))
        p =p[3]

def showLink(head):
    p=head.next
    while p != None:
        if p.next != None:
            print("{}-->".format(p.val),end=" ")
        else:
            print("{}".format(p.val))
        p= p.next

class ListNode:
    def __init__(self,x,next = None):
        self.val = x
        self.next = next

def creatLink(iList):
    head = ListNode(None)
    end = head
    for i in iList:
        end.next = ListNode(i)
        end = end.next
    return head

def creatCycleLink(iList):
    position = random.choice(range(-1,len(iList)))
    if position == -1 :
        head = creatLink(iList)
        return head,position,None
    head = ListNode(None)
    end = head
    for i,num in enumerate(iList):
        end.next = ListNode(num)
        end = end.next
        if i == position:
            crossNode = end
    end.next = crossNode
    return head,position,end

def showCyscleLink(head,position ,end):
    if position ==-1:
        showLink(head)
        return
    p = head.next
    while True:
        if p != end:
            print("{}-->".format(p.val), end=" ")
        else:
            print("{}".format(p.val))
            break
        p = p.next
    print("end connect {},position is {}".format(p.next.val,position))


class BinaryTreeNode():
    def __init__(self,val,left = None,right = None):
        self.val= val
        self.left =left
        self.right = right

def creatBinaryTree(iList,root=0):
    if root >=len(iList):
        return  None
    if iList[root] == None:
        return None
    leftRoot = creatBinaryTree(iList,root*2+1)
    rightRoot = creatBinaryTree(iList, root * 2 + 2)

    root  = BinaryTreeNode(iList[root],leftRoot,rightRoot)
    return root

def showBinaryTree(root,count):
    if root ==None:
        return count-1
    print("node {} is {}".format(count,root.val))
    count = showBinaryTree(root.left,count+1)
    count = showBinaryTree(root.right,count+1)
    return count

def showBinaryTreeByLevel(root):
    treeLevel = [[root]]
    nextLevel = True
    while nextLevel:
        nextLevel= False
        level = []
        for i in treeLevel[-1]:
            if i != None:
                level.append(i.left)
                level.append(i.right)
            else:
                level.append(None)
                level.append(None)
                continue

            if i.left != None or i.right != None:
                nextLevel = True
        treeLevel.append(level)
 #   tree = []
#    nodeNum =
    for i,level in enumerate(treeLevel):
        print("level {} is ".format(i),end="")
        for node in level:
            if node !=None:
                print("{} ".format(node.val),end="")
            else:
                print("{} ".format(node), end="")
        print("")




if __name__ == "__main__":
    iList = randomList(5)
    print(iList)
    randomZero(iList,5)
    print(iList)
    printMatrix(randomMatrix(3))
    root = creatBinaryTree([3,9,20,None,None,15,7])
    showBinaryTree(root,0)
    root = creatBinaryTree([3,9,20,15,None,15,7])
    showBinaryTree(root,0)
    showBinaryTreeByLevel(root)