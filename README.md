## Summary
This assignment builds a system for managing train cars, validating ticket codes, and processing messages using recursion and linked lists.

## Approach

Problem 1:
Used a doubly linked list to manage train cars and support reverse traversal from the tail.

Problem 2:
Validated ticket codes by checking the `"MM-"` prefix and ensuring the remainder is exactly 4 digits.

Problem 3:
Used recursion with an index-based helper to count how many times a target label appears.

Problem 4:
Used recursion with an index-based helper to remove spaces and return a cleaned message.

## Complexity

Problem 1: append/detach `O(1)`; reverse traversal `O(n)`. Space `O(n)`.
Problem 2: Time `O(n)`, Space `O(1)`.
Problem 3: Time `O(n)`, Space `O(n)` (call stack).
Problem 4: Time `O(n)`, Space `O(n)` (call stack + output).

## Edge-case checklist

- [x] empty train
- [x] one train car
- [x] several train cars
- [x] invalid ticket code (wrong prefix / wrong digits / wrong length)
- [x] empty label list
- [x] empty message
- [x] one-character or all-space message

## Assistance & Sources

AI used? Yes (for ideas only; not copied verbatim).

What it helped with:
Helped with problem decomposition, recursion structure, and debugging.

Other sources used:
Class notes and examples.
## Optional Stretch — Iterative vs Recursive

- `count_priority_labels` and `clean_radio_message` use recursion to meet the assignment requirement.
- `count_priority_labels_iterative` and `clean_radio_message_iterative` use iteration and Python idioms.
- The recursive versions are clearer for demonstrating call stack use.
- The iterative versions avoid extra call stack space and are more efficient in Python.
