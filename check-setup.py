import os
import sys
import pkg_resources


def check_project_structure():
    print("=== Project Structure Check ===")
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")

    # Check directory contents
    print("\nDirectory contents:")
    for item in os.listdir(current_dir):
        print(f"- {item}")

    # Check package directory
    package_dir = os.path.join(current_dir, "turing_machine")
    if os.path.exists(package_dir):
        print("\nturing_machine directory contents:")
        for item in os.listdir(package_dir):
            print(f"- {item}")
    else:
        print("\nWARNING: turing_machine directory not found!")

    # Check Python path
    print("\nPython path:")
    for path in sys.path:
        print(f"- {path}")

    # Check installed packages
    print("\nInstalled packages:")
    for package in pkg_resources.working_set:
        if "turing" in package.key:
            print(f"- {package.key} version {package.version}")

    # Try importing
    print("\nTrying import...")
    try:
        import turing_machine
        print("Success: imported turing_machine")
        print(f"Module location: {turing_machine.__file__}")
    except ImportError as e:
        print(f"Failed to import: {e}")


if __name__ == "__main__":
    check_project_structure()