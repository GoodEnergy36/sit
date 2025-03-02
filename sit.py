import os
from pathlib import Path

import os
from pathlib import Path

def create_sit_data(sit_data_path):
    try:
        os.makedirs(sit_data_path, exist_ok=False)
        return 0
    except OSError as error:
        print(f"Error creating directory '{sit_data_path}': {error}")
        return 1

def init_sit():
    init_file_path = os.path.join(Path.cwd(), ".sit")
    
    # Check if project already exists
    if os.path.exists(init_file_path):
        print("sit project already exists in this directory")
        return 1
    
    # Define the data directory path
    sit_data_path = os.path.join(Path(__file__).parent.resolve(), "sit_data")
    
    # Create data directory if needed
    if not os.path.exists(sit_data_path):
        if create_sit_data(sit_data_path):
            return 1
    
    # Create the .sit file
    try:
        open(init_file_path, "w").close()
        return 0
    except OSError as error:
        print(f"Error creating .sit file: {error}")
        return 1
    
def _write_sit():
    pass
    
def write_sit():
    init_file_path = os.path.join(Path.cwd(), ".sit")
    if not os.path.exists(init_file_path):
        print("sit project does not exists in this directory")
        return 1
    else:
        _write_sit()
        return 0

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Project attempting to write git from first principals called sit (sam-git)")
    parser.add_argument("--init", action="store_true", help="Create a new sit project")
    parser.add_argument("--write", action="store_true", help="Write changes to project to sit")
    
    args = parser.parse_args()
    
    if args.init and args.write:
        exit(1)
    
    if args.init:
        exit(init_sit())

    if args.write:
        exit(write_sit())
    
