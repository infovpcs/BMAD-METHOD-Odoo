import os
import yaml
import re

# --- Utility Functions ---

def parse_related_checklists(task_file_path):
    """Extracts the 'Related Checklists' section from a task file."""
    with open(task_file_path, 'r') as f:
        content = f.read()
    match = re.search(r'## Related Checklists\n((?:- .+\n)+)', content)
    if not match:
        return []
    checklist_lines = match.group(1).strip().split('\n')
    return [line.split('](')[0].replace('- [', '').strip() for line in checklist_lines]

def load_checklist_mappings(mapping_file_path):
    with open(mapping_file_path, 'r') as f:
        return yaml.safe_load(f)

def find_doc_in_default_locations(doc_name, default_locations, module_name=None):
    """Tries to find the required doc in the default locations."""
    for loc in default_locations:
        if module_name:
            loc = loc.replace('{module}', module_name)
        candidate = os.path.join(loc, doc_name) if not doc_name.startswith(loc) else doc_name
        if os.path.exists(candidate):
            return candidate
    return None

def run_checklist_runner(checklist_file, docs_to_check):
    """Simulate running a checklist. In reality, you'd parse the checklist and validate each item."""
    print(f"\nRunning checklist: {checklist_file}")
    print(f"Validating docs: {docs_to_check}")
    # Simulate: just print the checklist items
    with open(checklist_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.strip().startswith('- ['):
            print(line.strip())
    print("Checklist validation complete.\n")
    return True

# --- Main Orchestrator Logic ---

def run_checklists_for_task(task_file_path, mapping_file_path, module_name=None):
    related_checklists = parse_related_checklists(task_file_path)
    mappings = load_checklist_mappings(mapping_file_path)
    for checklist_name in related_checklists:
        key = checklist_name.lower().replace(' ', '-')
        if key not in mappings:
            print(f"Checklist '{checklist_name}' not found in mappings.")
            continue
        mapping = mappings[key]
        checklist_file = mapping['checklist_file']
        required_docs = mapping.get('required_docs', [])
        default_locations = mapping.get('default_locations', [])
        docs_to_check = []
        for doc in required_docs:
            found = find_doc_in_default_locations(doc, default_locations, module_name)
            if found:
                docs_to_check.append(found)
            else:
                docs_to_check.append(f"NOT FOUND: {doc}")
        run_checklist_runner(checklist_file, docs_to_check)

# --- Example Usage ---

if __name__ == "__main__":
    # Example: Validate after creating a model in 'my_module'
    task_file = "bmad-agent/tasks/create-odoo-model.md"
    mapping_file = "bmad-agent/tasks/checklist-mappings.yml"
    module_name = "my_module"  # Replace with actual module if needed
    run_checklists_for_task(task_file, mapping_file, module_name) 