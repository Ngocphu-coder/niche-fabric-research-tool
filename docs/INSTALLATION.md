# Installation Guide

## Prerequisites
- Python 3.9+
- Node.js 16+
- npm or yarn
- Git

## Backend Setup

### 1. Create Virtual Environment
```bash
cd backend
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
# Edit .env with your settings
```

### 5. Run Database Migrations
```bash
alembic upgrade head
```

### 6. Start Backend Server
```bash
python -m uvicorn main:app --reload
```

Backend will be available at: `http://localhost:8000`

## Frontend Setup

### 1. Install Dependencies
```bash
cd frontend
npm install
```

### 2. Start Development Server
```bash
npm run dev
```

Frontend will open at: `http://localhost:3000`

## Running Both Services

### Terminal 1 (Backend)
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python -m uvicorn main:app --reload
```

### Terminal 2 (Frontend)
```bash
cd frontend
npm run dev
```

## Troubleshooting

### Port Already in Use
- Backend: Change `PORT` in `.env` (default 8000)
- Frontend: Set `PORT=3001 npm start`

### Database Issues
- Delete `*.db` file and run migrations again
- Check database URL in `.env`

### Dependencies Issues
- Clear npm cache: `npm cache clean --force`
- Reinstall: `rm -rf node_modules && npm install`
