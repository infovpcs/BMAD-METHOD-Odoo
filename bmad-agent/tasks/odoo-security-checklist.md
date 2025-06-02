# Checklist: Odoo Security Checklist for AI Agent

> **Note:** This checklist should be referenced by all tasks involving Odoo model, module, or controller creation. See [Odoo Security Checklist](../checklists/odoo-security-checklist.md) for details.

## Purpose
This checklist guides an AI agent in performing a comprehensive security review of an Odoo module (versions 17/18), identifying potential vulnerabilities and ensuring adherence to Odoo's security best practices.

## Instructions for AI Agent
When performing a security review of an Odoo module, use the following checks. For each item, analyze the relevant code, configuration, and module setup. Report security compliance or identify specific security risks and propose actionable remediation steps (e.g., code edits, configuration changes).

## Checklist Items

### 1. Access Rights (`ir.model.access.csv`)
- [ ] All custom models have appropriate `ir.model.access.csv` entries (read, write, create, unlink)
- [ ] Record rules (`