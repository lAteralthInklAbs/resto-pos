# RestoPoS

[![CI](https://github.com/lAteralthInklAbs/resto-pos/actions/workflows/ci.yml/badge.svg)](https://github.com/lAteralthInklAbs/resto-pos/actions/workflows/ci.yml)
[![Demo](https://img.shields.io/badge/demo-live-brightgreen)](https://lateralthinklabs.github.io/resto-pos/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Full-stack Restaurant Point of Sale** - Flask web app with live browser demo

[**Live Demo**](https://lateralthinklabs.github.io/resto-pos/) | [Documentation](docs/architecture.md)

## Try It Now

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/lAteralthInklAbs/resto-pos)

Click the button above to launch the full app with database in your browser. No installation needed.

Or try the [static demo](https://lateralthinklabs.github.io/resto-pos/) (no server, runs in browser only).

## Why This Exists

Fast food cashiers need a simple POS. This handles:
- Customer registration
- Menu ordering (19 items across 4 categories)
- Bill calculation (18% tax, 1% service charge)
- Receipt generation

Originally built with Tkinter + MySQL, reengineered to Flask + SQLite with MVC architecture, tests, Docker, and CI/CD.

## Reengineering Highlights

| Aspect | Legacy (Tkinter) | Reengineered (Flask) |
|--------|------------------|---------------------|
| **UI** | Desktop-only Tk widgets | Web browser (any device) |
| **Database** | MySQL with hardcoded password | SQLite with env vars |
| **Architecture** | Monolithic scripts | MVC with blueprints |
| **Testing** | None | pytest with 90%+ coverage |
| **Deployment** | Manual install | Docker + GitHub Actions |
| **Demo** | Run locally | Live GitHub Pages |
| **Security** | Exposed credentials | Environment variables |

## Architecture

```
Browser → Flask Routes → Services → SQLAlchemy Models → SQLite
```

See [docs/architecture.md](docs/architecture.md) for details.

## Menu

| Category | Item | Price (Rs.) |
|----------|------|-------------|
| South Indian | Rava Dosa | 70 |
| South Indian | Masala Dosa | 75 |
| South Indian | Sada Dosa | 60 |
| South Indian | Idli Plate | 40 |
| South Indian | Vada Plate | 50 |
| Chinese | Chinese Bhel | 25 |
| Chinese | Manchurian Soup | 50 |
| Chinese | Singapore Soup | 75 |
| Chicken | Chicken 65 | 120 |
| Chicken | Chicken Crispy | 135 |
| Chicken | Chicken Manchurian | 130 |
| Rice & Noodles | Egg Fried Rice | 85 |
| Rice & Noodles | Egg Fried Noodles | 90 |
| Rice & Noodles | Chicken Fried Rice | 100 |
| Rice & Noodles | Chicken Fried Noodles | 110 |
| Rice & Noodles | Chicken Triple Rice | 130 |
| Rice & Noodles | Chicken Triple Noodles | 150 |
| Rice & Noodles | Veg Triple Rice | 110 |
| Rice & Noodles | Veg Triple Noodles | 124 |

## Quick Start

### Docker (Recommended)

```bash
docker-compose up
# Open http://localhost:5000
```

### Local

```bash
# Clone
git clone https://github.com/lAteralthInklAbs/resto-pos.git
cd resto-pos

# Install
pip install -r requirements.txt

# Run
python app.py
# Open http://localhost:5000

# Login: admin / admin
```

## Demo

The [live demo](https://lateralthinklabs.github.io/resto-pos/) implements the complete 5-screen POS flow:

1. **Login** - Cashier authentication
2. **Dashboard** - Main menu with actions
3. **Customer Registration** - Optional customer details
4. **Order Entry** - Menu items grouped by category with quantity selection
5. **Payment & Receipt** - Bill with tax/service charge, payment, printable receipt

No server required - runs entirely in the browser using JavaScript and localStorage.

## API Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/login` | Login page |
| POST | `/login` | Authenticate (admin/admin) |
| GET | `/logout` | Clear session |
| GET | `/dashboard` | Main dashboard |
| GET | `/customers/new` | Customer form |
| POST | `/customers` | Register customer |
| GET | `/orders/new` | Order page with menu |
| POST | `/orders` | Create order |
| GET | `/orders/<id>/payment` | Payment page |
| POST | `/orders/<id>/pay` | Process payment |
| GET | `/orders/<id>/receipt` | View receipt |
| GET | `/api/menu` | JSON menu items |

## Testing

```bash
# Run all tests
make test
# or
pytest tests/ -v

# Run linter
make lint
# or
ruff check src/ tests/

# Full CI check
make ci
```

## Design Decisions

| ADR | Decision | Rationale |
|-----|----------|-----------|
| [ADR-001](docs/adr/ADR-001-flask-over-tkinter.md) | Flask over Tkinter | Browser access, cloud deployment, testability |
| [ADR-002](docs/adr/ADR-002-sqlite-over-mysql.md) | SQLite over MySQL | Zero deps, env-var config, in-memory testing |

## Project Structure

```
resto-pos/
├── app.py              # Flask app factory
├── src/
│   ├── models.py       # SQLAlchemy models
│   ├── routes.py       # Flask blueprints
│   ├── services.py     # Business logic
│   ├── config.py       # Configuration
│   └── seed_data.py    # Menu data seeder
├── templates/          # Jinja2 HTML templates
├── static/             # CSS and JavaScript
├── tests/              # pytest tests
├── demo/               # GitHub Pages demo
├── legacy/             # Original Tkinter code
└── docs/               # Documentation
```

## License

MIT - see [LICENSE](LICENSE)

---

Built with Flask, SQLAlchemy, and Bootstrap 5
