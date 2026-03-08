class Node:
    """
    Singly linked list node.
    Stores a value and a reference to the next element.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    Queue implemented using a singly linked list.
    Addition happens at the end (enqueue), removal from the beginning (dequeue).
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        """
        Adds a new element to the queue.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        """
        Removes and returns an element from the front of the queue.
        If the queue is empty, returns None.
        """
        if self.head is None:
            return None

        value = self.head.value
        # If head becomes None, we should also update tail to None 
        # for an empty queue state.
        if self.head == self.tail:
             self.tail = None
        
        self.head = self.head.next
        return value

    def show(self):
        """
        Prints all elements currently in the queue.
        """
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next


queue = Queue()
queue.enqueue("Запит 1: авторизація")
queue.enqueue("Запит 2: завантаження файлів")
queue.enqueue("Запит 3: зміна пароля")
queue.enqueue("Запит 4: видалення акаунта")

print("Поточна черга:")
queue.show()

print("Обробка запитів:")

while True:
    req = queue.dequeue()
    if req is None:
        break
    print("Оброблено:", req)