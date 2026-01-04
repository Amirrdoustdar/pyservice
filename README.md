# PyService

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-latest-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange.svg)

A production-ready Python microservice built with Django, featuring Docker containerization, CI/CD pipelines, and Ansible automation.

[Features](#features) •
[Quick Start](#quick-start) •
[Documentation](#documentation) •
[API Endpoints](#api-endpoints) •
[Deployment](#deployment)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

PyService is a modern, scalable microservice template built with Django. It provides a solid foundation for building RESTful APIs with best practices in containerization, automation, and continuous integration.

### Key Highlights

- 🐳 **Docker & Docker Compose** - Fully containerized application
- 🚀 **Django REST Framework** - Powerful API development
- 🔄 **CI/CD Ready** - GitHub Actions workflows included
- 📦 **Ansible Automation** - Infrastructure as Code
- 🧪 **Testing Suite** - Unit and integration tests with pytest
- 📚 **API Documentation** - Auto-generated API docs
- 🔧 **Easy Development** - Makefile for common tasks

---

## ✨ Features

- **RESTful API Architecture** - Clean and organized API structure
- **Health Check Endpoint** - Monitor service availability
- **Swagger/OpenAPI Documentation** - Interactive API documentation at `/api/docs/`
- **Environment-based Configuration** - Easy configuration management
- **Database Migrations** - Django ORM with migration support
- **Modular Design** - Easy to extend and customize
- **Production-ready Setup** - Proper logging, error handling, and security

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **pip** (Python package manager)
- **Docker** and **Docker Compose** (optional, for containerized deployment)
- **Make** (optional, for using Makefile commands)
- **Git**

---

## 🚀 Quick Start

### Option 1: Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Amirrdoustdar/pyservice.git
   cd pyservice
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements/development.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - API Base: `http://localhost:8000`
   - Health Check: `http://localhost:8000/api/v1/health/`
   - API Documentation: `http://localhost:8000/api/docs/`

### Option 2: Docker Deployment

1. **Clone the repository**
   ```bash
   git clone https://github.com/Amirrdoustdar/pyservice.git
   cd pyservice
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   ```

3. **Build and run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - The service will be available at `http://localhost:8000`

### Option 3: Using Makefile

```bash
make install    # Install dependencies
make migrate    # Run migrations
make run        # Start development server
make test       # Run tests
```

---

## 📁 Project Structure

```
pyservice/
├── .github/
│   └── workflows/        # GitHub Actions CI/CD pipelines
├── ansible/              # Ansible playbooks for deployment
├── requirements/         # Python dependencies
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── scripts/              # Utility scripts
├── src/                  # Main application source code
├── tests/                # Test suite
├── venv./                # Virtual environment
├── .env.example          # Example environment variables
├── .gitignore           # Git ignore rules
├── Dockerfile           # Docker image definition
├── docker-compose.yml   # Docker Compose configuration
├── Makefile             # Common development tasks
├── manage.py            # Django management script
├── pyproject.toml       # Project metadata and dependencies
├── pytest.ini           # Pytest configuration
└── README.md            # This file
```

---

## 🔌 API Endpoints

### Base URL
```
http://localhost:8000/api/v1/
```

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/health/` | Health check endpoint |
| GET | `/api/docs/` | Interactive API documentation (Swagger UI) |

### Example Request

```bash
# Health Check
curl http://localhost:8000/api/v1/health/

# Response
{
  "status": "healthy",
  "timestamp": "2024-01-05T10:30:00Z"
}
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/pyservice

# Application
APP_NAME=PyService
APP_VERSION=1.0.0
```

### Database Configuration

PyService supports multiple database backends. Configure your database in the `.env` file or `settings.py`.

---

## 🛠️ Development

### Setting Up Development Environment

1. **Install development dependencies**
   ```bash
   pip install -r requirements/development.txt
   ```

2. **Run the development server**
   ```bash
   python manage.py runserver
   ```

3. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

### Code Style and Linting

```bash
# Format code
black .

# Run linter
flake8

# Type checking
mypy .
```

### Pre-commit Hooks

Install pre-commit hooks to ensure code quality:

```bash
pre-commit install
```

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_api.py

# Run with verbose output
pytest -v
```

### Test Configuration

Tests are configured in `pytest.ini`. The test suite includes:

- Unit tests
- Integration tests
- API endpoint tests

---

## 🚢 Deployment

### Docker Deployment

```bash
# Build the Docker image
docker build -t pyservice:latest .

# Run the container
docker run -p 8000:8000 pyservice:latest

# Using Docker Compose
docker-compose up -d
```

### Ansible Deployment

```bash
# Navigate to ansible directory
cd ansible

# Run the playbook
ansible-playbook -i inventory deploy.yml
```

### Production Considerations

- Set `DEBUG=False` in production
- Use a production-grade web server (Gunicorn, uWSGI)
- Configure proper database (PostgreSQL recommended)
- Set up SSL/TLS certificates
- Implement proper logging and monitoring
- Use environment-specific requirements (`requirements/production.txt`)

---

## 🔄 CI/CD Pipeline

This project includes GitHub Actions workflows for automated testing and deployment.

### Workflows

- **CI Pipeline**: Runs on every push and pull request
  - Linting and code quality checks
  - Unit and integration tests
  - Build Docker image

- **CD Pipeline**: Deploys to production on main branch merge
  - Build and push Docker image
  - Deploy to production environment

### GitHub Actions Configuration

Workflows are located in `.github/workflows/`. Configure your secrets in GitHub repository settings:

- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `SSH_PRIVATE_KEY`

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide
- Write tests for new features
- Update documentation as needed
- Keep commits atomic and descriptive

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Amir Doustdar** - [GitHub](https://github.com/Amirrdoustdar)

---

## 🙏 Acknowledgments

- Django and Django REST Framework teams
- Docker community
- All contributors and users of this project

---

## 📞 Support

If you have any questions or need help, please:

- Open an issue on GitHub
- Contact the maintainers
- Check the documentation

---

## 🗺️ Roadmap

- [ ] Add authentication and authorization
- [ ] Implement rate limiting
- [ ] Add caching layer (Redis)
- [ ] Enhance monitoring and logging
- [ ] Add more comprehensive tests
- [ ] Create admin dashboard
- [ ] Implement WebSocket support

---

<div align="center">

Made with ❤️ by Amir Doustdar

⭐ Star this repository if you find it helpful!

</div>
