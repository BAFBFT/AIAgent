import os
from config import MAX_CHARS

def get_files_info(working_directory, directory="."):
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(abs_work, directory))
    
    # check if the target directory is in or is the working directory
    if not (abs_target.startswith(abs_work + os.sep) or abs_target == abs_work):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_target):
        return f'Error: "{directory}" is not a directory'
    
    try: # get info on the files in the target directory
        names = sorted(os.listdir(abs_target))
        formatted = []
        for name in names:
            full_path = os.path.join(abs_target, name)
            s = f"- {name}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}"
            formatted.append(s)
    except Exception as e:
        return f"Error: {e}"
    
    return "\n".join(formatted)

def get_file_content(working_directory, file_path):
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(abs_work, file_path))
    
    # check if the target file is in or is the working directory
    if not (abs_target.startswith(abs_work + os.sep) or abs_target == abs_work):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'  
    if not os.path.isfile(abs_target):
        return f'Error: File not found or is not a regular file "{file_path}"'
    
    try:
        with open(file_path, "r") as f:
            if len(f.read()) > MAX_CHARS:
                file_content_string = f.read(MAX_CHARS)
                file_content_string.append(f'[...File "{file_path}" truncated at {MAX_CHARS} characters]')
            else:
                file_content_string = f.read()
    except Exception as e:
        return f"Error: {e}"

    return file_content_string