# 🏦 Bank Management System

## 📌 Project Overview

The Bank Management System is a Python-based console application developed using Object-Oriented Programming (OOP) and MongoDB. The system allows users to register, log in, manage bank accounts, perform transactions, and maintain transaction records.

The project demonstrates core banking functionalities such as account creation, balance enquiry, cash deposits, withdrawals, and fund transfers while storing customer and transaction data in MongoDB using PyMongo.

---

## 🎯 Features

### 👤 User Authentication

* User Registration (Sign Up)
* User Login (Sign In)
* Username Availability Validation
* Password Verification
* Unique Account Number Generation

### 👥 Customer Management

* Customer Registration
* Customer Profile Storage
* Customer Information Management

### 💳 Account Management

* Automatic  Unique Account Number Generation
* Account Status Management
* Balance Tracking
* Account Information Storage

### 💰 Transaction Management

* Cash Deposit
* Cash Withdrawal
* Fund Transfer
* Transaction History Recording
* Timestamp-Based Transaction Logging

### 🏦 Banking Services

* Balance Enquiry
* Deposit Funds
* Withdraw Funds
* Transfer Funds Between Accounts

---

## 🛠️ Technology Stack

### Programming Language

* Python 3.x

### Database

* MongoDB

### Database Driver

* PyMongo

### Concepts Used

* Object-Oriented Programming (OOP)
* CRUD Operations
* Exception Handling
* Modular Programming
* MongoDB Collections
* Banking Workflow Logic

### Tools

* MongoDB Compass
* Git
* GitHub
* Visual Studio Code

---

## 📂 Project Structure

```bash
Bank-Management-System/
│
├── main.py
├── register.py
├── customer.py
├── bank.py
├── database.py
└── README.md
```

---

## 🗄️ Database Design

### Database Name

```text
bank
```

### Collection: customers

Stores customer account information.

```json
{
  "username": "hrushi",
  "password": "1234",
  "name": "Hrushikesh",
  "age": "22",
  "city": "Pune",
  "balance": 0,
  "account_number": 12345678,
  "status": 1
}
```

### Collection: transactions

Stores transaction records.

```json
{
  "timedate": "2026-06-05 10:30:00",
  "username": "hrushi",
  "account_number": 12345678,
  "remarks": "Amount Deposit",
  "amount": 5000
}
```

---

## 🔗 Database Relationships

```text
Customers (1)
      │
      │
      ▼
Transactions (M)

One Customer
      │
      ├── Deposit Transactions
      ├── Withdrawal Transactions
      └── Fund Transfer Transactions
```

---

## 🔄 Project Workflow

### User Registration

```text
Create Username
        ↓
Validate Username
        ↓
Generate Unique Account Number
        ↓
Create Customer Object
        ↓
Store Customer Record in MongoDB
```

### User Login

```text
Enter Username
        ↓
Verify Username
        ↓
Verify Password
        ↓
Authentication Success
```

### Banking Operations

```text
Login
   ↓
Bank Menu
   ↓
Balance Enquiry
Deposit
Withdraw
Fund Transfer
   ↓
Update MongoDB
   ↓
Store Transaction Record
```

---

## 🧠 OOP Design

### Customer Class

Responsible for:

* Storing customer information
* Creating customer records
* Passing customer data to MongoDB

### Bank Class

Responsible for:

* Balance Enquiry
* Cash Deposit
* Cash Withdrawal
* Fund Transfer
* Transaction Recording

---

## 🔐 Security Features

* Username Uniqueness Validation
* Account Number Uniqueness Validation
* Input Validation
* Exception Handling
* MongoDB Indexing

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/kontamhrushikesh/Bank--management-system.git
```

### Navigate to Project

```bash
cd Bank--management-system
```

### Install Dependencies

```bash
pip install pymongo
```

### Start MongoDB

Ensure MongoDB Server is running:

```text
mongodb://localhost:27017/
```

### Run Application

```bash
python main.py
```

---

## 📸 Application Menu

### Main Menu

```text
Welcome to Mohit Banking Project

1. SignUp
2. SignIn
```

### Banking Menu

```text
1. Balance Enquiry
2. Cash Deposit
3. Cash Withdraw
4. Fund Transfer
5. Exit
```

---

## 📚 Learning Outcomes

This project helped in understanding:

* Python Programming
* Object-Oriented Programming (OOP)
* MongoDB Database Design
* PyMongo Integration
* CRUD Operations
* Banking Business Logic
* Exception Handling
* Authentication Flow
* Modular Project Architecture

---

## 🚀 Future Enhancements

* Password Hashing using bcrypt
* Admin Dashboard
* Transaction Statement Generation
* Multiple Accounts Per User
* Account Deletion
* Loan Management Module
* Fixed Deposit Module
* Interest Calculation
* GUI Interface
* REST API Integration

---

## 👨‍💻 Author

**Hrushikesh Kontam**

Python Developer | AI/ML Enthusiast | Backend Development Learner

GitHub: https://github.com/kontamhrushikesh

---

## 📄 License

This project is developed for educational, learning, and portfolio purposes.
