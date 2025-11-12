import oop_solution.library_oop as O

def test_basic_flow():
    lib = O.Library()
    lib.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    lib.add_book(2, "Clean Code", "Robert Martin", 2)
    lib.add_member(101, "Alice Smith", "alice@email.com")

    assert len(lib.books) == 2
    assert len(lib.members) == 1

    assert lib.borrow_book(101, 1) is True
    assert lib.find_book(1).available_copies == 2

    assert lib.return_book(101, 1) is True
    assert lib.find_book(1).available_copies == 3