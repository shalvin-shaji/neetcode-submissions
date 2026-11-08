class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    def link(self, node):
        self.next_node = node

class LinkedList:
    
    def __init__(self):
        self.__head = None
        self.__length = 0

    
    def get(self, index: int) -> int:
        if index < self.__length:
            next_node = self.__head
            while index > 0:
                next_node = next_node.next_node
                index -= 1
            return next_node.value
        return -1

        

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next_node = self.__head
        self.__head = node
        self.__length += 1
        

    def insertTail(self, val: int) -> None:
        node = Node(val)
        last_node = self.__head
        while last_node is not None and last_node.next_node != None:
            last_node = last_node.next_node
        if last_node is None:
            self.insertHead(val)
        else:
            last_node.next_node = node
            self.__length += 1
        

    def remove(self, index: int) -> bool:
        if index < self.__length:
            prev_node = None
            current_node = self.__head
            while index > 0:
                index -= 1
                prev_node = current_node
                current_node = current_node.next_node
            if prev_node == None:
                self.__head = self.__head.next_node
            else:
                prev_node.next_node = current_node.next_node
            self.__length -= 1
            return True
        return False
            
            
            
        

    def getValues(self) -> List[int]:
        values = []
        current_node = self.__head
        while current_node is not None:
            values.append(current_node.value)
            current_node = current_node.next_node
        return values
        
