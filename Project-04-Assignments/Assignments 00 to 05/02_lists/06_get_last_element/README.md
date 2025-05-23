# **📌 Get Last Element - Python List Handling 🚀**  

This script retrieves and prints the **last element** from a user-inputted list. It demonstrates **basic list operations, user input handling, and function structuring** in Python.  

---

## 📌 **Project Overview**  
The program prompts the user to enter elements into a list **one by one**.  
- The user can stop entering values by pressing **Enter (empty input)**.  
- The program then prints the **last element** of the list.  

---

## 🛠️ **How It Works**  

1️⃣ **User Input Function (`get_lst`)**  
- Repeatedly **asks the user for list elements**.  
- If the user presses **Enter without input**, the list entry stops.  

2️⃣ **Retrieve Last Element (`get_last_element`)**  
- Prints the **last element** of the list.  

3️⃣ **Main Function (`main`)**  
- Calls `get_lst()` to get the list from the user.  
- Calls `get_last_element()` to **display the last element**.  

---

## 📜 **Code Explanation**  

### **🔹 `get_lst()`** - Get List from User  
This function prompts the user to enter elements **one at a time** until they press Enter.  
```python
def get_lst():
    lst = []  # Initialize an empty list
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Keep adding elements until Enter is pressed
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst  # Return the final list
```

### **🔹 `get_last_element(lst)`** - Print Last Element  
This function receives a list and **prints its last element**.  
```python
def get_last_element(lst):
    print(lst[-1])  # Print the last element
```

### **🔹 `main()`** - Program Execution  
The `main` function **calls both functions** to execute the program logic.  
```python
def main():
    lst = get_lst()  # Get the list from user input
    get_last_element(lst)  # Print the last element
```

---

## 🏗️ **Project Structure**  

📂 **Project Directory:**  
```
Project-4-Assignments/Assignments 00 to 05/02_lists/06_get_last_element/
│── main.py  # Main script for retrieving the last element of a list
```

📄 **File Breakdown:**  
- **`main.py`** → Contains the complete Python script for handling user input and retrieving the last list element.  

---

## ▶️ **How to Run the Project**  

### 🔧 **Prerequisites**  
Ensure you have **Python installed** on your system.  

### 🏃 **Run the Application**  
```sh
python main.py
```
This will prompt the user to enter a list and return the **last element**.  

---

## 🎯 **Expected Output**  

**Example Run:**  
```
Please enter an element of the list or press enter to stop: apple
Please enter an element of the list or press enter to stop: banana
Please enter an element of the list or press enter to stop: cherry
Please enter an element of the list or press enter to stop: 
cherry  # (Last element of the list)
```

---

## 🛠️ **Customization Options**  

| **Modification** | **How to Implement** |
|-----------------|----------------------|
| Ensure list isn't empty | Add a check before printing the last element |
| Convert input to integers | Use `int(input())` inside `get_lst()` |
| Print all elements | Modify `get_last_element()` to loop through the list |

**Example of checking an empty list before printing the last element:**  
```python
def get_last_element(lst):
    if lst:  # Check if the list is not empty
        print(lst[-1])
    else:
        print("The list is empty!")
```

---

## 🎯 **Learning Outcomes**  
This project is a great way to learn:  
✅ **User input handling in Python** 🖥️  
✅ **Basic list operations** 📋  
✅ **Function structuring and modular programming** 🚀  

---

## 📜 **Future Enhancements**  
🚀 Handle cases where users enter empty lists.  
🚀 Allow **numbers or mixed data types** instead of only strings.  
🚀 Add an **option to retrieve any index, not just the last element**.  

---

## 🎯 **Final Thoughts**  
This **Get Last Element App** is a beginner-friendly **Python project** that demonstrates **list handling, user input, and function structuring**. 🐍💡  

🔗 **Perfect for beginners exploring Python programming!** 🚀  

---
