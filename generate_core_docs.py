import ast
import os

def get_docstring(node):
    """Safely extracts docstring from an AST node."""
    if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef, ast.Module)):
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            return node.body[0].value.s
    return None

def get_function_signature(node):
    """Extracts a function's signature (name and arguments)."""
    args = [arg.arg for arg in node.args.args]
    if node.args.vararg:
        args.append("*" + node.args.vararg.arg)
    if node.args.kwarg:
        args.append("**" + node.args.kwarg.arg)
    return f"{node.name}({', '.join(args)})"

def parse_module(file_path):
    """Parses a Python module and extracts its documentation details."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        tree = ast.parse(content, filename=file_path)
    except SyntaxError as e:
        print(f"SyntaxError parsing {file_path}: {e}")
        return None

    module_docstring = get_docstring(tree)
    classes = []
    functions = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            if node.name.startswith("_"): # Skip private classes
                continue
            class_docstring = get_docstring(node)
            methods = []
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if item.name.startswith("_") and not item.name.startswith("__"): # Skip protected, allow dunder
                        continue
                    method_signature = get_function_signature(item)
                    method_docstring = get_docstring(item)
                    methods.append({
                        "name": item.name,
                        "signature": method_signature,
                        "docstring": method_docstring or "(Brak docstringu)"
                    })
            classes.append({
                "name": node.name,
                "docstring": class_docstring or "(Brak docstringu)",
                "methods": methods
            })
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("_"): # Skip private functions
                continue
            func_signature = get_function_signature(node)
            func_docstring = get_docstring(node)
            functions.append({
                "name": node.name,
                "signature": func_signature,
                "docstring": func_docstring or "(Brak docstringu)"
            })

    return {
        "docstring": module_docstring or "(Brak docstringu modułu)",
        "classes": classes,
        "functions": functions
    }

def generate_markdown_for_module(module_name, module_data, base_path="core"):
    """Generates Markdown content for a single module."""
    md_content = []

    # Generate anchors for TOC
    module_anchor = module_name.replace('.', '_')

    md_content.append(f"## `{module_name}`")
    md_content.append(module_data["docstring"])
    md_content.append("")

    if module_data["classes"]:
        md_content.append(f"### <a name=\"klasy-{module_anchor}\"></a>Klasy")
        for class_info in module_data["classes"]:
            md_content.append(f"#### `{class_info['name']}`")
            md_content.append(class_info["docstring"])
            if class_info["methods"]:
                md_content.append("##### Metody")
                for method_info in class_info["methods"]:
                    md_content.append(f"- `{method_info['signature']}`: {method_info['docstring']}")
            md_content.append("")

    if module_data["functions"]:
        md_content.append(f"### <a name=\"funkcje-{module_anchor}\"></a>Funkcje")
        for func_info in module_data["functions"]:
            md_content.append(f"- `{func_info['signature']}`: {func_info['docstring']}")
        md_content.append("")

    return "\n".join(md_content)

def main():
    core_dir = "core"
    output_file = "CORE_DOCUMENTATION.md"

    all_modules_data = {}
    module_order = []

    for root, dirs, files in os.walk(core_dir):
        # Skip specific subdirectories like migrations or prompts
        dirs[:] = [d for d in dirs if d not in ["migrations", "prompts", "tree", "info"]]

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                # Construct module name relative to core_dir
                relative_path = os.path.relpath(file_path, core_dir)
                module_name_parts = list(os.path.splitext(relative_path)[0].split(os.sep))

                # Handle __init__.py as package docstring
                if module_name_parts[-1] == "__init__":
                    module_name_parts.pop() # Remove __init__
                    if not module_name_parts: # Root __init__.py in core
                        module_name = "core"
                    else:
                         module_name = "core." + ".".join(module_name_parts)
                else:
                    module_name = "core." + ".".join(module_name_parts)

                if not module_name: # Should not happen with current logic
                    continue

                print(f"Processing: {file_path} as {module_name}")
                module_data = parse_module(file_path)
                if module_data:
                    # If it's an __init__.py, its docstring is for the package
                    # If other data exists (classes/functions in __init__), store it.
                    if file.endswith("__init__.py"):
                        if module_name in all_modules_data:
                            # Merge docstring if package already processed (e.g. other files in package)
                             all_modules_data[module_name]["docstring"] = module_data["docstring"]
                             all_modules_data[module_name]["classes"].extend(module_data["classes"])
                             all_modules_data[module_name]["functions"].extend(module_data["functions"])
                        else:
                            all_modules_data[module_name] = module_data
                        if module_name not in module_order:
                             module_order.append(module_name)
                    else:
                        # For regular .py files, ensure their parent package is in order if not already
                        package_name_parts = module_name_parts[:-1]
                        parent_package_name = "core"
                        if package_name_parts:
                             parent_package_name = "core." + ".".join(package_name_parts)

                        if parent_package_name not in module_order and parent_package_name != module_name :
                             module_order.append(parent_package_name)
                             if parent_package_name not in all_modules_data:
                                 # Add placeholder for parent package if it was not an __init__.py itself
                                 all_modules_data[parent_package_name] = {
                                     "docstring": "(Dokumentacja pakietu)",
                                     "classes": [],
                                     "functions": []
                                 }

                        all_modules_data[module_name] = module_data
                        if module_name not in module_order:
                            module_order.append(module_name)


    # Sort modules: put parent packages first, then modules within them
    def sort_key(m_name):
        parts = m_name.split('.')
        # Ensure 'core' (if it exists as a module entry) comes first
        if m_name == "core":
            return (0, 0)
        # Then sort by number of parts (depth), then alphabetically
        return (len(parts), parts)

    module_order = sorted(list(all_modules_data.keys()), key=sort_key)


    # Generate Table of Contents
    toc = ["# Dokumentacja folderu `core`", "## Spis treści"]
    for module_name in module_order:
        if module_name not in all_modules_data: # Should not happen
            continue

        module_anchor = module_name.replace('.', '_')
        toc.append(f"- [{module_name}](#{module_anchor})")

        # Add sub-links for classes and functions if they exist
        # Need to check all_modules_data[module_name] as it might be just a package docstring
        if all_modules_data[module_name]["classes"]:
            toc.append(f"  - [Klasy](#klasy-{module_anchor})")
        if all_modules_data[module_name]["functions"]:
            toc.append(f"  - [Funkcje](#funkcje-{module_anchor})")

    toc.append("\n---")

    # Generate main content
    markdown_content = ["\n".join(toc)]
    for module_name in module_order: # Iterate in sorted order
        if module_name in all_modules_data:
             anchor_name = module_name.replace('.', '_')
             # Add main anchor for the module section title
             markdown_content.append(f"\n---\n<a name=\"{anchor_name}\"></a>")
             markdown_content.append(generate_markdown_for_module(module_name, all_modules_data[module_name]))
        else:
            # This case should ideally be handled by ensuring all module_order entries exist in all_modules_data
            print(f"Warning: Module {module_name} found in order but not in data. Skipping.")


    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_content))

    print(f"Dokumentacja została wygenerowana: {output_file}")

if __name__ == "__main__":
    main()
