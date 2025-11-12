# Lib Management System - OOP

## Project Overview
This is a simple Library Management System built for the programming class.
At first, it was written using a procedural style, I refactored it into an **object-oriented version** using Python classes.
The goal of this project is to show how object-oriented programming (OOP) can make the code easier to manage and understand
The program can add books and members, borrow and return books, and display which books are available or borrowed

## Project Structure
│
├── README.md
│
├── procedural_version/
│ ├── library_procedural.py 
│ └── test_procedural.py 
│
├── oop_solution/
│ ├── library_oop.py 
│ └── library_oop_Lib.py 
│ └── library_oop_Book.py 
│ └── library_oop_Member.py 
│ └── test_oop.py 

## Design Overview
### Book Class
- **Attributes:**
  - `id` – Book ID  
  - `title` – Book title  
  - `author` – Author name  
  - `total_copies` – Total copies of the book  
  - `available_copies` – How many copies can still be borrowed
### Member Class
- **Attributes:**
  - `id` – Member ID  
  - `name` – Member’s name  
  - `email` – Member’s email address  
  - `borrowed_books` – List of book IDs that the member has borrowed
### Library Class
- **Attributes:**
  - `books` – A list of all the Book objects  
  - `members` – A list of all the Member objects  
  - `borrowed_books` – Records of who borrowed what

- **Main Methods:**
  - `add_book()` – Adds a new book to the library  
  - `add_member()` – Adds a new member  
  - `borrow_book()` – Lets a member borrow a book (if available)  
  - `return_book()` – Handles book returns  
  - `display_available_books()` – Shows all books that still have copies left  
  - `display_member_books()` – Shows what books a member has borrowed

## Testing
### What’s Tested
All testing was done in the `test_oop.py` file. It checks both normal cases and error cases.

#### Basic Operations
- Adding books and members  
- Borrowing and returning books  
- Showing available books and member borrow lists  

#### Edge Cases
- Trying to borrow a book when there are no copies left  
- Trying to borrow more than 3 books  
- Returning a book that wasn’t borrowed  
- Using an invalid member ID or book ID
  
## How to run
### Using Git bash
cd to the local file/folder that my assign are in mine are:
cd "/c/Users/narak/OneDrive/Desktop/library_management_oop"

after that, I just using the command py
- python procedural_version/library_procedural.py
- python oop_solution/library_oop.py
