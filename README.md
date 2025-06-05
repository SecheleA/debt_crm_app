# Debt CRM App

A modern debt collection CRM with FastAPI + Streamlit.

## 🚀 Features
- Debtor management
- Notes, PTPs, Invoices, Reminders
- User roles (Collector, Supervisor, Admin)
- Risk scoring, segmentation, legal flags
- KPIs, call logs, QA reviews

## 🛠 Tech Stack
- FastAPI (backend)
- Streamlit (frontend)
- SQLModel + SQLite (database)
- Docker (optional containerization)

## 🔧 How to Run

### Without Docker
```bash
# Backend
cd backend
uvicorn main:app --reload

# In another terminal
cd frontend
streamlit run app.py
