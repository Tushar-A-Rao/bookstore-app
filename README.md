📚 BookStore App
A full-stack BookStore application built as a DevOps learning project.

🛠️ Tech Stack
Backend - Python + Flask
Database - MongoDB Atlas
Frontend - HTML, CSS, JavaScript

🚀 Project Roadmap
✅ Phase 1 - Flask Backend + Frontend
✅ Phase 2 - Microservices
✅ Phase 3 - Docker + Docker Compose
⏳ Phase 4 - CI/CD Pipeline
⏳ Phase 5 - Kubernetes
⏳ Phase 6 - Monitoring (Prometheus + Grafana)

📡 API Routes
Method  Route                        Description
GET     /api/books                   Get all books
POST    /api/books                   Add a book
DELETE  /api/books/:id               Delete a book
GET     /api/books/search?query=     Search books

⚙️ How To Run Locally (Without Docker)
1. Clone the repo
2. Create a .env file (refer .env.example)
3. Install dependencies: pip install flask pymongo python-dotenv flask-cors
4. Run the app: python app.py

🐳 How To Run With Docker (Phase 3)
1. Clone the repo
2. Create a .env file in the root folder:
   MONGO_URI=your_mongodb_atlas_uri
   DB_NAME=bookstore
3. Run: docker compose up -d
4. Open http://localhost:5000

Services
Each service is containerized individually:
- book_service/     → Port 5001
- search_service/   → Port 5002
- frontend_service/ → Port 5000

Files added per service:
- Dockerfile        — builds the service image
- requirements.txt  — Python dependencies
- .dockerignore     — excludes venv, .env, pycache from image