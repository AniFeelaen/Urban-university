class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if not step:
            raise StepValueError("Шаг не может быть равен 0")

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        if self.step > 0 and self.pointer >= self.stop:
            return False
        elif self.step < 0 and self.pointer <= self.stop:
            return False
        else:
            return True

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')


iter2 = Iterator(-5, 1)

iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)