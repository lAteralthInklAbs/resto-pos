# ADR-002: SQLite over MySQL

## Status

Accepted

## Context

The original application used MySQL with:

- Hardcoded password ("anuroop1602") in source code
- Required MySQL server installation
- No environment-based configuration
- Manual database setup

## Decision

Replace MySQL with SQLite via SQLAlchemy ORM:

- Database file stored locally (pos.db)
- Configuration via environment variables
- In-memory database for testing
- SQLAlchemy provides database abstraction

## Rationale

1. **Zero External Dependencies**: SQLite is built into Python
2. **Env-var Configuration**: No hardcoded credentials
3. **In-memory Testing**: Fast, isolated test runs
4. **Portability**: Single file, easy to backup/move
5. **SQLAlchemy ORM**: Can switch to PostgreSQL/MySQL later if needed

## Consequences

### Positive

- No database server installation
- Secure credential management
- Fast test execution
- Simpler deployment
- Works offline

### Negative

- Not suitable for high-concurrency (>100 concurrent writes)
- No built-in replication
- Limited to single-server deployments

### Mitigations

- For high-traffic scenarios, switch DATABASE_URL to PostgreSQL
- SQLAlchemy ORM makes this a configuration change only

## Alternatives Considered

- **PostgreSQL**: Better for production, but requires installation
- **MySQL/MariaDB**: Same issues as original
- **MongoDB**: Overkill, doesn't match relational data model
