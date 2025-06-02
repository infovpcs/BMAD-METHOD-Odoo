import os
import sys
import glob

# --- Configuration ---
# Assuming config is in a Python file named build-web-agent.cfg.py
config_file_path = os.path.join(os.path.dirname(__file__), 'build-web-agent.cfg.py')

config = {}
try:
    with open(config_file_path, 'r') as f:
        exec(f.read(), {}, config)
except FileNotFoundError:
    print(f"Error loading configuration file '{config_file_path}': File not found.", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error loading configuration file '{config_file_path}': {e}", file=sys.stderr)
    sys.exit(1)

# --- Helper Functions ---
def get_base_filename(file_path):
    filename_with_ext = os.path.basename(file_path)
    name, ext = os.path.splitext(filename_with_ext)
    return name

def ensure_directory_exists(dir_path):
    os.makedirs(dir_path, exist_ok=True)

# --- Main Script Logic ---
def main():
    print(f"Loading configuration from: {os.path.abspath(config_file_path)}")

    required_keys = ['asset_root', 'build_dir', 'orchestrator_agent_prompt', 'agent_cfg']
    for key in required_keys:
        if key not in config:
            print(f"Error: Missing required field ('{key}') in configuration file.", file=sys.stderr)
            sys.exit(1)

    # 2. Determine and validate asset folder root and build directory
    asset_folder_root_input = config['asset_root']
    asset_folder_root = os.path.join(os.path.dirname(__file__), asset_folder_root_input)
    if not os.path.exists(asset_folder_root) or not os.path.isdir(asset_folder_root):
        print(f"Error: Asset folder root '{asset_folder_root_input}' (resolved to '{os.path.abspath(asset_folder_root)}') not found or not a directory.", file=sys.stderr)
        sys.exit(1)
    print(f"Using resolved asset folder root: {os.path.abspath(asset_folder_root)}")

    build_dir_input = config['build_dir']
    build_dir = os.path.join(os.path.dirname(__file__), build_dir_input)
    ensure_directory_exists(build_dir)
    print(f"Build directory is: {os.path.abspath(build_dir)}")

    build_dir_name_only = os.path.basename(build_dir)

    # 3. Generate agent-prompt.txt
    orchestrator_prompt_path_input = config['orchestrator_agent_prompt']
    orchestrator_prompt_path = os.path.join(os.path.dirname(__file__), orchestrator_prompt_path_input)
    if not os.path.exists(orchestrator_prompt_path) or not os.path.isfile(orchestrator_prompt_path):
        print(f"Error: Orchestrator agent prompt file '{orchestrator_prompt_path_input}' (resolved to '{os.path.abspath(orchestrator_prompt_path)}') not found or not a file.", file=sys.stderr)
        sys.exit(1)

    agent_prompt_output_path = os.path.join(build_dir, 'agent-prompt.txt')
    try:
        with open(orchestrator_prompt_path, 'r', encoding='utf-8') as infile:
            prompt_content = infile.read()
        with open(agent_prompt_output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(prompt_content)
        print(f"\nSuccessfully generated '{os.path.abspath(agent_prompt_output_path)}'")
    except Exception as e:
        print(f"Error generating '{os.path.abspath(agent_prompt_output_path)}': {e}", file=sys.stderr)
        sys.exit(1)

    # NEW STEP: Copy agent_cfg to build_dir as agent-config.txt
    agent_config_path_input = config['agent_cfg']
    agent_config_path = os.path.join(os.path.dirname(__file__), agent_config_path_input)
    if not os.path.exists(agent_config_path) or not os.path.isfile(agent_config_path):
        print(f"Error: Agent config file '{agent_config_path_input}' (resolved to '{os.path.abspath(agent_config_path)}') not found or not a file.", file=sys.stderr)
        sys.exit(1)

    agent_config_output_path = os.path.join(build_dir, 'agent-config.txt')
    try:
        with open(agent_config_path, 'r', encoding='utf-8') as infile:
            config_content = infile.read()
        with open(agent_config_output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(config_content)
        print(f"\nSuccessfully copied agent configuration to '{os.path.abspath(agent_config_output_path)}'")
    except Exception as e:
        print(f"Error copying agent configuration to '{os.path.abspath(agent_config_output_path)}': {e}", file=sys.stderr)
        sys.exit(1)

    # 4. Discover subdirectories to process from asset_root
    print(f"\nDiscovering source directories in '{os.path.abspath(asset_folder_root)}' (excluding '{build_dir_name_only}')...")
    source_subdir_names = [
        d for d in os.listdir(asset_folder_root)
        if os.path.isdir(os.path.join(asset_folder_root, d)) and d != build_dir_name_only
    ]

    if not source_subdir_names:
        print(f"Warning: No source subdirectories found in '{os.path.abspath(asset_folder_root)}' (excluding '{build_dir_name_only}'). No asset bundles will be created.")
    else:
        print(f"Found source directories to process: {', '.join(source_subdir_names)}")

    # 5. Perform pre-check for duplicate base filenames in each discovered subdirectory
    print("Performing pre-check for duplicate base filenames...")
    for subdir_name in source_subdir_names:
        source_subdir_path = os.path.join(asset_folder_root, subdir_name)
        try:
            files = [f for f in os.listdir(source_subdir_path) if os.path.isfile(os.path.join(source_subdir_path, f))]
            if not files:
                print(f"  Directory '{os.path.abspath(source_subdir_path)}' is empty. No duplicates possible.")
                continue

            print(f"  Checking for duplicates in '{os.path.abspath(source_subdir_path)}'...")
            base_filenames_seen = {}

            for filename_with_ext in files:
                file_path = os.path.join(source_subdir_path, filename_with_ext)
                base_name = get_base_filename(filename_with_ext)

                if base_name in base_filenames_seen:
                    print(f"Error: Duplicate base name '{base_name}' found in directory '{os.path.abspath(source_subdir_path)}'.", file=sys.stderr)
                    print(f"       Conflicting files: '{base_filenames_seen[base_name]}' and '{filename_with_ext}'.", file=sys.stderr)
                    print("       Please ensure all files in a subdirectory have unique names after removing their last extensions.", file=sys.stderr)
                    sys.exit(1)
                else:
                    base_filenames_seen[base_name] = filename_with_ext

            print(f"    No duplicates found in '{os.path.abspath(source_subdir_path)}'.")
        except Exception as e:
            print(f"Warning: Could not read directory '{os.path.abspath(source_subdir_path)}' during pre-check. {e}", file=sys.stderr)

    print("Pre-check completed. No critical duplicate base filenames found (or directories were empty/unreadable).")

    # 6. Main processing loop for discovered subdirectories
    for subdir_name in source_subdir_names:
        source_subdir_path = os.path.join(asset_folder_root, subdir_name)
        output_bundle_path = os.path.join(build_dir, f'{subdir_name}.txt')
        print(f"\nProcessing directory '{os.path.abspath(source_subdir_path)}'...")

        try:
            files_to_bundle = sorted([ # Sort files for consistent output order
                f for f in os.listdir(source_subdir_path)
                if os.path.isfile(os.path.join(source_subdir_path, f))
                and '.ide.' not in f # Skip files with .ide. in the name
            ])

            if not files_to_bundle:
                print(f"  No files (excluding *.ide.*) found in '{os.path.abspath(source_subdir_path)}'. Skipping bundle creation.")
                continue

            print(f"  Files to bundle: {', '.join(files_to_bundle)}")

            with open(output_bundle_path, 'w', encoding='utf-8') as outfile:
                for filename in files_to_bundle:
                    file_path = os.path.join(source_subdir_path, filename)
                    base_name = get_base_filename(filename)
                    outfile.write(f"==================== START: {base_name} ====================\n")
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                        outfile.write("\n") # Ensure a newline after each file content
                    except Exception as e:
                        print(f"Error reading file '{os.path.abspath(file_path)}': {e}", file=sys.stderr)
                        # Continue processing other files but log the error

                    outfile.write(f"==================== END: {base_name} ====================\n\n")

            print(f"Successfully created bundle: '{os.path.abspath(output_bundle_path)}'")

        except Exception as e:
            print(f"Error processing directory '{os.path.abspath(source_subdir_path)}': {e}", file=sys.stderr)
            sys.exit(1)

    print("\nBuild process completed.")

if __name__ == "__main__":
    main() 