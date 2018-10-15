class Node(object):
    data = None
    next = None

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def addNext(self, data):
        self.next = Node(data)


class LinkedList(object):
    head = None

    def __init__(self, data):
        self.head = Node(data)

    def addNode(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            ref = self.head
            while(ref.next is not None):
                ref = ref.next
            ref.addNext(data)


    def __str__(self):
        if self.head is None:
            return ''
        else:
            ref = self.head
            s = ''
            while(ref):
                s += str(ref.data) + ' -> '
                ref = ref.next
            return s


def reverseNodes(linked_list):
    if (linked_list.head is None):
        return 'Empty LinkedList'
    else:
        head = linked_list.head
        empty_node = Node(None)
        while head.next:
            next = head.next
            head.next = empty_node
            empty_node = head
            head = next
        linked_list.head = empty_node
        return linked_list

def reverse(head):
    new_head = Node(None)
    while head:
        # head.next, head, new_head = new_head, head.next, head 
        head.next = new_head
        head = head.next
        new_head = head
    return new_head
 


def solution2(head):
    curr = head
    prev = Node(None)
    next = Node(None)
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


if __name__ == '__main__':
    linkedList = LinkedList('A')
    linkedList.addNode('B')
    linkedList.addNode('C')
    linkedList.addNode('D')
    linkedList.addNode('E')

    print(linkedList)

    # reversed_list = reverseNodes(linkedList)
    reversed_list = reverse(linkedList.head)

    while(reversed_list.next):
        print(reversed_list.data)
        reversed_list = reversed_list.next

    # print(reversed_list)