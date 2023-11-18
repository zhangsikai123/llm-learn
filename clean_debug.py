import re
import sys


def remove_debug_code(file_path):
    if file_path.strip() == "clean_debug.py":
        return
    try:
        with open(file_path, "r") as file:
            content = file.read()

        import_pdb_pattern = r"\bimport\s+pdb\b"
        set_trace_pattern = r"\bpdb\.set_trace\(\)"

        # Find occurrences of "import pdb"
        import_pdb_matches = re.findall(import_pdb_pattern, content)
        # Find occurrences of "pdb.set_trace()"
        set_trace_matches = re.findall(set_trace_pattern, content)

        if not import_pdb_matches and not set_trace_matches:
            print("no debug code found.")
            return

        # Use regular expressions to remove "" and ""
        cleaned_content = re.sub(r"import pdb", "", content)
        cleaned_content = re.sub(r"pdb\.set_trace\(\)", "", cleaned_content)
        # Write cleaned content back to the file
        with open(file_path, "w") as file:
            file.write(cleaned_content)

        print(f"Debug code removed from {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


if __name__ == "__main__":
    file_path = sys.argv[1]
    print(file_path)
    remove_debug_code(file_path)
