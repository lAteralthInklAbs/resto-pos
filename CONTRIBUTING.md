# Contributing to RestoPoS

Thank you for your interest in contributing to RestoPoS!

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/resto-pos.git`
3. Create a branch: `git checkout -b feature/your-feature`
4. Install dependencies: `pip install -r requirements.txt`
5. Make your changes
6. Run tests: `pytest tests/ -v`
7. Run linter: `ruff check src/ tests/`
8. Commit your changes with a clear message
9. Push to your fork and submit a Pull Request

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
pip install pytest ruff

# Run development server
python app.py

# Run tests
pytest tests/ -v

# Run linter
ruff check src/ tests/
```

## Code Style

- Follow PEP 8
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Write tests for new features

## Pull Request Guidelines

- Create one PR per feature/fix
- Include tests for new functionality
- Update documentation if needed
- Ensure CI passes before requesting review
- Reference related issues in the PR description

## Reporting Issues

When reporting issues, please include:

- Python version
- OS and version
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

## Questions?

Feel free to open an issue for questions or discussion.
