# The BMAD-Method 3.1 (Breakthrough Method of Agile (ai-driven) Development)

## Do This First, and all will make sense!

There are lots of docs here, but I HIGHLY suggest you just try the Web Agent - it takes just a few minutes to set up in Gemini - and you can use the BMad Agent to explain how this method works, how to set up in the IDE, how to set up in the Web, what should be done in the web or ide (although you can choose your own path also!) - all just by talking to the bmad agent!

### Web Quickstart Project Setup (Recommended)

The Agent Orchestrator in V3 utilizes a build script to package various agent assets (personas, tasks, templates, etc.) into a structured format, primarily for use with web-based orchestrator agents that can leverage large context windows. This process involves consolidating files from specified source directories into bundled text files and preparing a main agent prompt.

You can use either the Node.js or Python version of the build script.

**Using the Node.js Build Script:**
1. Ensure you have Node.js installed.
2. Run the script from the project root:
   ```sh
   node build-web-agent.js
   ```

**Using the Python Build Script:**
1. Ensure you have Python 3.6+ installed.
2. Install required Python dependencies (if any - currently none for the script itself, but your config might require `PyYAML` if you use YAML configs):
   ```sh
   pip install pyyaml # if needed for config file
   ```
3. Run the script from the project root:
   ```sh
   python build-web-agent.py
   ```

Both scripts will read the configuration from `build-web-agent.cfg.js` (for Node.js) or `build-web-agent.cfg.py` (for Python), process files from the asset directory (`bmad-agent/`), and output the bundled assets into the specified build directory (`bmad-agent/build/`). The output will include:

- `agent-prompt.txt`: The main orchestrator prompt.
- `agent-config.txt`: The agent configuration parsed from `web-bmad-orchestrator-agent.cfg.md`.
- Bundled `.txt` files for each asset subdirectory (e.g., `personas.txt`, `tasks.txt`).

These files are then ready to be used by the Web Agent (like Google Gems or customGPTs).

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

## Project Scaffolding Script

To quickly set up a new project directory with the necessary BMAD agent structure, or update an existing one, you can use the `scaffold_bmad_project.py` script.

**Purpose:** Creates a new project folder and copies the `bmad-agent` directory (containing all personas, tasks, templates, etc.) and an empty `docs` directory into it. If the directory already exists and the `--update` flag is used, it will update the `bmad-agent` and `docs` structure within the existing folder.

**Usage:**
1.  Ensure you have Python 3.6+ installed.
2.  Run the script from the root directory of the **cloned BMAD-METHOD-Odoo repository** (the one containing the `scaffold_bmad_project.py` file).
3.  Provide the name for your project directory as a command-line argument.

    -   **To scaffold a NEW project:**
        ```sh
        python scaffold_bmad_project.py your-new-project-name
        ```
        Replace `your-new-project-name` with the desired name for your new project folder. This will fail if the directory already exists.

    -   **To UPDATE an EXISTING project structure:**
        ```sh
        python scaffold_bmad_project.py your-existing-project-name --update
        ```
        Replace `your-existing-project-name` with the name of the project directory you want to update. This will copy/overwrite the `bmad-agent` folder and create the `docs` folder if it doesn't exist.

**What the script does:**
- Creates a directory with the specified name in the same location as the script **(only if not using --update)**.
- Copies the entire `bmad-agent` folder from the current repository into your project directory. If the directory exists and `--update` is used, it copies into the existing directory.
- Creates an empty `docs` folder in your project directory. If the directory exists and `--update` is used, it creates the `docs` folder if it doesn't already exist within the existing directory.

**Next Steps After Scaffolding:**
1.  **Navigate to your new project directory:**
    ```sh
    cd your-new-project-name
    ```
2.  **Generate Initial Documentation (Web Agent):** Use your configured web-based AI agent (e.g., Google Gems) to generate core project documents like `PRD.md` and `architecture.md` for your new project.
3.  **Manually Add Docs:** Save the generated `PRD.md` and `architecture.md` files into the `docs` folder within your new project directory.
4.  **Continue with IDE Agent:** Open your new project folder (`your-new-project-name`) in your IDE. Activate the `ide-bmad-orchestrator.md` agent located at `/bmad-agent/ide-bmad-orchestrator.md` within your new project. The IDE agent will now have access to all BMAD assets and your core documentation to continue the workflow (e.g., creating stories, scaffolding code, running checklists).

This script streamlines the initial setup, allowing you to quickly get a new project ready to leverage the full BMAD workflow.

---

## End Matter

Interested in improving the BMAD Method? See the [contributing guidelines](docs/CONTRIBUTING.md).

This project is maintained by VPerfectCS and the open source community. We welcome contributions from all Odoo developers and enthusiasts.

Thank you for supporting the Odoo community and helping us build better tools for everyone!

[License (MIT, Community & VPerfectCS)](docs/LICENSE)
