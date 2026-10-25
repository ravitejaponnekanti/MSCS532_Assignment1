# MSCS532 Assignment 1

Python implementation of insertion sort in monotonically decreasing
(non-increasing) order: each value is greater than or equal to the next.

## Requirements

Python 3.8 or higher. No third-party packages are required.

## Run

```powershell
python --version
python insertion_sort.py
python -m unittest -v
```

Example output:

```text
Original array: [5, 2, 4, 6, 1, 3, 2]
Descending order: [6, 5, 4, 3, 2, 2, 1]
```

## How it works

The first element is a sorted prefix. Starting at the second element, store
the current value as `key`, shift smaller prefix elements one position to
the right, then insert `key` into the resulting gap. After each iteration,
the prefix is sorted in descending order. Once the loop finishes, the whole
list is sorted.

The comparison `values[j] < key` puts larger elements first. Equal elements
are not shifted past each other, so the sort is stable. The function changes
the original list and returns that same list. It uses no built-in sorting;
the tests use `sorted` only as an independent reference result.

Best-case time is O(n) for an already descending list. Average and worst-case
time are O(n^2). Auxiliary space is O(1).

Tests cover empty and single-element lists, duplicates, negative values,
ascending and descending inputs, and 100 reproducible random lists.

## VS Code setup

Install Microsoft's Python extension (`ms-python.python`). Open this folder,
run **Python: Select Interpreter** from the Command Palette, and select a
Python 3.8+ interpreter or the local `.venv` interpreter when available.
Then use **Run Python File in Terminal** on `insertion_sort.py`.

If using the local environment directly in PowerShell:

```powershell
.\.venv\Scripts\python.exe insertion_sort.py
.\.venv\Scripts\python.exe -m unittest -v
```

## Git history

The repository has separate commits for initialization, implementation, and
tests/documentation. View them with `git log --oneline`.

## Reference

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022).
*Introduction to Algorithms* (4th ed.), Chapter 2. This implementation
adapts insertion sort to descending order.
