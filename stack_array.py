from dataclasses import dataclass
from typing import Any

"""Implements an efficient last-in first-out Abstract Data Type using a Python List"""


@dataclass
class Stack:
    capacity: int  # capacity of stack

    def __post_init__(self) -> None:
        self.items = [None] * self.capacity  # array for stack
        self.num_items = 0  # number of items in stack

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance"""
        return self.num_items == 0

    def is_full(self) -> bool:
        """Returns True if the stack is full, and False otherwise
           MUST have O(1) performance"""
        return self.num_items == self.capacity

    def push(self, item: Any) -> Any:
        """If stack is not full, pushes item on stack.
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance"""
        if self.num_items < self.capacity:
            self.items[self.num_items] = item
            self.num_items += 1
        else:
            raise IndexError

    def pop(self) -> Any:
        """If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance"""
        if self.num_items >= 1:
            self.num_items -= 1
            return self.items[self.num_items]
        else:
            raise IndexError

    def peek(self) -> Any:
        """If stack is not empty, returns next item to be popped (but does not remove the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance"""
        if self.num_items == 0:
            raise IndexError
        else:
            return self.items[self.num_items - 1]

    def size(self) -> int:
        """Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance"""
        return self.num_items
