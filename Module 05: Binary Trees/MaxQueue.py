from SLLQueue import SLLQueue
from DLList import DLList
from Interfaces import Queue

class MaxQueue(Queue):
    def __init__(self):
        self.sll = SLLQueue()
        self.dll = DLList()
        # self.n is stored in sll

    # note: Book object has dunder methods that overrides < and >
    def add(self, x: object) -> None:
        self.sll.add(x) # Add to the SLLQueue

        while self.dll.size() > 0 and self.dll.dummy.prev.x < x:
            self.dll.remove(self.dll.size() - 1)
        self.dll.append(x)

    def remove(self) -> [int, object]:
        if self.sll.size() == 0:
            raise IndexError()
        removed_element = self.sll.remove()

        if removed_element == self.dll.dummy.next.x:
            self.dll.remove(0)
        return removed_element

    def size(self) -> int:
        return self.sll.n

    def max(self, ) -> object:
        if self.sll.size() == 0:
            raise IndexError()
        return self.dll.dummy.next.x

    def __str__(self):
        return str(self.sll)