from __future__ import annotations

# ======================
# Problem 1 (DLL)
# ======================


class TrainCarNode:
    car_id: str
    prev: TrainCarNode | None
    next: TrainCarNode | None

    def __init__(self, car_id: str) -> None:
        self.car_id = car_id
        self.prev = None
        self.next = None


class MidnightMailDLL:
    head: TrainCarNode | None
    tail: TrainCarNode | None

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append_car(self, car_id: str) -> None:
        new_node = TrainCarNode(car_id)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def detach_last_car(self) -> str | None:
        if self.tail is None:
            return None

        removed_id = self.tail.car_id

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return removed_id

        previous_tail = self.tail.prev
        if previous_tail is None:
            self.head = None
            self.tail = None
            return removed_id

        self.tail = previous_tail
        self.tail.next = None
        return removed_id

    def to_reverse_list(self) -> list[str]:
        reversed_ids: list[str] = []
        current = self.tail

        while current is not None:
            reversed_ids.append(current.car_id)
            current = current.prev

        return reversed_ids


# ======================
# Problem 2
# ======================


def is_valid_ticket_code(code: str) -> bool:
    if not code.startswith("MM-"):
        return False

    digits = code[3:]
    return len(digits) == 4 and digits.isdigit()


# ======================
# Problem 3 (Recursion)
# ======================


def count_priority_labels(labels: list[str], target: str) -> int:
    def _count_at(index: int) -> int:
        if index >= len(labels):
            return 0

        return (1 if labels[index] == target else 0) + _count_at(index + 1)

    return _count_at(0)


# ======================
# Problem 4 (Recursion)
# ======================


def clean_radio_message(message: str) -> str:
    cleaned_chars: list[str] = []

    def _collect_chars(index: int) -> None:
        if index >= len(message):
            return

        char = message[index]
        if char != " ":
            cleaned_chars.append(char)

        _collect_chars(index + 1)

    _collect_chars(0)
    return "".join(cleaned_chars)


def count_priority_labels_iterative(labels: list[str], target: str) -> int:
    return sum(1 for label in labels if label == target)


def clean_radio_message_iterative(message: str) -> str:
    return message.replace(" ", "")
