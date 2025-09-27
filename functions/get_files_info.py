import os
from google import genai
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

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


