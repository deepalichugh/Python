class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(head.data, "-> ", end="")
        head = head.next

    return head

def lengthOfLL(head):
    count = 0
    while head is not None:
        count = count + 1
        head = head.next

    return count


def insertAtI(head, pos, data):
    if pos < 0 or pos >lengthOfLL(head):
        return head
    
    prev = None
    curr = head
    newNode = Node(data)
    count = 0

    while count < pos:
        prev = curr
        curr = curr.next
        count = count + 1
    
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr

    return head


def takeInput():
    ll = [int(ele) for ele in input().split()]

    head = None
    tail = None

    for ele in ll:
        if ele == -1:
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
    
head = takeInput()
printLL(head)
print()
head = insertAtI(head, 9, 10)
printLL(head)