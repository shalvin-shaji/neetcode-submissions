class DynamicArray:
    
    def __init__(self, capacity: int):
        self.__current_index = 0
        self.__capacity = capacity
        self.__arr = [0] * capacity


    def get(self, i: int) -> int:
        if i < self.__current_index:
            return self.__arr[i]
        return 0


    def set(self, i: int, n: int) -> None:
        if i < self.__current_index:
            self.__arr[i] = n



    def pushback(self, n: int) -> None:
        if self.__current_index ==  self.__capacity:
            self.resize()
        self.__arr[self.__current_index] = n
        self.__current_index += 1


    def popback(self) -> int:
        temp = self.__arr[self.__current_index-1]
        self.__arr[self.__current_index-1] = 0
        self.__current_index -= 1
        return temp

 

    def resize(self) -> None:
        temp = [0] * self.__capacity * 2
        for i, element in enumerate(self.__arr):
            temp[i] = element
        self.__arr = temp
        self.__capacity *= 2


    def getSize(self) -> int:
        return self.__current_index
        
    
    def getCapacity(self) -> int:
        return self.__capacity
