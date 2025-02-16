class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None
    

class SingleLinkedList():
    def __init__ (self):
        self.head = None
        self.length = 0
        
    def insert_at_start(self, data) -> int:
        first_node = Node(data)
        first_node.next = self.head
        self.head = first_node
        self.length += 1
        return 0
    
    def insert_at_end(self, data) -> int:
        new_node = Node(data)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        self.length += 1
        return self.length - 1
    
    def insert_at_index(self, data, index) -> int:
        inserted_node_index = -1
        if index == 0:
            self.insert_at_start(data)
            inserted_node_index = 0
        else:  
            new_node = Node(data)
            counter = 0
            current_node = self.head
            while (counter + 1 < index) and (current_node != None):
                counter += 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
                inserted_node_index = index
        if inserted_node_index:
            self.length += 1
        return inserted_node_index

    def get_length(self) -> int:
        temp_node = self.head
        node_counter = 0
        while temp_node:
            temp_node = temp_node.next
            node_counter += 1
        self.length = node_counter
        return node_counter

    def remove_at_start(self) -> int:
        if self.length:
            self.head = self.head.next
            self.length -= 1
        return 0

    def remove_at_index(self, index) -> int:
        removed_node_index = -1
        if index == 0:
            removed_node_index = self.remove_at_start()
        elif index < self.length:
            temp_node = self.head
            node_counter = 0
            while node_counter + 1 < index:
                temp_node = temp_node.next
                node_counter += 1
            nn = temp_node.next
            temp_node.next = nn.next
            self.length -= 1
            removed_node_index = index
        return removed_node_index

    def update_at_index(self, data, index) -> int:
        updated_node_index = -1
        if index < self.length:
            temp_node = self.head
            node_counter = 0
            while node_counter != index:
                temp_node = temp_node.next
                node_counter += 1
            temp_node.data = data
            updated_node_index = node_counter
        return updated_node_index

    def print_all(self):
        temp_node = self.head
        node_counter = 0
        while temp_node:
            print(f"{temp_node.data} ({node_counter})", end=' -> ')
            temp_node = temp_node.next
            node_counter += 1
        print('None')
        return node_counter


if __name__ == "__main__":
    SLL = SingleLinkedList()
    SLL.insert_at_start("Two")
    SLL.insert_at_start("one")
    SLL.insert_at_end("three")
    SLL.insert_at_index("zero", 0)
    SLL.insert_at_index("garbage", LL.get_length())
    SLL.print_all() # zero (0) -> one (1) -> Two (2) -> three (3) -> garbage (4) -> None 
    SLL.remove_at_index(4)
    SLL.update_at_index("two", 2)
    SLL.print_all() # zero (0) -> one (1) -> two (2) -> three (3) -> None