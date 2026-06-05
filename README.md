# 🏦 Bank Management System

## 📌 Project Overview

The Bank Management System is a full-stack web application designed to manage banking operations efficiently. The system provides functionalities for customer management, account management, transaction processing, loan management, employee management, and branch management.

The objective of this project is to create a secure, scalable, and user-friendly banking platform that simplifies day-to-day banking activities while maintaining data integrity and security.

---

## 🎯 Features

### 👤 User Management

- User Registration
- Secure Login & Authentication
- Role-Based Access Control
- Profile Management

### 🏦 Customer Management

- Customer Registration
- KYC Verification
- Customer Information Management
- Address and Identity Storage

### 💳 Account Management

- Savings Account Creation
- Current Account Creation
- Account Status Management
- Balance Tracking
- Account Details Management

### 💰 Transaction Management

- Deposit Funds
- Withdraw Funds
- Transfer Funds
- Transaction History
- Reference Number Tracking

### 👥 Beneficiary Management

- Add Beneficiary
- Update Beneficiary
- Delete Beneficiary
- Transfer to Beneficiaries

### 📈 Loan Management

- Apply for Loan
- Loan Approval Process
- EMI Calculation
- Loan Status Tracking

### 🏢 Branch Management

- Branch Registration
- IFSC Management
- Branch Details Management

### 👨‍💼 Employee Management

- Employee Registration
- Branch Assignment
- Employee Role Management

---

## 🛠️ Technology Stack

### Frontend

- React.js
- HTML5
- CSS3
- JavaScript
- Bootstrap / Tailwind CSS

### Backend

- Node.js
- Express.js

### Database

- MongoDB

### Authentication

- JWT Authentication
- Bcrypt Password Hashing

### Tools

- Git
- GitHub
- Postman
- MongoDB Compass

---

## 📂 Project Structure

```bash
Bank-Management-System/
│
├── backend/
│   ├── config/
│   ├── controllers/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── app.js
│   └── server.js
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── context/
│   │   └── App.js
│   │
│   └── package.json
│
├── README.md
└── .env
```

---


## 🔗 Database Relationships

```text
Users (1) -------- (1) Customers

Customers (1) ---- (M) Accounts

Accounts (1) ----- (M) Transactions

Customers (1) ---- (M) Beneficiaries

Customers (1) ---- (M) Loans

Branches (1) ----- (M) Employees

Users (1) -------- (1) Employees
```

---

## 🔐 Security Features

- JWT Authentication
- Password Hashing using Bcrypt
- Role-Based Authorization
- Protected API Routes
- Input Validation
- Error Handling Middleware
- Environment Variable Protection

---

## ⚙️ Environment Variables

```env
PORT=5000

MONGO_URI=your_mongodb_connection_string

JWT_SECRET=your_secret_key
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/bank-management-system.git
```

### Navigate to Project

```bash
cd bank-management-system
```

### Install Backend Dependencies

```bash
cd backend
npm install
```

### Install Frontend Dependencies

```bash
cd ../frontend
npm install
```

### Start Backend Server

```bash
npm run dev
```

### Start Frontend

```bash
npm start
```

---

## 📊 Future Enhancements

- Internet Banking
- Mobile Banking
- UPI Integration
- Credit Card Module
- Fixed Deposit Module
- SMS Notifications
- Email Notifications
- AI Fraud Detection
- Analytics Dashboard
- Audit Logging

---

## 👨‍💻 Author

**Hrushikesh Kontam**

GitHub: https://github.com/

LinkedIn: https://linkedin.com/

---

## 📄 License

This project is developed for educational and portfolio purposes.
