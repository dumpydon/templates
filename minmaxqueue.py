class MinMaxQueue:
    def __init__(self) -> None:
        self._q: Deque[T] = deque()
        self._minq: Deque[T] = deque()  # increasing
        self._maxq: Deque[T] = deque()  # decreasing

    def __len__(self) -> int:
        return len(self._q)

    def add(self, x: T) -> None:
        self._q.append(x)

        while self._minq and self._minq[-1] > x:
            self._minq.pop()
        self._minq.append(x)

        while self._maxq and self._maxq[-1] < x:
            self._maxq.pop()
        self._maxq.append(x)

    def pop(self) -> T:
        if not self._q:
            raise IndexError("pop from empty queue")

        x = self._q.popleft()

        if self._minq and self._minq[0] == x:
            self._minq.popleft()
        if self._maxq and self._maxq[0] == x:
            self._maxq.popleft()

        return x

    def min(self) -> T:
        if not self._q:
            raise IndexError("min from empty queue")
        return self._minq[0]

    def max(self) -> T:
        if not self._q:
            raise IndexError("max from empty queue")
        return self._maxq[0]
