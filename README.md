# Rational Numbers in Python

A simple Python implementation of **Rational numbers (fractions)** with support for arithmetic operations like **addition** and **subtraction** using Python’s **dunder methods** (`__add__`, `__sub__`, etc.).  
Fractions are automatically simplified using the **Euclidean Algorithm** (GCD) and (LCM).

---

## ✨ Features
- Create rational numbers with integers (numerator/denominator).
- Automatic simplification of fractions.
- Support for:
  - `+` (addition via `__add__`)
  - `-` (subtraction via `__sub__`)
  - Pretty string representation (`__str__`).
- Error handling for division by zero.
- LCM and GCD features for rational numbers.

---

## 📂 Project Structure
```
Rational_Number/
│── app.py              # Instantiation and functions testing.
│── main.py             # App called in main for execution.
│── Rational_class.py   # Rational class implementation.
──README.md             # Project documentation.
```

---

## 🚀 Usage

### Example: Add & Subtract Rational Numbers
```python
from Rational_class import Rational

r1 = Rational(1, 2)   # 1/2
r2 = Rational(3, 4)   # 3/4

print(r1 + r2)   # 5/4
print(r1 - r2)   # -1/4
print(f"The Greatest Common Divisor of {r1.num}/{r1.deno} is:",r1.GCD(1,2))  # 1
print(f"The Least Common Multiple of {r2.num}/{r2.deno} is:",r2.LCM(3,4))  # 12
```

Output:
```
5/4
-1/4
The Greatest Common Mivisor of 1/2 is: 1
The Greatest Common Mivisor of 3/4 is: 12
```

---

## ⚙️ How It Works
- Fractions are simplified using **Greatest Common Divisor (GCD)**:  
  ```python
  while deno != 0:
      num, deno = deno, num % deno
  ```
- Ensures numerator & denominator remain integers (using `//` instead of `/`).

---

## 📝 License
This project is made by Behroz Musharraf, an open-source and free to use project for educational purposes.
