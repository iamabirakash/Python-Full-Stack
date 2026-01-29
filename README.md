# 🐍 Python Programming Language – Master Notes
## Acces to All Class Notes :- [Notion Notes](https://www.notion.so/Python-Full-Stack-2f1f394b3ec080d8b0ebd5739f82ac42?source=copy_link)
## To add as a Contributor :- [Drop a DM](https://abirakash.netlify.app/)
# Python OOP Concepts – README

This repository demonstrates **core Object-Oriented Programming (OOP) concepts in Python** using clean, beginner-friendly examples. It also covers **exception handling** and **abstract base classes**.

---

## 📌 Concepts Covered

### 1️⃣ Inheritance (Reusability)
Inheritance allows a child class to **reuse properties and methods** of a parent class.

**Example:**
- `Car` inherits from `Vehicle`
- Reuses `model` and `color`

```python
class Vehicle:
    def __init__(self, model, color):
        self.model = model
        self.color = color
```

---

### 2️⃣ Polymorphism (Same Method, Different Behavior)
Polymorphism means **same method name but different behavior** based on the object.

**Runtime Polymorphism:**
- Achieved using **method overriding** and `super()`

```python
class Car(Vehicle):
    def display(self):
        super().display()
        print("Seats:", self.seats)
```

✔ Same `display()` method behaves differently in `Vehicle` and `Car`

---

### 3️⃣ Constructor Overloading
Python does not support constructor overloading directly, but it is **simulated using inheritance**.

- Parent constructor initializes common data
- Child constructor adds extra parameters

```python
super().__init__(model, color)
```

---

### 4️⃣ Method Overriding
When a child class provides its **own implementation** of a parent class method.

```python
def display(self):
    super().display()
```

---

### 5️⃣ Encapsulation (Data Security)
Encapsulation binds data and methods together and **restricts direct access**.

#### 🔐 Access Modifiers
| Modifier | Syntax | Access |
|--------|-------|-------|
| Public | `name` | Anywhere |
| Protected | `_name` | Within class & subclasses |
| Private | `__name` | Only inside class |

---

### 6️⃣ Getter & Setter Methods
Used to **access and update private variables safely**.

```python
def getId(self):
    return self.__id

def setId(self, value):
    self.__id = value
```

---

### 7️⃣ Property Decorators (Recommended)
A cleaner and more Pythonic way to implement getters and setters.

```python
@property
def marks(self):
    return self.__marks

@marks.setter
def marks(self, value):
    self.__marks = value
```

✔ Easier to read
✔ Less boilerplate code

---

### 8️⃣ Abstraction (Hiding Implementation)
Abstraction shows **essential details only** and hides implementation logic.

#### Abstract Class
- Acts as a base class
- Can contain abstract and non-abstract methods

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def greet(self):
        pass
```

---

### 9️⃣ Abstract Methods
- Declared using `@abstractmethod`
- Must be implemented in child classes

```python
class Technical(Employee):
    def greet(self):
        print("Hi, I am from IT department")
```

---

### 🔟 Exception Handling
Used to **maintain program flow** and handle runtime errors gracefully.

#### Custom Exceptions

```python
class AgeNotValid(Exception):
    pass
```

#### Raising Exceptions

```python
if age < 18:
    raise AgeNotValid("Age should not be below 18")
```

#### Handling Exceptions

```python
try:
    obj = Person(17)
except AgeNotValid as e:
    print(e)
```

---

### ✅ Custom Validation Examples
- `AgeNotValid` → validates age
- `MarksNotValid` → ensures marks are between 0 and 100

---

## 🧠 Summary

✔ Inheritance → Code reuse
✔ Polymorphism → Same method, different behavior
✔ Encapsulation → Data protection
✔ Abstraction → Hide unnecessary details
✔ Property Decorators → Clean getters/setters
✔ Exception Handling → Safe & controlled execution

---

## 🚀 Best Practices Highlighted
- Use `super()` for parent access
- Prefer property decorators over manual getters/setters
- Use abstract classes to enforce rules
- Create custom exceptions for validation

---

📘 This README acts as a **complete revision note for Python OOP concepts**, ideal for exams, interviews, and quick recall.



# 🔰 Installing Django
```python -m venv foldername```

```pip install django```

```django-admin startproject project```

```pyhton manage.py runserver```
