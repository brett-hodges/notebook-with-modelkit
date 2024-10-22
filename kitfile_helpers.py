import yaml
from datetime import datetime, timezone
from pathlib import Path

# Helper function to print the contents of the python dictionary object
# representing the project's Kitfile
def print_kitfile_contents(kitfile):
    print('\n\nKitfile Contents...')
    print('===================\n')
    print(yaml.safe_dump(kitfile, sort_keys=False))

# Helper function to read the project's Kitfile from disk into
# a python dictionary object.
# If the print flag is true, the Kitfile's contents are printed.
def import_kitfile(template = False, print = True) -> dict:
    # Path to kitfile template
    if template:
        kitfile_path = Path("template") / "Kitfile.template"
    else:
        kitfile_path = Path() / "Kitfile"
    # Open the Kitfile template
    with open(kitfile_path, 'r') as file:
        # Load the contents into a Python dictionary
        kitfile = yaml.safe_load(file)
    if print:
        print_kitfile_contents(kitfile)
    return kitfile

# Helper function to export the python dictionary object 
# representing the project's Kitfile to disk.
# If the print flag is true, the Kitfile's contents are printed.
def export_kitfile(kitfile, print = True):
    # Open the Kitfile 
    yaml.safe_dump(kitfile, open('Kitfile', 'w'), sort_keys=False)
    if print:
        print_kitfile_contents(kitfile)

# Helper function to update the Kitfile's Code section with
# details about the code files to include.
# If the replace flag is True, the Code section will 
# be over-written; otherwise, the Code section will be
# updated with the additional Code file(s).
# If the print flag is True, the contents of the updated
# Kitfile are printed.
def update_code_section(kitfile, code, replace = True, print = True):
    if replace:
        kitfile["code"] = code
    else:
        kitfile["code"].extend(code)
    # save the updated Kitfile contents to disk
    export_kitfile(kitfile, print)

# Helper function to update the Kitfile's Datasets section with
# details about the data files to include.
# If the replace flag is True, the Datasets section will 
# be over-written; otherwise, the Datasets section will be
# updated with the additional Datasets.
# If the print flag is True, the contents of the updated
# Kitfile are printed.
def update_datasets_section(kitfile, datasets, replace = True, print = True):
    if replace:
        kitfile["datasets"] = datasets 
    else:
        kitfile["datasets"].extend(datasets)
    # save the updated Kitfile contents to disk
    export_kitfile(kitfile, print)

# Helper function to update the Kitfile's Package section with
# details about the current ModelKit, including the tag name
# to be used when pushing it, and the approximate timestamp
# when the ModelKit is to be pushed.
# If the print flag is True, the contents of the updated
# Kitfile are printed.
def update_package_section(kitfile, tag_name, print = True):
    # Get the current UTC timestamp
    current_utc_timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
    package_section = kitfile["package"]
    description = package_section["description"]
    description += ("\nModelKit tag: " + tag_name + " pushed at: " + current_utc_timestamp)
    package_section["description"] = description
    # save the updated Kitfile contents to disk
    export_kitfile(kitfile, print)

# Helper function to update the Kitfile's Model section with
# details about the trained model to include.
# If the print flag is True, the contents of the updated
# Kitfile are printed.
def update_model_section(kitfile, model_info, print = True):
    kitfile["model"] = model_info
    export_kitfile(kitfile, print)