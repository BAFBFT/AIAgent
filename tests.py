from functions.run_python_file import run_python_file

print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))

# print("Result for '/bin' directory:")
# print(get_files_info("calculator", "/bin"))
# print("Result for '../' directory:")
# print(get_files_info("calculator", "../"))

