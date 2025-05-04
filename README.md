# Webhook Delivery Backend

This is a basic backend project that simulates a webhook delivery system using FastAPI, SQLite, Redis, and a background worker.

## 🔧 Features

- Register webhook clients
- Send events to registered webhooks
- Queue events in Redis
- Deliver events using a background worker

## 🧰 Tech Stack

- Python
- FastAPI
- SQLite
- Redis (via WSL or local install)
- Requests (for webhook delivery)

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
2. Create a Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Linux/macOS
3. Install Requirements
bash
Copy code
pip install -r requirements.txt
4. Start Redis Server
If you're using WSL:

bash
Copy code
sudo service redis-server start
Make sure it's running by typing:

bash
Copy code
redis-cli ping
# Should return: PONG
📡 Run the FastAPI Server
bash
Copy code
uvicorn app.main:app --reload
Open your browser to: http://127.0.0.1:8000/docs

Use Swagger UI to test the /register and /event endpoints.

🛠️ Run the Worker
In a second terminal:

bash
Copy code
venv\Scripts\activate  # Or source venv/bin/activate
python app/worker.py
This will listen for queued events and send them to the appropriate webhook URLs.

📁 Project Structure
bash
Copy code
app/
│
├── main.py          # FastAPI app
├── database.py      # DB setup
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── worker.py        # Redis background worker
└── utils.py         # (Optional utility functions)