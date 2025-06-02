# Checklist: Odoo Security Checklist for AI Agent

## Purpose
This checklist guides an AI agent in performing a comprehensive security review of an Odoo module (versions 17/18), identifying potential vulnerabilities and ensuring adherence to Odoo's security best practices.

## Instructions for AI Agent
When performing a security review of an Odoo module, use the following checks. For each item, analyze the relevant code, configuration, and module setup. Report security compliance or identify specific security risks and propose actionable remediation steps (e.g., code edits, configuration changes).

## Checklist Items

### 1. Access Rights (`ir.model.access.csv`)
- [ ] All custom models have explicit `ir.model.access.csv` entries.
- [ ] Access rights (read, write, create, unlink) are set to the least privilege necessary for each user group.
- [ ] Default access (if any) for `base.group_user` and `base.group_public` is reviewed and restricted as needed.
- [ ] No over-permissive access rules for sensitive models/fields.

### 2. Record Rules (`ir.rule`)
- [ ] Record rules are implemented for multi-company, multi-user, or data segregation requirements.
- [ ] Rules are correctly defined with `domain_force` for proper data filtering based on user context or record ownership.
- [ ] Rules are attached to the correct `groups`.
- [ ] Rules account for inheritance and potential conflicts with base rules.

### 3. `sudo()` Usage
- [ ] `sudo()` calls are minimized and explicitly justified with an inline `# Reason:` comment.
- [ ] `sudo()` is used only when elevated privileges are strictly necessary for a specific operation (e.g., system-level actions, background jobs).
- [ ] `sudo()` is applied to the smallest possible scope (e.g., `record.sudo().write(...)` instead of `self.sudo().write(...)` if only one record needs sudo).
- [ ] `sudo()` is not used for direct user input operations without prior validation and sanitization.

### 4. Controller Security (HTTP Routes)
- [ ] HTTP routes (`@http.route`) have appropriate `auth` settings (`public`, `user`, `none`).
- [ ] Public routes handle input validation and sanitization to prevent injection attacks (SQL, XSS, etc.).
- [ ] Sensitive operations in controllers require `auth='user'` and are further protected by appropriate security groups.
- [ ] CSRF protection is enabled for POST requests (`csrf=True` or default enabled in Odoo 17+), especially for forms, or justified if disabled.
- [ ] File uploads are handled securely (e.g., validate file types, size, scan for malicious content if applicable).

### 5. Data Validation & Sanitization
- [ ] All user input, especially for `Char`, `Text`, `Html` fields, is validated and sanitized on the backend to prevent injection attacks.
- [ ] Use of `t-esc` in QWeb templates is preferred over `t-out` for user-generated content to prevent XSS.
- [ ] Parameters used in raw SQL queries (`self.env.cr.execute`) are properly parameterized to prevent SQL injection.

### 6. Hardcoded Credentials & Secrets
- [ ] No hardcoded API keys, passwords, sensitive tokens, or other secrets are present in the code.
- [ ] Configuration for external services uses Odoo's system parameters (`ir.config_parameter`) or dedicated settings models.

### 7. Logging & Error Handling
- [ ] Sensitive information is not logged unnecessarily (e.g., full credit card numbers, passwords).
- [ ] Error messages do not expose sensitive system details or stack traces to end-users.

### 8. Session Management
- [ ] Session cookies are properly secured (HTTPOnly, Secure flags).
- [ ] Inactive sessions are appropriately timed out.

### 9. External Module & Library Review
- [ ] All third-party libraries and external Odoo modules used are from trusted sources.
- [ ] Known vulnerabilities in dependencies are addressed (e.g., by updating to secure versions).

## Reference
Refer to Odoo's official security guidelines, OWASP Top 10, and specific Odoo 17/18 security best practices for detailed information.

See Odoo-specific security best practices and version notes in [Odoo KB](../data/odoo-kb.md). 