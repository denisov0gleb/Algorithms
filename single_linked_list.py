class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None
    

class SingleLinkedList():
    def __init__ (self):
        self.head = None
        
    def insert_at_start(self, data):
        first_node = Node(data)
        first_node.next = self.head
        self.head = first_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    
    def insert_at_index(self, data, index):
        function_result = None
        new_node = Node(data)
        counter = 0
        current_node = self.head
        if index == 0:
            self.insert_at_start(data)
            function_result = 0
        else:        
            while (counter + 1 < index) and (current_node != None):
                counter += 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
                fuction_result = index
            else:
                function_result = -1
            
        return function_result
        
        
    def print_all(self):
        temp_node = self.head
        counter = 0
        while temp_node:
            print(f"{temp_node.data} ({counter})", end=' -> ')
            temp_node = temp_node.next
            counter += 1
        print('None')


if __name__ == "__main__":
    LL = SingleLinkedList()
    LL.insert_at_start("two")
    LL.insert_at_start("one")
    LL.insert_at_end("three")
    LL.insert_at_index("zero", 0)
    
    LL.print_all() # zero (0) -> one (1) -> two (2) -> three(3) -> None