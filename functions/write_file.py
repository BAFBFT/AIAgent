import os

def write_file(working_directory, file_path, content):
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(abs_work, file_path))
    
    # check if the target file is in or is the working directory
    if not (abs_target.startswith(abs_work + os.sep) or abs_target == abs_work):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(abs_target): # create file if it doesn't exist
            with open(abs_target, 'x') as f:
                pass
        # overwrite the file
        with open(abs_target, 'w') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"