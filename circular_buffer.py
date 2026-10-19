
# Program Description: Implements a circular buffer using a Python list.
# Author: Christian Gonzalez
# Date: October 19, 2026


class CircularBuffer:
    """A fixed-size circular buffer that operates as a FIFO queue."""

    def __init__(self, capacity):
        """Initialize the circular buffer."""
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.__capacity = capacity
        self.__size = 0
        self.__buffer = [None] * capacity
        self.__head = 0
        self.__tail = 0

    def get_capacity(self):
        """Return the capacity."""
        return self.__capacity

    def set_capacity(self, capacity):
        """Set a new capacity while preserving existing items."""
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        items = []
        for i in range(self.__size):
            items.append(
                self.__buffer[(self.__head + i) % self.__capacity]
            )

        items = items[-capacity:]
        self.__capacity = capacity
        self.__buffer = [None] * capacity
        self.__size = len(items)
        self.__head = 0

        for i, item in enumerate(items):
            self.__buffer[i] = item

        self.__tail = self.__size % capacity

    def get_size(self):
        """Return the number of items in the buffer."""
        return self.__size

    def get_buffer(self):
        """Return the underlying list."""
        return self.__buffer

    def get_head(self):
        """Return the head index."""
        return self.__head

    def get_tail(self):
        """Return the tail index."""
        return self.__tail

    def add(self, item):
        """Add an item, overwriting the oldest item if full."""
        self.__buffer[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__capacity

        if self.__size == self.__capacity:
            # The oldest item was overwritten.
            self.__head = (self.__head + 1) % self.__capacity
        else:
            self.__size += 1

    def delete(self):
        """Remove and return the oldest item."""
        if self.is_empty():
            return None

        item = self.__buffer[self.__head]
        self.__buffer[self.__head] = None
        self.__head = (self.__head + 1) % self.__capacity
        self.__size -= 1

        if self.__size == 0:
            self.__head = 0
            self.__tail = 0

        return item

    def clear(self):
        """Clear the buffer and reset its pointers."""
        self.__buffer = [None] * self.__capacity
        self.__size = 0
        self.__head = 0
        self.__tail = 0

    def is_empty(self):
        """Return True if the buffer is empty."""
        return self.__size == 0

    def peek_first(self):
        """Return the first item without removing it."""
        if self.is_empty():
            return None
        return self.__buffer[self.__head]

    def peek_last(self):
        """Return the last item without removing it."""
        if self.is_empty():
            return None

        last_index = (self.__tail - 1) % self.__capacity
        return self.__buffer[last_index]

    def find(self, item):
        """Return True if the item exists in the buffer."""
        for i in range(self.__size):
            index = (self.__head + i) % self.__capacity
            if self.__buffer[index] == item:
                return True
        return False

    def __str__(self):
        """Display items from the head to the tail."""
        if self.is_empty():
            return "Buffer is empty"

        items = []
        for i in range(self.__size):
            index = (self.__head + i) % self.__capacity
            items.append(str(self.__buffer[index]))

        return " --> ".join(items)
