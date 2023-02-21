class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(str(head.data), " -> ", end = "")
        head = head.next
    return 


def takeInput():
    inp = [int(ele) for ele in input().split()]
    head = None

    for ele in inp:
        newNode = Node(ele)

        if ele == -1:
            break
        if head is None:
            head = newNode
        else:
            currNode = head
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = newNode
    return head

printLL(takeInput())
