# 💎 Diamond Pattern Generator in Python

This is a simple Python program that prints a **diamond pattern** made of asterisks (`*`) using loops and string multiplication. It's great for learning nested loops and basic string operations in Python.

---

## 🧠 What It Does

- Takes a fixed height (can be changed)
- Prints a centered diamond shape using `*`
- Uses `for` loops and string repetition (`*` operator)

---

---

## 🧾 Code Overview

```python
def diamond_pattern():
    num = 5  # Change this value to increase/decrease the size of the diamond

    # Upper half of the diamond
    for i in range(1, num + 1):
        print(" " * (num - i) + "*" * (2 * i - 1))

    # Lower half of the diamond
    for i in range(num - 1, 0, -1):
        print(" " * (num - i) + "*" * (2 * i - 1))

# Run the function
diamond_pattern()


🚀 How to Run
Clone the repo or copy the code

Make sure Python is installed

Save the code in a .py file, for example: diamond.py

Run the script:

bash
Copy
Edit
python diamond.py



📂 Project Structure
Copy
Edit
Diamond_Pattern/
├── diamond.py
└── README.md
💡 Tips
You can make the diamond taller or shorter by changing num

Try using input() to let users set the size dynamically

📄 License
This project is open-source and free to use under the MIT License.

Created with 💻 by Zara Khan
