import sys


def reorder_imports(input_file, output_file):
    # Open the input file for reading
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Check if the imports are already at the top
    imports_at_top = True
    counter = []
    for i, line in enumerate(lines):
        if line.strip().startswith("import ") or line.strip().startswith("from "):
            # Found a non-import line, imports are not at the top
            counter.append(i)
    if lines and counter[0] != 0:
        imports_at_top = False
    for i, line in enumerate(lines):
        if (
            i >= counter[0]
            and i <= counter[-1]
            and not line.strip().startswith("import ")
            and not line.strip().startswith("from ")
            and not line.strip() == ""
        ):
            print(line)
            imports_at_top = False
            break

    if imports_at_top:
        print("Imports are already at the top. No reordering needed.")
        return

    print(f"Reordering imports {input_file} ...")
    # Separate import lines and other lines
    import_lines = []
    other_lines = []

    for line in lines:
        if line.strip().startswith("import ") or line.strip().startswith("from "):
            import_lines.append(line)
        else:
            other_lines.append(line)

    # Combine import lines and other lines
    reordered_lines = import_lines + other_lines

    # Open the output file for writing and save the reordered code
    with open(output_file, "w") as file:
        file.writelines(reordered_lines)


if __name__ == "__main__":
    input_file = sys.argv[1]
    reorder_imports(input_file, input_file)
