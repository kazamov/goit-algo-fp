class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self, message: str):
        current = self.head

        print(message)
        while current:
            print(current.data)
            current = current.next


def reverse_linked_list(list: LinkedList):
    prev = None
    current = list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    list.head = prev


def merge_sort_linked_list(list: LinkedList):
    new_list = LinkedList()
    new_list.head = merge_sort(list.head)
    return new_list


def merge_sort(head):
    if not head or not head.next:
        return head

    # Find the middle of the linked list
    middle = find_middle(head)

    # Split the linked list into two halves
    left = head
    right = middle.next
    middle.next = None

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    sorted_list = merge(left, right)

    return sorted_list


def find_middle(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(left, right):
    dummy = Node()
    current = dummy

    while left and right:
        if left.data < right.data:
            current.next = Node(left.data)
            left = left.next
        else:
            current.next = Node(right.data)
            right = right.next

        current = current.next

    # Attach the remaining nodes of both lists
    if left:
        current.next = left
    if right:
        current.next = right

    return dummy.next


def merge_linked_lists(list1: LinkedList, list2: LinkedList):
    new_list = LinkedList()
    new_list.head = merge(list1.head, list2.head)
    return merge_sort_linked_list(new_list)


if __name__ == "__main__":
    llist = LinkedList()

    llist.insert_at_beginning(12)
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    llist.print_list("\nInitial list:")

    reverse_linked_list(llist)
    llist.print_list("\nReversed list:")

    sorted_list = merge_sort_linked_list(llist)
    sorted_list.print_list("\nSorted list:")

    another_list = LinkedList()
    another_list.insert_at_beginning(4)
    another_list.insert_at_beginning(8)
    another_list.insert_at_beginning(13)

    merged_list = merge_linked_lists(sorted_list, another_list)
    merged_list.print_list("\nMerged list:")
