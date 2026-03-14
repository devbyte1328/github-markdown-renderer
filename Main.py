from Standards import * 
import os
import subprocess
import time
import signal


PATH_OF_HOME_USER = OS_return_path_of_home_user()
PATH_OF_SOURCE_DIRECTORY = f"{PATH_OF_HOME_USER}/.markdown/src"
PATH_OF_MARKDOWN_DIRECTORY = f"{PATH_OF_HOME_USER}/.markdown"


def Main_source_files_for_deletion():

    if OS_return_boolean_filesystem(PATH_OF_SOURCE_DIRECTORY):
    
        loop = 0
        list_of_directory_files = OS_return_list_of_directory_files(
            PATH_OF_SOURCE_DIRECTORY
        )
        while loop < Python_length(list_of_directory_files):
            file_for_loop = list_of_directory_files[loop]
            file_path = f"{PATH_OF_SOURCE_DIRECTORY}/{file_for_loop}"
            if OS_return_boolean_file(file_path):
                OS_delete_file(file_path)
            loop += 1


def Main_exit_with_deletion_of_source_files():
    Main_source_files_for_deletion()
    OS_exit_Main()


Main = True
while Main == True:

    parameters = OS_return_function_parameters()

    if Python_length(parameters) != 2:
        OS_exit_Main()

    markdown_script_for_render = parameters[1]

    path_of_file_for_input = OS_return_absolute_path(markdown_script_for_render)

    if OS_return_boolean_filesystem(path_of_file_for_input) == False:
        OS_exit_Main()

    if OS_return_boolean_directory(PATH_OF_SOURCE_DIRECTORY) == False:
        OS_initialize_directory(PATH_OF_SOURCE_DIRECTORY)

    path_of_file_for_output = f"{PATH_OF_SOURCE_DIRECTORY}/{markdown_script_for_render}"

    Main_source_files_for_deletion()
    SubProcess_Initialize(f"cp {path_of_file_for_input} {path_of_file_for_output}")
    
    Python_overwrite_file(
        f"{PATH_OF_SOURCE_DIRECTORY}/SUMMARY.md",
        f"- [{markdown_script_for_render}](./{markdown_script_for_render})\n"
    )

    Signal_signal(Signal_return_signal_for_interruption(), Main_exit_with_deletion_of_source_files)
    Signal_signal(Signal_return_signal_for_termination(), Main_exit_with_deletion_of_source_files)

    SubProcess_Parallel_Initialize(f"mdbook serve -p 4000 {PATH_OF_MARKDOWN_DIRECTORY}")

    record_of_markdown_script = ""
    while True:
        time.sleep(0.5)
        try:
            markdown_script = Python_read_file(path_of_file_for_input)
            if markdown_script != record_of_markdown_script:
                SubProcess_Initialize(f"cp {path_of_file_for_input} {path_of_file_for_output}")
                record_of_markdown_script = markdown_script
        except FileNotFoundError:
            pass

