import procedural_version.library_procedural as L

def test_basic_flow():
    L.books[:] = []
    L.members[:] = []
    L.borrowed_books[:] = []

    L.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    L.add_book(2, "Clean Code", "Robert Martin", 2)

    L.add_member(101, "Alice Smith", "alice@email.com")
    assert len(L.books) == 2
    assert len(L.members) == 1

    assert L.borrow_book(101, 1) is True
    assert L.find_book(1)["available_copies"] == 2

    assert L.return_book(101, 1) is True
    assert L.find_book(1)["available_copies"] == 3
