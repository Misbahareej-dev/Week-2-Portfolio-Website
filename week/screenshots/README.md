# 🚀 TaskFlow — Full Stack Task Manager

### 💻 A Modern, Responsive & Professional Task Management Web Application

**Software Development Internship — Week 4 Project**

`Python` • `Flask` • `SQLite` • `HTML5` • `CSS3` • `JavaScript` • `REST API`

---

## 📑 Table of Contents

- [🌟 Project Overview](#-project-overview)
- [🎯 Project Objectives](#-project-objectives)
- [✨ Key Features](#-key-features)
- [🛠️ Technologies Used](#️-technologies-used)
- [📁 Project Structure](#-project-structure)
- [⚙️ Installation Guide](#️-installation-guide)
- [🔌 API Endpoints](#-api-endpoints)
- [🧪 API Testing](#-api-testing)
- [💾 Database](#-database)
- [🖥️ Frontend & Backend Integration](#️-frontend--backend-integration)
- [📱 Responsive Design](#-responsive-design)
- [📸 Project Screenshots](#-project-screenshots)
- [📈 CRUD Operations](#-crud-operations)
- [🎓 Learning Outcomes](#-learning-outcomes)
- [📦 Week 4 Deliverables](#-week-4-deliverables)
- [👩‍💻 Project Information](#-project-information)

---

## 🌟 Project Overview

TaskFlow is a full-stack Task Management Web Application developed using:

**Python Flask + SQLite + HTML5 + CSS3 + JavaScript**

The application provides a complete task management workflow through a responsive and professional user interface connected to a Flask REST API and SQLite database.

### Users Can

- ➕ Create new tasks
- 👀 View existing tasks
- ✏️ Update tasks
- ✅ Mark tasks as completed
- ↩️ Undo completed tasks
- 🗑️ Delete tasks
- 📊 View Total, Completed, and Pending task statistics

### Application Architecture

Frontend → JavaScript → Flask REST API → SQLite Database → Response → Updated Interface

---

## 🎯 Project Objectives

The main objectives of this Week 4 Internship Project were to:

- Build a functional Flask backend
- Develop RESTful API endpoints
- Implement complete CRUD operations
- Integrate SQLite database storage
- Connect the frontend with the backend
- Test APIs using Postman
- Create a responsive and professional user interface
- Implement mobile-friendly navigation
- Display dynamic task statistics
- Prepare complete project documentation and installation instructions

---

## ✨ Key Features

### 📋 Task Management

| Feature | Description |
|---|---|
| ➕ Add Task | Create new tasks |
| 👀 View Tasks | Display existing tasks |
| ✏️ Update Task | Modify task information |
| ✅ Complete Task | Mark a task as completed |
| ↩️ Undo Task | Return a completed task to pending |
| 🗑️ Delete Task | Remove tasks |

### 📊 Task Statistics

TaskFlow provides:

- Total Tasks
- Completed Tasks
- Pending Tasks

The statistics update according to the current task data.

### 🔗 REST API

The Flask backend supports:

`GET` • `POST` • `PUT` • `DELETE`

### 💾 SQLite Database

Task information is stored locally using SQLite for persistent data management.

### 📱 Responsive Design

The application works across:

- 💻 Desktop
- 📱 Mobile

**Desktop Navigation:** `Dashboard | My Tasks | Statistics`

**Mobile Navigation:** `Home | Tasks | Stats`

### 🎨 Professional UI

The interface uses a modern **Dark Navy + Indigo** theme with:

- Clean cards
- Responsive layouts
- Clear navigation
- Interactive controls
- Mobile-friendly spacing
- Professional typography

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Backend framework & REST API |
| SQLite | Database & data storage |
| HTML5 | Frontend structure |
| CSS3 | Styling & responsive design |
| JavaScript | Frontend logic & API integration |
| Postman | API testing |
| Visual Studio Code | Development environment |
| Git & GitHub | Version control & project management |

---

## 📁 Project Structure

```
Week_4/
│
├── app.py
├── requirements.txt
├── tasks.db
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── screenshots/
    ├── 01_Basic_Flask_Backend.png
    ├── 02_Database_Creation.png
    ├── 03_Add_Task_API_Test.png
    ├── 04_View_Task_API_Test.png
    ├── 05_Update_Task_API_Test.png
    ├── 06_Delete_Task_API_Test.png
    ├── 07_TaskFlow_Desktop_Dashboard.png
    ├── 08_TaskFlow_Add_Task.png
    ├── 09_TaskFlow_Statistics.png
    ├── 10_TaskFlow_Task_Status_Overview.png
    ├── 11_TaskFlow_My_Tasks.png
    ├── 12_TaskFlow_Mobile_Dashboard.png
    ├── 13_TaskFlow_Mobile_My_Tasks.png
    └── 14_TaskFlow_Mobile_Statistics.png
```

---

## ⚙️ Installation Guide

### 1️⃣ Install Python

Check whether Python is installed:

`python --version`

### 2️⃣ Open the Project

Open the `Week_4` folder in Visual Studio Code.

Open the terminal inside the project folder.

### 3️⃣ Install Dependencies

`pip install -r requirements.txt`

If required:

`pip install flask`

### 4️⃣ Run the Application

`python app.py`

The Flask server will start.

Usually:

`http://127.0.0.1:5000/`

### 5️⃣ Open TaskFlow

Open the local address shown in the terminal in your browser.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/tasks` | Retrieve all tasks |
| `POST` | `/tasks` | Create a new task |
| `PUT` | `/tasks/<id>` | Update or complete a task |
| `DELETE` | `/tasks/<id>` | Delete a task |

---

## 🧪 API Testing

The TaskFlow APIs were tested using Postman.

### Tested Operations

- ✅ Add Task
- ✅ View Tasks
- ✅ Update Task
- ✅ Complete Task
- ✅ Delete Task

The API testing evidence is included in the `screenshots` folder.

---

## 💾 Database

TaskFlow uses SQLite for persistent task storage.

### Database File

`tasks.db`

### Stored Information

- Task ID
- Task Title
- Completion Status

---

## 🖥️ Frontend & Backend Integration

The frontend is developed using:

- HTML5
- CSS3
- JavaScript

JavaScript communicates with the Flask REST API, while Flask handles backend operations and SQLite manages task data.

### Application Flow

User Interface → JavaScript → Flask REST API → SQLite Database → Response → Updated Interface

---

## 📱 Responsive Design

TaskFlow supports both desktop and mobile layouts.

### 💻 Desktop

`Dashboard | My Tasks | Statistics`

### 📱 Mobile

`Home | Tasks | Stats`

The interface automatically adapts to different screen sizes.

---

## 📸 Project Screenshots

### 🔹 Backend & Database

### 1. Basic Flask Backend

![Basic Flask Backend](./screenshots/01_Basic_Flask_Backend.png)

### 2. Database Created

![Database Created](./screenshots/02_Database_Created.png)

---

### 🔹 API Testing

### 3. Add Task API Test

![Add Task API Test](screenshots/03_Add_Task_API_Test.png)

### 4. View Tasks API Test

![View Tasks API Test](screenshots/04_View_Tasks_API_Test.png)

### 5. Update Task API Test

![Update Task API Test](screenshots/05_Update_Task_API_Test.png)

### 6. Delete Task API Test

![Delete Task API Test](screenshots/06_Delete_Task_API_Test.png)

---

### 🔹 Desktop Frontend

### 7. TaskFlow Desktop Dashboard

![TaskFlow Desktop Dashboard](screenshots/07_TaskFlow_Desktop_Dashboard.png)

### 8. TaskFlow Add Task

![TaskFlow Add Task](screenshots/08_TaskFlow_Add_Task.png)

### 9. TaskFlow Statistics

![TaskFlow Statistics](screenshots/09_TaskFlow_Statistics.png)

### 10. TaskFlow Task Status Overview

![TaskFlow Task Status Overview](screenshots/10_TaskFlow_Task_Status_Overview.png)

### 11. TaskFlow My Tasks

![TaskFlow My Tasks](screenshots/11_TaskFlow_My_Tasks.png)

---

### 🔹 Mobile Frontend

### 12. TaskFlow Mobile Dashboard

![TaskFlow Mobile Dashboard](screenshots/12_TaskFlow_Mobile_Dashboard.png)

### 13. TaskFlow Mobile My Tasks

![TaskFlow Mobile My Tasks](screenshots/13_TaskFlow_Mobile_My_Tasks.png)

### 14. TaskFlow Mobile Statistics

![TaskFlow Mobile Statistics](screenshots/14_TaskFlow_Mobile_Statistics.png)

---

## 📈 CRUD Operations

TaskFlow implements the complete CRUD workflow:

Create → Read → Update → Delete

Add Task → View Tasks → Update Task → Remove Task

| Operation | HTTP Method | Purpose |
|---|---|---|
| Create | `POST` | Add a new task |
| Read | `GET` | View tasks |
| Update | `PUT` | Update task/status |
| Delete | `DELETE` | Remove task |

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- 🐍 Python Flask development
- 🔗 REST API development
- 🔄 CRUD operations
- 🗄️ SQLite database integration
- 🔄 Frontend-backend communication
- ⚡ JavaScript API integration
- 🧪 Postman API testing
- 📱 Responsive web development
- 🧭 Mobile navigation design
- 🔗 Git & GitHub workflow
- 📁 Project organization
- 📝 Technical documentation

---

## 📦 Week 4 Deliverables

| Deliverable | Status |
|---|---|
| Flask Backend | ✅ Complete |
| REST API | ✅ Complete |
| SQLite Database | ✅ Complete |
| CRUD Operations | ✅ Complete |
| Postman API Testing | ✅ Complete |
| Frontend Development | ✅ Complete |
| Frontend-Backend Integration | ✅ Complete |
| Desktop Responsive UI | ✅ Complete |
| Mobile Responsive UI | ✅ Complete |
| Project Screenshots | ✅ Complete |
| README Documentation | ✅ Complete |
| Installation Guide | ✅ Complete |

---

## 👩‍💻 Project Information

| Detail | Information |
|---|---|
| Project Name | TaskFlow — Full Stack Task Manager |
| Project Type | Full Stack Web Application |
| Internship | Software Development Internship |
| Project Week | Week 4 |
| Developer | Misbah Areej |
| Backend | Python + Flask |
| Database | SQLite |
| Frontend | HTML + CSS + JavaScript |
| API Testing | Postman |
| Development Tool | Visual Studio Code |

---

## ⭐ Conclusion

TaskFlow demonstrates a complete full-stack development workflow by combining:

**Flask Backend + REST API + SQLite Database + JavaScript + Responsive Frontend**

The project provides practical experience in building and integrating the major components of a full-stack web application while maintaining a clean, responsive, and user-friendly interface.

---

### 🚀 TaskFlow

**Organize. Manage. Stay Productive.**

*Software Development Internship — Week 4*
