# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in this project, please report it by emailing the maintainer directly rather than opening a public issue.

## Security Best Practices

### API Key Management

This project uses API keys for external services (e.g., GROQ API). **Never commit API keys to the repository.**

1. **Use `.env` files**: Store all API keys in a `.env` file (already gitignored)
2. **Use `.env.example`**: Provide a template without actual keys
3. **Rotate keys**: If a key is accidentally exposed, rotate it immediately

### Dependencies

- Regularly update dependencies to patch security vulnerabilities
- Run `pip list --outdated` to check for updates
- Consider using tools like `safety` or `pip-audit` for vulnerability scanning

### Data Privacy

- Do not commit any real user data or personally identifiable information (PII)
- Use synthetic or anonymized data for testing and examples
- Review all output files before committing to ensure no sensitive data is included

## Security Checklist for Contributors

Before pushing to GitHub:

- [ ] No API keys or secrets in code
- [ ] `.env` file is gitignored
- [ ] No sensitive data in output files
- [ ] Dependencies are up to date
- [ ] Code has been reviewed for security issues

## Secure Development Guidelines

1. **Input Validation**: Always validate and sanitize user inputs
2. **Error Handling**: Don't expose sensitive information in error messages
3. **Logging**: Be careful not to log sensitive data (API keys, user data, etc.)
4. **Dependencies**: Only use well-maintained, trusted packages
