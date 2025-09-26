import os 
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(abs_work, file_path))
    
    # check if the target file is in or is the working directory
    if not (abs_target.startswith(abs_work + os.sep) or abs_target == abs_work):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'  
    if not os.path.exists(abs_target):
        return f'Error: File "{file_path}" not found.'
    if not abs_target.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        commands = [sys.executable, abs_target]
        process = subprocess.run(
            args= commands.extend(args), 
            capture_output=True, 
            text=True,
            timeout=30,
        )
        
        output = []
        if process.stdout:
            stdout = f"STDOUT: {process.stdout}"
            output.append(stdout)
        if process.stderr:
            stderr = f"STDERR: {process.stderr}"
            output.append(stderr)
        if process.returncode != 0:
            return f"{stdout}\n{stderr}\nProcess exited with code{process.returncode}"

        return "\n".join(output) if output else "No output produced"
    except Exception as e:
        return f"Error: executing Python file: {e}"
