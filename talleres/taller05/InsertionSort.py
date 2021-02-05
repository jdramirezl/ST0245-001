from GraphTimesT5 import Graph

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortList(head: ListNode) -> ListNode:
    if head == None:
        return None
    node = ListNode(head.val)
    head = head.next
    while head != None:
        if head.val <= node.val:
            temp = ListNode(head.val)
            temp.next = node
            node = temp
        else:
            cur = node
            while (cur.next != None) and (cur.next.val < head.val):
                cur = cur.next
            temp = cur.next
            cur.next = ListNode(head.val, temp)
        head = head.next
    while(node):
        print(str(node.val), end=' ')
        node = node.next
    print()


def generateList(i):
    prev = None
    for j in range(i):
        prev = ListNode(j, prev)
    return prev


if __name__ == '__main__':
    inputs = [(x, generateList(x)) for x in range(1, 1001, 25)]
    Graph(insertionSortList, inputs, "Insertion Sort")
