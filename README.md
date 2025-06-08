# Resume Extractor

A modern web application that extracts information from resumes and provides a user-friendly interface to manage and view extracted data.

## Project Overview

The Resume Extractor is a full-stack web application built with a microservices architecture. It consists of two main components:

1. **Frontend**: A modern React.js application built with Tailwind CSS for styling
2. **Backend**: A Flask-based API service that handles resume processing and data extraction

## Features

- Upload resumes in various formats (PDF, DOCX, etc.)
- Extract key information from resumes
- View and manage extracted resume data
- Modern, responsive user interface
- Containerized deployment using Docker

## Prerequisites

- Docker and Docker Compose
- Modern web browser (Chrome, Firefox, Safari)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd resume-extractor
```

2. Build and run the application using Docker Compose:
```bash
docker-compose up --build
```

This will:
- Build the frontend and backend services
- Start the containers
- Set up all necessary configurations

## Accessing the Application

Once the containers are running:

- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Project Structure

```
resume-extractor/
├── backend/              # Flask backend service
├── resume-extractor-frontend/  # React frontend application
├── docker-compose.yml    # Docker Compose configuration
└── .gitignore           # Git ignore file
```

## Development

### Frontend Development

For local frontend development:

1. Navigate to the frontend directory:
```bash
cd resume-extractor-frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

### Backend Development

For local backend development:

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask application:
```bash
python app.py
```

## Deployment

The application is designed to be deployed using Docker Compose. The `docker-compose.yml` file contains all necessary configurations for both frontend and backend services.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
