# ADR-001: Flask over Tkinter

## Status

Accepted

## Context

The original Restaurant POS was built with Python Tkinter for the GUI and required local MySQL installation. This architecture limited:

- Accessibility (desktop-only, single machine)
- Deployment options (no cloud, no mobile)
- Testing (GUI testing is complex)
- Multi-user support (single operator)

## Decision

Reengineer the application as a Flask web application with:

- HTML/CSS/JavaScript frontend
- Flask backend with SQLAlchemy ORM
- SQLite database (portable, no installation required)
- RESTful API design

## Rationale

1. **Browser Access**: Any device with a browser can use the POS
2. **Cloud Deployable**: Can run on Heroku, Railway, AWS, etc.
3. **Testable**: HTTP endpoints are easy to test
4. **Multi-user**: Multiple cashiers can use simultaneously
5. **Demo-able**: Static HTML demo on GitHub Pages

## Consequences

### Positive

- Wider accessibility
- Easier deployment
- Better testability
- Modern development practices (CI/CD)
- Live demo without installation

### Negative

- HTML templates replace Tk widgets (rewrite required)
- Learning curve for web concepts
- Need internet for CDN resources (Bootstrap)

## Alternatives Considered

- **PyQt/PySide**: Still desktop-only
- **Electron + Python**: Heavy, complex
- **Django**: Overkill for this scale
