class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(head.data, "->", end = "")
        head = head.next
    return

def takingInput():
    ll = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for ele in ll:
        if ele ==-1:
            break
        else:
            newNode = Node(ele)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head

printLL(takingInput())
