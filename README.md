# Debt Collection CRM

Full-stack CRM built with FastAPI (backend) and Streamlit (frontend).

## Run without Docker

```bash
# Install dependencies
pip install -r requirements.txt

# Start backend
uvicorn backend.main:app --reload

# In a second terminal
streamlit run frontend/app.py
