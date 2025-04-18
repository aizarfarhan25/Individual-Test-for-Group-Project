# Individual Test for Group Project

## Project Overview
This project consists of two main parts:
- Frontend: An e-commerce website (GegeShop) built with Next.js
- Backend: A banking system API built with Flask

## Project Structure
```
├── FrontEnd/           # Next.js e-commerce application
├── BackEnd/            # Flask banking API
└── README.md          # This file
```

## Frontend Setup (GegeShop)

### Prerequisites
- Node.js (Latest LTS version)
- npm or yarn package manager

### Installation Steps
1. Navigate to frontend directory
```bash
cd FrontEnd
```

2. Install dependencies
```bash
npm install
```

3. Start development server
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

### Running Tests
```bash
npm test
```

## Backend Setup (Banking System)

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Installation Steps
1. Navigate to backend directory
```bash
cd BackEnd
```

2. Create and activate a virtual environment
```bash
python -m venv venv 
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
or
```bash
uv sync

after that

.venv\Scripts\Activate
```

3. Install dependencies
```bash
uv add flask_sqlalchemy
```

4. Run the development server
```bash
flask --app app --debug run
```

The backend API will be available at `http://localhost:5000`

### Database Configuration
The backend uses PostgreSQL with Supabase. Configuration can be found in `BackEnd/config/setting.py`.

## Features

### Frontend (GegeShop)
- User Authentication (Login/Signup)
- Product Catalog
- Shopping Cart Management
- Checkout Process
- Responsive Design

### Backend (Banking System)
- User Management
- Account Management
- Transaction Processing
  - Deposits
  - Withdrawals
  - Transfers
- Authentication & Authorization

## Testing
- Frontend uses Jest and React Testing Library
- Backend uses pytest for testing

## Documentation
- Frontend API Documentation: [Platzi API Documentation](https://fakeapi.platzi.com/en/about/introduction/)
- Backend API Documentation: Check `BackEnd/README.md` for API endpoints and activity diagrams

## Additional Resources
- Activity Diagrams available in `BackEnd/ActivityDiagram/`
- Test Coverage Reports
- API Documentation
