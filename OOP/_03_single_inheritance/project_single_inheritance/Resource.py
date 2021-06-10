from abc import ABC


class Resource(ABC):
    def __init__(self, name, manufacturer, total, allocated):

        if not isinstance(total, int) or total <= 0:
            raise ValueError("Total must be not negative integer.")
        if not isinstance(allocated, int) or allocated < 0 or allocated > total:
            raise ValueError('Allocated must be a positive integer not greater than total.')
        self._total = total
        self._allocated = allocated
        self.name = name
        self.manufacturer = manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Resource {self.name} {self.manufacturer}: {self.total} total."

    def claim(self, n):
        if self.remaining() >= n > 0:
            self._allocated += n
        else:
            raise ValueError(f"Cannot claim {n} of {self}")  # str or repr?

    def freeup(self, n):
        if self.allocated >= n > 0:
            self._allocated -= n
        else:
            raise ValueError(f"Cannot free up {n} of {self}")

    def died(self, n):
        if 0 < n <= self.allocated:
            self._total -= n
            self._allocated -= n
        elif 0 < n <= self.total:
            self._allocated = 0
            self._total -= n
        else:
            raise ValueError(f'Cannot remove {n} of {self}')

    def purchased(self, n):
        if n > 0:
            self._total += n
        else:
            raise ValueError(f"Cannot add {n} of {self}.")

    def category(self):
        return self.__class__.__name__.lower() #TODO

    def remaining(self):
        return self.total-self.allocated
