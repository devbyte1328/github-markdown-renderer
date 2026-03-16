from Standards import *
import os
import subprocess


PATH_OF_HOME_USER = OS_return_path_of_home_user()
PATH_OF_MARKDOWN_DIRECTORY = f"{PATH_OF_HOME_USER}/.markdown"
PATH_OF_BASHRC_SCRIPT = f"{PATH_OF_HOME_USER}/.bashrc"
PATH_OF_PYTHON_SCRIPT = OS_return_absolute_path("Main.py")


SubProcess_Initialize(f"mdbook init ~/.markdown --title \"Github Markdown Renderer\" --ignore=none --force > /dev/null 2>&1")
SubProcess_Initialize(f"cp STANDARDS.md ~/.markdown/")
SubProcess_Initialize(f"cp Standards.py ~/.markdown/")
SubProcess_Initialize(f"cp Main.py ~/.markdown/")
if OS_return_boolean_directory(PATH_OF_MARKDOWN_DIRECTORY) == False:
    OS_initialize_directory(PATH_OF_MARKDOWN_DIRECTORY)
bashrc_script = ""
if OS_return_boolean_filesystem(PATH_OF_BASHRC_SCRIPT) == True:
    bashrc_script = Python_read_file(PATH_OF_BASHRC_SCRIPT)
bashrc_function = Python_fstring(f"""

markdown() {{
    python ~/.markdown/Main.py "$1"
}}


""")
if "markdown()" not in bashrc_script:
    Python_write_file(PATH_OF_BASHRC_SCRIPT, bashrc_function)


