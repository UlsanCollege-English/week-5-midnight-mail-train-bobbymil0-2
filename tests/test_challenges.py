from src.challenges import (
    MidnightMailDLL,
    clean_radio_message,
    clean_radio_message_iterative,
    count_priority_labels,
    count_priority_labels_iterative,
    is_valid_ticket_code,
)


# ======================
# Problem 2 Tests
# ======================


def test_ticket_valid() -> None:
    assert is_valid_ticket_code("MM-1234") is True


def test_ticket_invalid_prefix() -> None:
    assert is_valid_ticket_code("XX-1234") is False


def test_ticket_invalid_short() -> None:
    assert is_valid_ticket_code("MM-12") is False


def test_ticket_edge_empty() -> None:
    assert is_valid_ticket_code("") is False


def test_ticket_invalid_non_digits() -> None:
    assert is_valid_ticket_code("MM-12A4") is False


# ======================
# Problem 1 Tests
# ======================


def test_dll_append_and_reverse() -> None:
    train = MidnightMailDLL()
    train.append_car("A")
    train.append_car("B")
    train.append_car("C")

    assert train.to_reverse_list() == ["C", "B", "A"]


def test_dll_detach_to_empty() -> None:
    train = MidnightMailDLL()
    train.append_car("A")
    train.append_car("B")

    assert train.detach_last_car() == "B"
    assert train.detach_last_car() == "A"
    assert train.detach_last_car() is None


def test_dll_empty_reverse_and_detach() -> None:
    train = MidnightMailDLL()
    assert train.to_reverse_list() == []
    assert train.detach_last_car() is None


def test_dll_append_after_detach_keeps_list_consistent() -> None:
    train = MidnightMailDLL()
    train.append_car("A")
    train.append_car("B")
    assert train.detach_last_car() == "B"
    train.append_car("C")

    assert train.to_reverse_list() == ["C", "A"]
    assert train.detach_last_car() == "C"
    assert train.detach_last_car() == "A"
    assert train.detach_last_car() is None


# ======================
# Problem 3 Tests
# ======================


def test_count_priority() -> None:
    assert count_priority_labels(["PRIORITY", "NORMAL", "PRIORITY"], "PRIORITY") == 2


def test_count_empty() -> None:
    assert count_priority_labels([], "PRIORITY") == 0


# ======================
# Problem 4 Tests
# ======================


def test_clean_message() -> None:
    assert clean_radio_message("go now") == "gonow"


def test_clean_spaces() -> None:
    assert clean_radio_message(" a b ") == "ab"


def test_clean_empty() -> None:
    assert clean_radio_message("") == ""


def test_clean_all_spaces() -> None:
    assert clean_radio_message("     ") == ""


def test_count_priority_iterative() -> None:
    assert count_priority_labels_iterative(["PRIORITY", "NORMAL", "PRIORITY"], "PRIORITY") == 2


def test_clean_message_iterative() -> None:
    assert clean_radio_message_iterative("go now") == "gonow"


def test_ticket_invalid_extra_characters_after_digits() -> None:
    assert is_valid_ticket_code("MM-1234X") is False


def test_count_priority_all_match() -> None:
    assert count_priority_labels(["PRIORITY", "PRIORITY"], "PRIORITY") == 2
