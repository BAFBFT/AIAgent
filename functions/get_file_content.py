import os
from functions.config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of a file, readable files are constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path for reading, relative to the working directory.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(abs_work, file_path))
    
    # check if the target file is in or is the working directory
    if not (abs_target.startswith(abs_work + os.sep) or abs_target == abs_work):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'  
    if not os.path.isfile(abs_target):
        return f'Error: File not found or is not a regular file "{file_path}"'
    
    try:
        with open(abs_target, "r") as f:
            file = f.read()
            if len(file) > MAX_CHARS:
                file_content_string = file[:MAX_CHARS + 1] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            else:
                file_content_string = file
    except Exception as e:
        return f"Error: {e}"
    
    return file_content_string