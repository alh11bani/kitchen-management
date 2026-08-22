# 🍽️ Kitchen Management System

A complete and easy-to-use web application built with **Django** to manage kitchen orders seamlessly.

The system allows customers to browse the menu and place orders online, while providing kitchen staff with an advanced dashboard to monitor and update order statuses efficiently.

---

## ✨ Features

### 👥 For Customers

* 🔐 **Account Management**

  * User registration and login
  * Profile management
  * Profile picture uploads

* 🍛 **Browse the Menu**

  * View available food options
  * Browse meals such as rice and proteins
  * View prices for each item

* 🛒 **Place Orders**

  * Select meals and food items
  * Choose the number of portions
  * Select meal time: **Lunch / Dinner**
  * Automatically calculate the total price

* 📦 **Order Tracking**

  * Track current and previous orders
  * View order status
  * Cancel new orders before the kitchen starts preparing them

---

### 👨‍🍳 For Kitchen Staff / Admins

* 📊 **Live Dashboard**

  * View order statistics at a glance
  * Monitor orders by status:

    * 🆕 New
    * 👨‍🍳 Preparing
    * ✅ Ready
    * 📦 Completed

* ⚡ **Instant Updates**

  * Update order statuses with a single click
  * No page refresh required
  * Powered by **AJAX**

* 🔎 **Order History & Filtering**

  * View all orders
  * Filter orders by status
  * Filter orders by meal time

* 📝 **Activity Logs**

  * Track who changed an order's status
  * Record exactly when each change occurred

---

## 🛠️ Tech Stack

| Technology           | Description                      |
| -------------------- | -------------------------------- |
| 🐍 Python 3.11       | Backend programming language     |
| 🎯 Django 6.0        | Web framework                    |
| 🌐 HTML5             | Page structure                   |
| 🎨 CSS3              | Styling                          |
| 🅱️ Bootstrap 5      | UI framework                     |
| ⚡ Vanilla JavaScript | Frontend interactions            |
| 🗄️ SQLite           | Development database             |
| 🐘 PostgreSQL        | Production-ready database option |

---

## 🌍 Live Demo

The project is deployed and available for testing:

**[🚀 Kitchen Management System — Live Preview](https://kitchen-management-bjx7.onrender.com/#)**


---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/kitchen-management.git
cd kitchen-management
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create an Admin Account

Create a Django superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter your username, email, and password.

### 7. Run the Development Server

```bash
python manage.py runserver
```

The project will now be available at:

```text
http://127.0.0.1:8000/
```


---

## 📄 License

This project is an **open-source project created for educational purposes**.

Feel free to use, modify, and improve it for your own learning and development.

---

