class MyQueue:

    def __init__(self):
        """
        in负责push,out负责pop
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()


    def peek(self) -> int:
        ans = self.pop()#复用pop函数
        self.stack_out.append(ans)#弹出后再装回去
        return ans

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)