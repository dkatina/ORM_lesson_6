# Lesson 6: In-Class Assignments

Complete these assignments during the live lesson. Each assignment builds on the concepts covered in the lesson.

---

## Assignment 1: Simple Many-to-Many Relationship

**Goal:** Create a many-to-many relationship between Students and Clubs

### Tasks:
1. **Create an association table** for students and clubs
   - Use `Table()` with `student_id` and `club_id` as ForeignKeys

2. **Create Student model** with:
   - `id` (Integer, primary key)
   - `name` (String)
   - `email` (String)
   - `clubs` (relationship to clubs)

3. **Create Club model** with:
   - `id` (Integer, primary key)
   - `name` (String)
   - `description` (String)
   - `students` (relationship to students)



---

## Assignment 2: Association Model with Additional Data

**Goal:** Create a many-to-many relationship between Books and Readers with extra information

### Tasks:
1. **Create BookReader association model** with:
   - `book_id` (ForeignKey to books)
   - `reader_id` (ForeignKey to readers)
   - `rating` (Float)
   - `review_date` (DateTime)

2. **Create Book model** with:
   - `id` (Integer, primary key)
   - `title` (String)
   - `author` (String)
   - `readers` (relationship to readers)

3. **Create Reader model** with:
   - `id` (Integer, primary key)
   - `name` (String)
   - `email` (String)
   - `books` (relationship to books)



---

## Assignment 3: CRUD Operations

**Goal:** Practice basic CRUD operations on a simple User model

### Tasks:
1. **Create User model** with:
   - `id` (Integer, primary key)
   - `name` (String)
   - `email` (String)
   - `age` (Integer)

2. **CRUD Operations:**
   - **CREATE:** Add 3 users
   - **READ:** Query users older than 25
   - **UPDATE:** Update one user's email
   - **DELETE:** Delete one user

---

## Quick Reference

### Common SQLAlchemy Imports:
```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Table, Float
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
```

### Basic Setup Pattern:
```python
engine = create_engine('sqlite:///database.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```

### Common Relationship Types:
- **One-to-Many:** `relationship("ModelName", back_populates="attribute")`
- **Many-to-Many:** `relationship("ModelName", secondary=association_table, back_populates="attribute")`
- **Association Model:** `relationship("ModelName", back_populates="attribute")`

---

## Tips:
- Use `echo=True` during development to see SQL queries
- Always call `session.commit()` after making changes
- Use `session.add()` to add new objects
- Use `session.query(Model).filter(condition).all()` for queries
- Use `session.delete(object)` to delete objects 