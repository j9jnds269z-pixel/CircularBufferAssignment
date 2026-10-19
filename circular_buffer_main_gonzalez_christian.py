

# Program Description: Tests the CircularBuffer class and its operations.
# Author: Your Name
# Date: October 19, 2026

"""
Test circular buffer class to perform data operations.
"""

# Import the CircularBuffer class.
from circular_buffer import CircularBuffer


def main():
    """Main function to test the functionality of circular buffer."""

    capacity = int(input("Enter Buffer Capacity: "))
    cb = CircularBuffer(capacity)

    # 1. Delete operation
    print("1. Delete operation:")
    item = cb.delete()

    if item is None:
        print("Buffer is empty")
    else:
        print(f"{item} has been deleted")

    # 2. Add 15
    print("2. Add 15:")
    cb.add(15)
    print(f"Buffer: {cb}")

    # 3. Add 5
    print("3. Add 5:")
    cb.add(5)
    print(f"Buffer: {cb}")

    # 4. Delete operation
    print("4. Delete operation:")
    item = cb.delete()
    if item is not None:
        print(f"{item} has been deleted")
    print(f"Buffer: {cb}")

    # 5. Add 3
    print("5. Add 3:")
    cb.add(3)
    print(f"Buffer: {cb}")

    # 6. Add 26
    print("6. Add 26:")
    cb.add(26)
    print(f"Buffer: {cb}")

    # 7. Delete operation
    print("7. Delete operation:")
    item = cb.delete()
    if item is not None:
        print(f"{item} has been deleted")
    print(f"Buffer: {cb}")

    # 8. Add 76
    print("8. Add 76:")
    cb.add(76)
    print(f"Buffer: {cb}")

    # 9. Add 105
    print("9. Add 105:")
    cb.add(105)
    print(f"Buffer: {cb}")

    # 10. Search for 48
    print("10. Search 48:")
    if cb.find(48):
        print("48 is in the buffer")
    else:
        print("48 is not in the buffer")

    # 11. Display first and last items
    print("11. Display items at first and last")
    if not cb.is_empty():
        print(
            f"{cb.peek_first()} is the first item, "
            f"and {cb.peek_last()} is the last item"
        )
    else:
        print("Buffer is empty")

    # 12. Calculate the sum
    print("12. Add all items:")
    print(f"Sum = {add_all(cb)}")

    # 13. Find the largest and smallest items
    print("13. Locate the largest/smallest item")

    if not cb.is_empty():
        max_index = get_max_index(cb)
        min_index = get_min_index(cb)
        buffer = cb.get_buffer()

        print(
            f"The largest item = {buffer[max_index]} "
            f"and the smallest item = {buffer[min_index]}"
        )
    else:
        print("Buffer is empty")

    # 14. Clear the buffer
    print("14. Clear the buffer")
    cb.clear()
    print(f"{cb}.")


def add_all(cb):
    """Add all items in the circular buffer and return their sum."""
    total = 0

    for i in range(cb.get_size()):
        index = (cb.get_head() + i) % cb.get_capacity()
        total += cb.get_buffer()[index]

    return total


def get_max_index(cb):
    """Return the buffer index containing the largest item."""
    if cb.is_empty():
        return -1

    max_index = cb.get_head()

    for i in range(cb.get_size()):
        index = (cb.get_head() + i) % cb.get_capacity()

        if cb.get_buffer()[index] > cb.get_buffer()[max_index]:
            max_index = index

    return max_index


def get_min_index(cb):
    """Return the buffer index containing the smallest item."""
    if cb.is_empty():
        return -1

    min_index = cb.get_head()

    for i in range(cb.get_size()):
        index = (cb.get_head() + i) % cb.get_capacity()

        if cb.get_buffer()[index] < cb.get_buffer()[min_index]:
            min_index = index

    return min_index


if __name__ == '__main__':
    main()


