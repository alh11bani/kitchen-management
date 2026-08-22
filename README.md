🍽️ Kitchen Management System
A complete and easy-to-use web application built with Django to manage kitchen orders seamlessly. It allows customers to browse the menu and place orders online, while providing the kitchen staff with an advanced, real-time dashboard to track and update order statuses efficiently.

✨ Features
👥 For Customers:

Account Management: Full user authentication system including registration, login, and profile management with profile picture uploads.

Browse the Menu: View available food options (like Rice and Proteins) along with their prices.

Place Orders: A user-friendly interface to select meals, choose the number of portions, pick the meal time (Lunch/Dinner), and view the automatically calculated total price.

Order Tracking: Customers can track the status of their previous and current orders, and cancel new orders before the kitchen starts preparing them.

👨‍🍳 For Kitchen Staff (Admins):

Live Dashboard: Quick insights and statistics for all orders (New, Preparing, Ready, Completed).

Instant Updates: Update order statuses with a single click without refreshing the page (powered by Ajax).

Order History & Filtering: A comprehensive view of all orders, with the ability to filter by order status or meal time.

Activity Logs: Keep full track of who changed an order's status and exactly when it happened.

🛠️ Tech Stack
Backend: Python 3.11, Django 6.0

Frontend: HTML5, CSS3, Bootstrap 5, Vanilla JavaScript

Database: SQLite (Configured to easily support PostgreSQL in production)

🌍 Live Demo
The project is deployed and available for testing here:
Kitchen Management System - Live Preview

🚀 How to Run Locally
Clone the repository:

Bash
git clone https://github.com/your-username/kitchen-management.git
cd kitchen-management
Create and activate a virtual environment:

Bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Apply database migrations:

Bash
python manage.py migrate
Create an admin account (Superuser):

Bash
python manage.py createsuperuser
Run the development server:

Bash
python manage.py runserver
The project will now be running at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


📄 License
This is an open-source project created for educational purposes.
