#!/usr/bin/env python3
import os
import sys
import shutil
import argparse

def main():
    parser = argparse.ArgumentParser(description='Scaffold or update a project with BMAD agent structure.')
    parser.add_argument('project_name', help='The name of the project directory.')
    parser.add_argument('--update', action='store_true', help='Allow updating an existing project structure instead of creating a new one.')
    args = parser.parse_args()

    new_project_name = args.project_name
    current_dir = os.path.dirname(os.path.abspath(__file__))
    new_project_path = os.path.join(current_dir, new_project_name)

    # Check if the destination directory already exists
    if os.path.exists(new_project_path):
        if args.update:
            print(f"Directory '{new_project_name}' already exists at '{new_project_path}'. Updating project structure.")
        else:
            print(f"Error: Directory '{new_project_name}' already exists at '{new_project_path}'. Use --update to modify existing structure.", file=sys.stderr)
            sys.exit(1)
    elif args.update:
         print(f"Error: Directory '{new_project_name}' does not exist at '{new_project_path}'. Cannot update a non-existent project.", file=sys.stderr)
         sys.exit(1)
    else:
        print(f"Scaffolding new project: '{new_project_name}' at '{new_project_path}'")
        try:
            # Create the new project directory
            os.makedirs(new_project_path)
            print(f"Created project directory: '{new_project_path}'")
        except Exception as e:
            print(f"Error creating project directory: {e}", file=sys.stderr)
            sys.exit(1)

    try:
        # Define source and destination paths
        bmad_agent_source = os.path.join(current_dir, 'bmad-agent')
        bmad_agent_dest = os.path.join(new_project_path, 'bmad-agent')
        docs_dest = os.path.join(new_project_path, 'docs')

        # Copy the bmad-agent directory
        if os.path.exists(bmad_agent_source) and os.path.isdir(bmad_agent_source):
            print(f"Copying '{bmad_agent_source}' to '{bmad_agent_dest}'...")
            # Use dirs_exist_ok=True when updating
            shutil.copytree(bmad_agent_source, bmad_agent_dest, dirs_exist_ok=args.update)
            print("bmad-agent directory copied.")
        else:
            print(f"Warning: Source '{bmad_agent_source}' not found or not a directory. Skipping bmad-agent copy.", file=sys.stderr)

        # Create an empty docs directory
        print(f"Creating docs directory at '{docs_dest}'...")
        # Use exist_ok=True when updating
        os.makedirs(docs_dest, exist_ok=args.update)
        print("docs directory created.")

        if args.update:
             print(f"\nProject '{new_project_name}' updated successfully.")
        else:
            print(f"\nProject '{new_project_name}' scaffolded successfully.")

        print(f"Navigate to the directory (cd {new_project_name}) to start.")
        if not args.update:
            print("Remember to manually add your initial PRD.md and architecture.md to the docs folder.")

    except Exception as e:
        print(f"Error during project process: {e}", file=sys.stderr)
        # Clean up partially created directory only if it was a new scaffolding and an error occurred before full creation
        if not args.update and os.path.exists(new_project_path) and not os.path.exists(os.path.join(new_project_path, 'bmad-agent')):
            print(f"Cleaning up partial directory '{new_project_path}'...")
            shutil.rmtree(new_project_path)
        sys.exit(1)

if __name__ == "__main__":
    main() 