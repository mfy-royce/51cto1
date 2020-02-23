#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: lclink.py
@time:  18:44
@welcom to learn ai
"""





def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

def removeNthFromEnd(head,n):
    p =  head
    for i in range(n):
        p= p.next
    nthP =  head.next
    while p.next != None:
        p = p.next
        nthP = nthP.next

    deleteNode(nthP)
    return head

def reverseLink(head):
    f =  head

    currentP = f.next
    if currentP ==None:
        return head

    nextP = currentP.next
    if nextP == None:   #  只有一个节点情况
        return head

    while currentP != head:
        currentP.next = f
        f = currentP
        currentP =  nextP
        nextP = nextP.next
        if nextP == None:
            nextP = head

    currentP.next = f
    nextP.next = None

    return head

def mergeTwoLink(head1,head2):
    p1 = head1.next
    p2 =  head2.next
    if p1 == None:
        return head2
    if p2 == None:
        return head1
    if p1.val > p2.val:
        end =p2
        head = head2
        p2 = p2.next
    else:
        end =  p1
        head = head1
        p1 = p1.next

    while p1 !=None or  p2 != None:
        while p1 != None and p2 != None:
            if p1.val > p2.val :
                end.next = p2
                end = p2
                p2 = p2.next
            else:
                end.next = p1
                end = p1
                p1 = p1.next

        while p1 !=None:
            end.next = p1
            end = p1
            p1 = p1.next

        while p2 != None:
            end.next = p2
            end = p2
            p2 = p2.next
    return  head

def isPalindrome(head):
    p = head.next
    iList = []
    while p != None:
        iList.append(p.val)
        p= p.next

    if iList == iList[::-1]:
        return True
    else:
        return False

def hasCycle(head):
    fast = head.next
    slow  = head
    cFlag = False
    while fast != slow:
        fast = fast.next
        slow = slow.next
        if fast == None:
            return False
        fast = fast.next
        if fast == None:
            return False
    return True


def main():
    from pythonds.test import randomList,showLink,creatLink,creatCycleLink,showCyscleLink
    # iList = randomList(2)
    # print (iList)
    iList = [1,2,2,1]
    # head = creatLink(iList)
    # showLink(head)
    head,position,end  =  creatCycleLink(iList)
    showCyscleLink(head,position,end)

    # iList = randomList(4)
    # iList=sorted(iList)
    # head1 = creatLink(iList)
    # showLink(head1)
    # iList = randomList(4)
    # iList=sorted(iList)
    # head2 = creatLink(iList)
    # showLink(head2)

    # deleteNode(head.next)
    # showLink(head)

    #head = removeNthFromEnd(head,2)
    #showLink(head)

    # head = reverseLink(head)
    # showLink(head)

    # head = mergeTwoLink(head1,head2)
    # showLink(head)

    #print("isPalindrome is {}".format(isPalindrome(head)))

    print("hasCycle is {}".format(hasCycle(head)))
if __name__ == "__main__":
    main()