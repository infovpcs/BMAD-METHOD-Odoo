# The BMAD-Method 3.1 (Breakthrough Method of Agile (ai-driven) Development)

## Do This First, and all will make sense!

There are lots of docs here, but I HIGHLY suggest you just try the Web Agent - it takes just a few minutes to set up in Gemini - and you can use the BMad Agent to explain how this method works, how to set up in the IDE, how to set up in the Web, what should be done in the web or ide (although you can choose your own path also!) - all just by talking to the bmad agent!

### Web Quickstart Project Setup (Recommended)

Orchestrator Uber BMad Agent that does it all - already pre-compiled in the `web-build-sample` folder.

- The contents of [Agent Prompt Sample](web-build-sample/agent-prompt.txt) text get pasted into the Gemini Gem, or ChatPGT customGPT 'Instructions' field.
- The remaining files in that same folder folder just need to be attached as shown in the screenshot below. Give it a name (such as BMad Agent) and save it, and you now have the BMad Agent available to help you brainstorm, research, plan, execute on your vision, or understand how this all even works!
- Once its running, start with typing `/help`, and then type option `2` when it presents 3 options to learn about the method!

![image info](docs/images/gem-setup.png)

[More Documentation, Explanations, and IDE Specifics](docs/readme.md) available here!

## Odoo-Specific Development & Validation

This project supports Odoo 17/18 module development with AI-driven best practices and validation. Follow these steps to use the BMAD Method for Odoo projects:

### 1. Reference Odoo Best Practices
- All Odoo-related development should follow the [Odoo Knowledge Base](bmad-agent/data/odoo-kb.md) for module structure, ORM, security, QWeb, and version-specific notes.

### 2. Use BMAD Agent Personas
- Use the Odoo personas in `bmad-agent/personas/` (backend, frontend, architect, functional consultant) for role-specific guidance.
- For story creation and validation, use the Scrum Master persona (`sm.ide.md`). For development, use the Developer persona (`dev.ide.md`).

### 3. Follow Task Instructions
- For any Odoo module, model, or frontend work, follow the step-by-step instructions in `bmad-agent/tasks/` (e.g., `create-odoo-model.md`, `create-qweb-template.md`).
- Each task file lists "Related Checklists" at the end for validation.

### 4. Validate with Checklists
- After completing a task, run the checklist validation using the Python runner:
  ```sh
  python bmad-agent/checklist_runner.py
  ```
- This will check your work against the relevant QA, security, upgrade, and frontend/website/OWL checklists.
- Edit the last lines of `checklist_runner.py` to specify the task and module you want to validate:
  ```python
  task_file = "bmad-agent/tasks/create-odoo-model.md"
  mapping_file = "bmad-agent/tasks/checklist-mappings.yml"
  module_name = "your_module_name"
  run_checklists_for_task(task_file, mapping_file, module_name)
  ```

### 5. Manual/Automated Testing
- For Odoo modules, use Odoo's built-in test framework:
  - Place tests in the `tests/` folder of your module.
  - Run tests using Odoo's test runner or via command line.

### 6. Documentation & Knowledge Base
- Update `README.md` in your module and project root as needed.
- Expand `bmad-agent/data/odoo-kb.md` with new best practices, version notes, or lessons learned.

### 7. Continuous Improvement
- As you add new tasks, checklists, or templates, keep the mappings and references up to date.
- Encourage contributors to use the checklist runner and reference the Odoo KB.

---

**Quickstart for New Odoo Project (Terminal):**

1. Clone this repo and enter the directory:
   ```sh
   git clone <your-repo-url>
   cd BMAD-METHOD-Odoo
   ```
2. Install Python dependencies:
   ```sh
   pip install pyyaml
   ```
3. Scaffold your Odoo module using templates in `bmad-agent/templates/`.
4. Follow the relevant task file in `bmad-agent/tasks/` for step-by-step instructions.
5. Run the checklist runner to validate your work:
   ```sh
   python bmad-agent/checklist_runner.py
   ```
6. Review the output and address any issues found.
7. Run Odoo tests for your module.
8. Update documentation and the Odoo KB as needed.

For more details, see the Odoo KB and the BMAD agent personas.

## End Matter

Interested in improving the BMAD Method? See the [contributing guidelines](docs/CONTRIBUTING.md).

This project is maintained by VPerfectCS and the open source community. We welcome contributions from all Odoo developers and enthusiasts.

Thank you for supporting the Odoo community and helping us build better tools for everyone!

[License (MIT, Community & VPerfectCS)](docs/LICENSE)
