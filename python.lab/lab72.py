class Node:
    """
    Вузол однозв'язного списку.
    Зберігає значення та посилання на наступний елемент.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    Черга, побудована на основі однозв'язного списку.
    Додавання відбувається в кінець, видалення з початку.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        """
        Додає новий елемент у чергу.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        """
        Забирає елемент з початку черги.
        Якщо черга порожня, повертає None.
        """
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next
        return value

    def show(self):
        """
        Виводить усі елементи, що зараз знаходяться у черзі.
        """
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

if __name__ == "__main__":
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
