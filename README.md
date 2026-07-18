# Student Management System

A professional-grade Python application for managing student records with full Docker containerization and CI/CD automation.

## Features

- **Add Students**: Register new students with ID, name, and grade
- **Remove Students**: Delete student records by ID
- **Search Students**: Case-insensitive search by student ID or name
- **Update Students**: Modify student information (name and/or grade)
- **Export Students**: Export all student records in CSV format

## Quick Start

### Docker (Recommended)

Pull and run the latest image from Docker Hub:

```bash
docker run --rm godsogeking/student-management:latest
```

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/AlexGithub901/Student-Management-System.git
cd Student-Management-System
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests:
```bash
pytest test_student.py -v
```

## Docker Setup

### Build Locally

```bash
docker build -t student-management:latest .
```

### Run Tests

```bash
docker run --rm student-management:latest
```

### Using Docker Compose

```bash
docker compose up
```

## Project Structure

```
.
├── student.py              # Core student management logic
├── test_student.py         # Comprehensive test suite (13 tests)
├── requirements.txt        # Python dependencies
├── Dockerfile              # Multi-stage Docker build
├── docker-compose.yml      # Compose configuration
├── .dockerignore           # Files excluded from Docker build
├── .github/
│   └── workflows/
│       ├── python.yml      # Python CI workflow
│       └── docker.yml      # Docker build & push workflow
└── README.md               # This file
```

## Image Details

- **Base Image**: `python:3.12-slim`
- **Size**: 50.6MB
- **Registry**: Docker Hub - `godsogeking/student-management`
- **Tags**: 
  - `latest` - Most recent build
  - `<commit-sha>` - Versioned by commit

## API Functions

### Core Functions

```python
add_student(student_id, name, grade) -> bool
remove_student(student_id) -> bool
search_student(query) -> list
update_student(student_id, name=None, grade=None) -> bool
export_students() -> str
```

## Testing

All 13 tests pass successfully:

- ✓ Add student (new and duplicate cases)
- ✓ Remove student (existing and not found cases)
- ✓ Search by ID (exact match)
- ✓ Search by name (partial, case-insensitive)
- ✓ Update student (single and multiple fields)
- ✓ Export to CSV

Run tests locally:
```bash
pytest test_student.py -v
```

Run tests in Docker:
```bash
docker compose up
```

## CI/CD Pipeline

This project includes automated GitHub Actions workflows:

### Python CI Workflow
- Triggers on: push to `main`, `feature-student-search`, `feature-export`, and pull requests
- Runs: Python 3.12 tests with pytest

### Docker Build & Push Workflow
- Triggers on: push to `main` and pull requests
- Builds: Docker image using Docker Buildx
- Tests: Runs all tests inside container
- Pushes: To Docker Hub on successful main branch push
- Caching: GitHub Actions cache for faster builds

#### GitHub Secrets Required
- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub access token

## Installation for Contributors

1. Fork the repository
2. Clone your fork
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Install dev dependencies: `pip install -r requirements.txt`
5. Make changes and test: `pytest test_student.py -v`
6. Push and create a Pull Request

## Dockerfile Optimization

The Dockerfile follows best practices:

- **Layer Caching**: `requirements.txt` copied separately for better cache hits
- **Slim Base**: Uses `python:3.12-slim` (not full `python:3.12`)
- **No Cache**: `pip install --no-cache-dir` reduces image size
- **.dockerignore**: Excludes unnecessary files (__pycache__, .git, etc.)

## Docker Hub

Image available at: https://hub.docker.com/r/godsogeking/student-management

Pull command:
```bash
docker pull godsogeking/student-management:latest
```

## License

See LICENSE file for details.

## Author

AlexGithub901

## Troubleshooting

### Docker authentication fails
- Verify Docker Hub credentials: `docker login`
- Check GitHub secrets are properly configured
- Ensure access token has read/write permissions

### Tests fail in container
- Rebuild without cache: `docker build --no-cache -t student-management .`
- Check Docker logs: `docker logs <container-id>`

### Image too large
- Verify .dockerignore is properly configured
- Check for unnecessary dependencies in requirements.txt

## Support

For issues or questions, open an issue on GitHub.
