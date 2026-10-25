"""Insertion sort in monotonically decreasing (non-increasing) order."""


def insertion_sort_descending(values):
    """Sort a list in place from largest to smallest and return that list."""
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1

        # The prefix before i is already sorted. Shift smaller values right
        # until we find the correct position for key in descending order.
        while j >= 0 and values[j] < key:
            values[j + 1] = values[j]
            j -= 1

        values[j + 1] = key

    return values


def main():
    while True:
        user_input = input("Enter integers separated by spaces: ")
        try:
            numbers = [int(value) for value in user_input.split()]
        except ValueError:
            print("Invalid input. Enter whole numbers only, such as: 5 -2 4 6")
            continue
        if not numbers:
            print("Please enter at least one integer.")
            continue
        break

    print("Original array:", numbers)
    insertion_sort_descending(numbers)
    print("Descending order:", numbers)


if __name__ == "__main__":
    main()
