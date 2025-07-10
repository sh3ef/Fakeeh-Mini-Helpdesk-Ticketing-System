# Mini Helpdesk System - Fakeeh College Developer Task

This project is a simple helpdesk web application, developed as part of the developer assessment task for Fakeeh College for Medical Sciences.


---

## 🚀 Live Demo

You can try the live application at the following link:

**[https://fakeeh-mini-helpdesk-ticketing-system.onrender.com](https://fakeeh-mini-helpdesk-ticketing-system.onrender.com)**

> **Note:** The application may take a few seconds to load initially due to Render's free tier spinning up.

---

## 📋 Overview

The project is a ticketing system that allows staff to create and track support tickets, while administrators can manage, reply to, and close all tickets. The application was built as a Full-Stack Web Application with a backend, frontend, and a real database.

---

## ✨ Features

### For All Users (Admin & Staff):
- **🔐 Login:** Secure authentication system for user login.
- **📝 Create Ticket:** Users can create a new ticket with a title and a description.
- **👀 View Own Tickets:** Each user can view a list of tickets they have submitted.
- **💬 Reply to Tickets:** Users can add replies to their tickets, creating a comment thread.

### For Staff Users:
- **📋 Personal Dashboard:** View only tickets they have created.
- **🔍 Track Status:** Monitor if their tickets are open or closed.
- **💬 Communicate:** Add replies and follow up on their submitted tickets.
- 
### For Admins Only:
- **📊 Comprehensive View:** Admins can view **all** tickets submitted by **all** users.
- **💬 Reply to Any Ticket:** Admins can reply to any ticket in the system.
- **🔒 Close Tickets:** Admins can change a ticket's status from "Open" to "Closed".
- **📈 Admin Dashboard:** A special dashboard that displays quick statistics about open, closed, and total tickets.
- **🔍 Filter Tickets:** Admins can filter the ticket view by status (All, Open, Closed).


### ✨ Bonus Features

To enhance the application's quality and user experience, several features were added that were not explicitly required by the task:

-   **🔒 Password Security:** The **Bcrypt** algorithm was used to **hash** passwords before storing them in the database, ensuring they are not stored in plain text and are fully protected.
-   **🌐 Internationalization (i18n):** The application supports a user interface in both **Arabic and English**, with instant switching between them via dedicated buttons in the navigation bar.
-   **🎨 Enhanced UI/UX:** An improved user interface that includes:
    - A special dashboard for the administrator with statistics cards.
    - Dynamic ticket filtering powered by JavaScript.
    - Icons (Font Awesome) to improve visual clarity.
    - Responsive design that works on all devices.
-   **⚙️ Environment Variables Documentation:** An `.env.example` file was created as a guide for other developers to facilitate the process of setting up and running the project locally.

---

## 🛠️ Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **Database:** PostgreSQL (hosted on Supabase)
- **Key Libraries:**
  - `psycopg2-binary`: For database connection.
  - `Flask-Bcrypt`: For secure password hashing.
  - `Flask-Babel`: For internationalization support.
  - `python-dotenv`: For managing environment variables.
  - `gunicorn`: For production server deployment.
- **Deployment:** Render.com
- **Version Control:** Git & GitHub

---

## 🔑 Test Credentials

You can use the accounts suggested in the task and sent to you in email.

---

## 📸 Screenshots

### Admin Dashboard
- Clean interface with ticket statistics
  
  ![image](https://github.com/user-attachments/assets/b80fcc77-76ea-4279-9ee3-b94fc8f10df4)
  ![image](https://github.com/user-attachments/assets/ea8988ac-e029-415d-b011-5b779d092e52)

- Filter functionality for easy ticket management
  
  ![image](https://github.com/user-attachments/assets/bf3920dc-2fa9-4544-b296-bd09474e6672)
  ![image](https://github.com/user-attachments/assets/c97c4c81-48de-426c-a638-717ca546389c)

- Responsive design for all screen sizes

### Ticket Management
- Simple ticket creation form
  
  ![image](https://github.com/user-attachments/assets/fe209515-f5e8-4fc0-b057-2e9ef3043662)
  ![image](https://github.com/user-attachments/assets/2d825071-2baa-49da-997c-b7a06b6745a1)


- Threaded conversation view
  
  ![image](https://github.com/user-attachments/assets/8773672a-87ec-4d4c-bb87-6c696a6d2cb7)
  ![image](https://github.com/user-attachments/assets/fa6a5e23-f323-4f11-88cf-b3dde0d4660f)


- Status management for administrators
  
  ![image](https://github.com/user-attachments/assets/6b4d857f-2480-4d65-864c-8280e4034f5c)
  ![image](https://github.com/user-attachments/assets/22b726a8-e2b9-4f1b-81d6-c457f7d33644)





---

## ⚙️ Setup Instructions (How to run locally)

To run this project on your local machine, follow these steps:

### Prerequisites
- Python 3.8 or higher
- PostgreSQL database (or use SQLite for development)
- Git

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/fakeeh-mini-helpdesk-ticketing-system.git
    cd fakeeh-mini-helpdesk-ticketing-system
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    
    # On Windows
    venv\Scripts\activate
    
    # On Mac/Linux
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    - Copy the `.env.example` file to a new file named `.env`.
    - You will need to create your own PostgreSQL database (on Supabase or any other platform).
    - Fill in the actual values in the `.env` file:
      ```ini
      DATABASE_URL=your_own_postgresql_connection_string
      SECRET_KEY=a_very_strong_random_secret_key
      ```

5.  **Initialize the database:**
    - In your PostgreSQL database, run the SQL commands found in the `schema.sql` file.
    - This will create all the necessary tables (`users`, `tickets`, `replies`) and populate them with the required initial data (6 test users and 5 sample tickets).
      
6.  **Run the application:**
    ```bash
    python app.py
    ```

7.  **Access the application:**
    Open your browser and navigate to `http://127.0.0.1:5001`

---

## 🚀 Deployment

This application is deployed on Render.com. 

---

## 📁 Project Structure

```
fakeeh-helpdesk/
├── templates/          # HTML templates
├── static/            # CSS, JS, and static assets
├── translations/      # i18n translation files
├── app.py            # Main Flask application
├── models.py         # Database models
├── config.py         # Configuration settings
├── requirements.txt  # Python dependencies
└── README.md        # Project documentation
```


---

## 📞 Contact

eng.shifaa.moh@gmail.com
---

**⭐ I hope you have a great experience!**
