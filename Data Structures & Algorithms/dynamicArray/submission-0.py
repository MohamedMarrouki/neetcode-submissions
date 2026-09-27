class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.arr=[0]*capacity

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i]=n


    def pushback(self, n: int) -> None:
        if (self.size==self.capacity):
            self.resize()
            self.arr[self.size]=n
            self.size=self.size+1
        else:
            self.arr[self.size]=n
            self.size=self.size+1


    def popback(self) -> int:
        i=self.arr[self.size-1]
        self.arr[self.size-1]=0
        self.size -=1
        return i
 

    def resize(self) -> None:
        self.capacity=self.capacity*2
        new_a=[0]*self.capacity
        for i in range(self.size):
            new_a[i]=self.arr[i]

        self.arr=new_a



    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
