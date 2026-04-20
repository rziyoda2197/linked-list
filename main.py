class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get(self, index):
        if index >= self.length():
            print("Index out of range")
            return None

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def erase(self, index):
        if index >= self.length():
            print("Index out of range")
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next

# Test
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)

print("Linked list:")
linked_list.print_list()

print("Length:", linked_list.length())

print("Get 2:", linked_list.get(2))

linked_list.erase(2)

print("Linked list after erase 2:")
linked_list.print_list()

print("Search 3:", linked_list.search(3))

linked_list.delete(3)

print("Linked list after delete 3:")
linked_list.print_list()
