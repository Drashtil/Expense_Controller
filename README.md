# 💰 Expense Controller

A simple **command-line based Expense Management System** built using **Python**.

This project helps users manage their daily expenses, store expense records permanently, calculate total spending, and analyze spending patterns using categories.

---

## 🚀 Features

✅ Add new expenses
✅ Store expenses permanently using file handling
✅ View all recorded expenses
✅ Calculate total spending
✅ Generate category-wise expense summary
✅ Simple and user-friendly CLI interface

---

## 🛠️ Technologies Used

* **Python 3**
* File Handling
* Lists
* Dictionaries
* Functions
* Exception Handling

---

## 📂 Project Structure

```
Expense_Controller/
│
├── 1.cli(expense controller)main.py
├── expenses.text
└── README.md
```

---

## 💾 Data Storage

Expenses are stored permanently in:

```
expenses.text
```

The data is stored in the following format:

```
amount:category
```

Example:

```
500:Food
200:Travel
300:Shopping
```

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project folder

```bash
cd Expense_Controller
```

### 3. Run the Python file

```bash
python "1.cli(expense controller)main.py"
```

---

## 📌 Application Menu

When the program starts, users get the following options:

```
1. Add Expense
2. View Expense
3. Total Spending
4. Category Summary
5. Exit
```

---

## ✨ Functionalities Explained

### ➕ Add Expense

Users can enter:

* Expense amount
* Expense category

Example:

```
Enter your amount: 500
Enter your category: Food
```

The expense is saved automatically.

---

### 👀 View Expenses

Displays all saved expenses.

Example:

```
500:Food
200:Travel
300:Shopping
```

---

### 💰 Total Spending

Calculates the total amount spent from all saved expenses.

Example:

```
Your total spending = 1000
```

---

### 📊 Category Summary

Groups expenses according to categories.

Example:

```
{
 'Food': 500,
 'Travel': 200,
 'Shopping': 300
}
```

---

## 🎯 Future Improvements

* Add date-wise expense tracking
* Add monthly expense reports
* Create GUI version using Tkinter
* Export expenses to CSV/Excel
* Add expense search functionality
* Add user authentication

---

## 📚 Learning Outcomes

Through this project, I learned and practiced:

* Python file handling
* Working with lists and dictionaries
* Creating reusable functions
* Managing data storage
* Building a real-world CLI application

---

## 👨‍💻 Author

**Drashtil**

Python Developer | Learning Software Development & Automation

---

⭐ If you find this project useful, consider giving it a star!
