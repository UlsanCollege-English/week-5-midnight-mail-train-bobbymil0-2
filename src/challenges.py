# ======================
# Problem 1 (DLL)
# ======================

class TrainCarNode:
    def __init__(self, car_id: str):
        self.car_id = car_id
        self.prev = None
        self.next = None


class MidnightMailDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_car(self, car_id: str) -> None:
        new_node = TrainCarNode(car_id)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def detach_last_car(self) -> str | None:
        if not self.tail:
            return None

        removed = self.tail.car_id

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return removed

    def to_reverse_list(self) -> list[str]:
        result = []
        current = self.tail

        while current:
            result.append(current.car_id)
            current = current.prev

        return result


# ======================
# Problem 2
# ======================

def is_valid_ticket_code(code: str) -> bool:
    if not code.startswith("MM-"):
        return False

    digits = code[3:]

    if len(digits) != 4:
        return False

    return digits.isdigit()


# ======================
# Problem 3 (Recursion)
# ======================

def count_priority_labels(labels: list[str], target: str) -> int:
    if not labels:
        return 0

    if labels[0] == target:
        return 1 + count_priority_labels(labels[1:], target)
    else:
        return count_priority_labels(labels[1:], target)


# ======================
# Problem 4 (Recursion)
# ======================

def clean_radio_message(message: str) -> str:
    if message == "":
        return ""

    if message[0] == " ":
        return clean_radio_message(message[1:])
    else:
        return message[0] + clean_radio_message(message[1:])