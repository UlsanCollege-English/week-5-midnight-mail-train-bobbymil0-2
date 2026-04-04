from src.challenges import (
    MidnightMailDLL,
    count_priority_labels,
    clean_radio_message,
    is_valid_ticket_code
)

# ======================
# Problem 2 Tests
# ======================

def test_ticket_valid():
    assert is_valid_ticket_code("MM-1234") == True

def test_ticket_invalid():
    assert is_valid_ticket_code("XX-1234") == False

def test_ticket_short():
    assert is_valid_ticket_code("MM-12") == False

def test_ticket_empty():
    assert is_valid_ticket_code("") == False


# ======================
# Problem 1 Tests
# ======================

def test_dll_append_and_reverse():
    train = MidnightMailDLL()
    train.append_car("A")
    train.append_car("B")
    train.append_car("C")

    assert train.to_reverse_list() == ["C", "B", "A"]

def test_dll_detach():
    train = MidnightMailDLL()
    train.append_car("A")
    train.append_car("B")

    assert train.detach_last_car() == "B"
    assert train.detach_last_car() == "A"
    assert train.detach_last_car() is None


# ======================
# Problem 3 Tests
# ======================

def test_count_priority():
    assert count_priority_labels(
        ["PRIORITY", "NORMAL", "PRIORITY"], "PRIORITY"
    ) == 2

def test_count_empty():
    assert count_priority_labels([], "PRIORITY") == 0


# ======================
# Problem 4 Tests
# ======================

def test_clean_message():
    assert clean_radio_message("go now") == "gonow"

def test_clean_spaces():
    assert clean_radio_message(" a b ") == "ab"

def test_clean_empty():
    assert clean_radio_message("") == ""