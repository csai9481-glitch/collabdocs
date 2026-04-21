# 📄 CollabDocs API

A Django REST API for collaborative document management with version control, tagging, and activity tracking.

---

## 🚀 Features

* 🧑‍🤝‍🧑 Workspace management
* 📄 Document creation & editing
* 🕓 Automatic document versioning
* 🏷️ Tagging system
* 💬 Comments on documents
* 📊 Document statistics
* 📝 Audit logs for tracking actions
* 🔍 Search & filtering support

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (default)

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/csai9481-glitch/collabdocs.git
cd collabdocs
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Apply Migrations

```bash
python manage.py migrate
```

---

### 5. Run Server

```bash
python manage.py runserver
```

---

### 6. Open in Browser

```text
http://127.0.0.1:8000/api/
```

---

## 📌 API Endpoints

| Feature    | Endpoint                        |
| ---------- | ------------------------------- |
| Workspaces | `/api/workspaces/`              |
| Members    | `/api/members/`                 |
| Documents  | `/api/documents/`               |
| Versions   | `/api/documents/{id}/versions/` |
| Comments   | `/api/comments/`                |
| Tags       | `/api/tags/`                    |
| Audit Logs | `/api/auditlogs/`               |

---

## 🔍 Custom Endpoints

* Draft Documents
  `/api/documents/status-draft/`

* Search Documents
  `/api/documents/search/?q=keyword`

* Document Stats
  `/api/documents/stats/`

---

## 📸 Screenshots

(Add your screenshots here)

* Workspace List
* Document Creation
* Version History
* API Root

---

## 📂 Project Structure

```
collabdocs/
│
├── core/
├── collabdocs/
├── manage.py
├── requirements.txt
└── .env.example
```

---

## 👤 Author

**Charan Sai Kumar M**

---

## 📄 License

This project is for educational purposes.
