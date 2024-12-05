import os


def get_input_file_path(module_file: str, input_file_path: str = "input.txt") -> str:
    current_file_path = os.path.abspath(module_file)
    parent_directory = os.path.dirname(current_file_path)
    return os.path.join(parent_directory, input_file_path)
