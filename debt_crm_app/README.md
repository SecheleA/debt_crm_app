# Debt Collection CRM

This project is a debt collection CRM built with FastAPI (backend) and Streamlit (frontend). It includes features like authentication, debtor management, reminders, activity logging, and performance dashboards.

## Features

- Role-based user system (Collector, Supervisor, Client, Admin)
- Debtor records, notes, PTPs, and activity logs
- Reminders and notification system
- Legal flags, QA review, and performance KPIs
- Upload documents and track call consents

## Running the Project

### Using Docker

```bash
docker build -t debt_crm .
docker run -p 8000:8000 -p 8501:8501 debt_crm
```

Then access:
- Backend: http://localhost:8000/docs
- Frontend: http://localhost:8501
