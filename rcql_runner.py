import re
from pathlib import Path

def parse_rcql(file_path):
    """
    Parses an RCQL file and returns a list of task dictionaries.
    Each directive like Contain, Recall, Reflect, etc., becomes a key in the task dict.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    rcql_blocks = []
    current_block = {}
    directive_pattern = re.compile(r'^(Contain|Recall|Reflect|Intend|Consent|Yield|FailSafe|Validate):\s*(.*)', re.IGNORECASE)

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue  # Skip comments and blank lines

        match = directive_pattern.match(line)
        if match:
            key, value = match.groups()
            key = key.capitalize()
            if key == "Contain" and current_block:
                rcql_blocks.append(current_block)
                current_block = {}
            current_block[key] = value
    if current_block:
        rcql_blocks.append(current_block)

    return rcql_blocks

def main():
    import argparse
    parser = argparse.ArgumentParser(description="RCQL Runner - Parse and display RCQL task blocks")
    parser.add_argument("file", help="Path to your RCQL file")
    args = parser.parse_args()

    tasks = parse_rcql(args.file)
    for i, task in enumerate(tasks, 1):
        print(f"\n--- Task Block {i} ---")
        for key, value in task.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
