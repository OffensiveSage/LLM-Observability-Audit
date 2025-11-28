# Security Policy

## 🛡️ Reporting Vulnerabilities

**Do not open public GitHub issues for security vulnerabilities.**

If you discover a security issue, please report it privately by emailing the maintainer. We adhere to the principle of **Coordinated Vulnerability Disclosure**.

## 🔐 Project Security Standards

### 1. Secrets Management
*   **Strict Isolation**: API keys (e.g., Groq, OpenAI) must **never** be committed to version control.
*   **Environment Variables**: All secrets are loaded exclusively from a local `.env` file.
*   **Git Protection**: The `.gitignore` file is configured to strictly exclude `.env`, `*.key`, and `secrets/`.
*   **Key Rotation**: In the event of an accidental commit, all exposed keys must be revoked and rotated immediately.

### 2. Data Privacy & Anonymization
*   **No PII**: This repository must not contain Personally Identifiable Information (PII).
*   **Synthetic Data**: Use only anonymized or synthetic datasets for testing (e.g., `data/RA_Application_Task.csv`).
*   **Output Sanitization**: Review all generated artifacts (logs, CSVs, HTML) for sensitive data before committing.

### 3. Dependency Security
*   **Vulnerability Scanning**: We utilize GitHub Actions to scan dependencies for known CVEs.
*   **Minimal Footprint**: Only essential, well-maintained packages are included in `requirements.txt`.

## ✅ Contributor Security Checklist

Before submitting a Pull Request, verify the following:

- [ ] **Secrets Check**: No API keys or credentials are hardcoded.
- [ ] **Git Status**: The `.env` file is untracked.
- [ ] **Data Review**: No real user data is present in outputs.
- [ ] **Sanitization**: Error messages and logs do not leak internal state or secrets.

## 🛡️ Secure Development Lifecycle (SDLC)

1.  **Input Validation**: Sanitize all external inputs before processing.
2.  **Fail Safe**: Ensure the application fails securely without exposing stack traces to end-users.
3.  **Audit Trails**: Maintain observability (via OpenTelemetry) without logging sensitive payloads.
