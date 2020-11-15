from src.metier.Collection import Collection
from src.domain.Node import Node
import math


class LinkedList(Collection):

    __currentNode: Node
    __index: int
    __n : int
    def __str__(self):
        pass

    def add(self, element, index: int = None) -> None:
        if self.is_empty(self):
            self.currentNode = Node(None, element,None)
            self.__index = index
        else:
            while index > self.index + 1 and self.currentNode.get_prev(self.currentNode) != None:
                self.currentNode = self.currentNode.get_prev(self.currentNode)
                self.index -= 1

            while index < self.index - 1 and self.currentNode.get_prev(self.currentNode) != None:
                self.currentNode = self.currentNode.get_next(self.currentNode)
                self.index += 1

            tmp: Node = self.currentNode
            self.currentNode = Node(tmp.get_prev(tmp), element, tmp)
            tmp.set_prev(tmp,self.currentNode)
            tmp = self.currentNode
            self.currentNode = self.currentNode.get_prev(self.currentNode)
            self.currentNode.set_next(self.currentNode, tmp)




    def get(self, index: int):
        self.get_length()
        self.get_first(self)

        if self.n - 1 < index :
            raise
        else:
            while self.index != index:
                self.currentNode = self.currentNode.get_next(self.currentNode)
                self.index += 1

            return self.currentNode.get_value(self.currentNode)


    def set(self, element, index: int) -> None:
        while self.index > index and self.currentNode.get_prev(self.currentNode) != None:
            self.currentNode = self.currentNode.get_prev(self.currentNode)
            self.index -= 1

        while self.index < index and self.currentNode.get_prev(self.currentNode) != None:
            self.currentNode = self.currentNode.get_next(self.currentNode)
            self.index += 1

        if self.index == index:
            self.currentNode.set_value(self.currentNode, element)

    def contains(self, element) -> bool:
        while self.currentNode.get_prev(self.currentNode) != None:
            self.currentNode = self.currentNode.get_prev(self.currentNode)

        while self.currentNode.get_value(self.currentNode) != element and self.currentNode.get_next(self.currentNode) != None :
            self.currentNode = self.currentNode.get_next(self.currentNode)

        return self.currentNode.get_value(self.currentNode) == element

    def remove(self, element=None, index: int = None) -> None:
        while self.index > index and self.currentNode.get_next(self.currentNode) != None:
            self.currentNode = self.currentNode.get_prev()
            self.index -= 1

        while self.index < index and self.currentNode.get_prev(self.currentNode) != None:
            self.currentNode = self.currentNode.get_next(self.currentNode)
            self.index += 1




    def clear(self) -> None:
        self.getFirst()
        tmp : Node = self.currentNode.get_next(self.currentNode)
        self.currentNode.set_next(self.currentNode, None)
        self.currentNode = tmp

        while self.currentNode.get_next(self.currentNode) != None:
            tmp = self.currentNode.get_next(self.currentNode)
            self.currentNode.set_next(self.currentNode, None)
            self.currentNode.set_prev(self.currentNode, None)
            self.currentNode = tmp

        self.currentNode.set_prev(self.currentNode, None)
        self.currentNode = None

    def size(self) -> int:
        while self.currentNode.get_prev(self.currentNode) != None:
            self.currentNode = self.currentNode.get_prev(self.currentNode)
            self.index -= 1

        while self.currentNode.get_next(self.currentNode) != None :
            self.currentNode = self.currentNode.get_next(self.currentNode)
            self.index += 1

        return self.index + 1


    def is_empty(self) -> bool:
        return self.currentNode == None

    def index_of(self, element) -> int:
        while self.currentNode.get_prev(self.currentNode) != None:
            self.currentNode = self.currentNode.get_prev()

        self.index = 0
        while self.currentNode.get_value(self.currentNode) != element and self.currentNode.get_prev(self.currentNode) != None:
            self.currentNode = self.currentNode.get_next(self.currentNode)
            self.index += 1

        if self.currentNode.get_value(self.currentNode) == element:
            return self.index
        else:
            return -1

    def insertion_sort(self):
        self.get_first(self)
        self.currentNode = self.currentNode.get_next(self.currentNode)
        self.index = 1
        val : int
        j: int = 0

        while self.index < self.n:
            val = self.currentNode.get_value(self.currentNode)
            j = self.index - 1
            while j > 0 and self.get(self,j) > val:
                tmp : Node = self.currentNode
                self.currentNode = self.currentNode.get_next(self.currentNode)
                self.currentNode = tmp
                j -= 1
                self.currentNode.set_value(self.currentNode, val)

            self.index += 1

    def merge_sort(self):
        self.get_first(self)
        p: int = self.index
        r: int = self.n
        q: int = (p + r) / 2

        n1: int = q - p + 1
        n2: int = r - q

        L: list = [None] * (n1 + 1)
        R: list = [None] * (n2 + 1)

        while self.index < q + 1:
            L[self.index] = self.get(self, self.index)
            self.index += 1

        while self.index < r + 1:
            R[self.index] = self.get(self, self.index)
            self.index += 1

        L[n1] = R[n2] = math.inf
        i: int = 0
        j: int = 0
        for k in range(p, r + 1):
            15
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
        else:
            self.currentNode.set(self,R[j], k)
            j += 1

    def dichotomic_search(self, element) -> int:
        self.get_length(self)
        self.get_first(self)
        p: int = self.index
        q: int = self.n / 2
        r: int = self.n

        while p <= r:
            q = (p+r)/2
            if self.get(self,q) == element:
                return q
            elif self.get(self,q) > element :
                r = q - 1
            else:
                p = q + 1

    def get_first(self):
        while self.currentNode.get_prev(self.currentNode) != None:
            self.currentNode = self.currentNode.get_prev(self.currentNode)

        self.index = 0

    def get_length(self):
        self.get_first()
        if self.is_empty():
            return 0

        while self.currentNode.get_next(self.currentNode) != None:
            self.currentNode = self.currentNode.get_next(self.currentNode)
            self.index += 1

        self.n = self.index + 1
