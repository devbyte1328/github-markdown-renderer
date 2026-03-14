

# Python

Python_data_type_integer = int
Python_data_type_float = float
Python_data_type_string = str
Python_data_type_boolean = bool
Python_data_type_list = list
Python_data_type_tag_list = dict

import importlib.util
def Python_load_immutables(immutable_data):
    spec = importlib.util.spec_from_file_location(
        "immutables",
        os.path.join(os.path.dirname(__file__), ".immutables.py")
    )
    immutables = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(immutables)
    immutable_data = getattr(immutables, immutable_data)
    return immutable_data

def Python_print(any_value):
    print(any_value)

def Python_integer(any_value):
    return int(any_value)
    
def Python_float(any_value):
    return float(any_value)
    
def Python_string(any_value):
    return str(any_value)
    
def Python_boolean(any_value):
    return bool(any_value)
    
def Python_list(any_value):
    return list(any_value)

def Python_tag_list(any_value):
    return dict(any_value)

def Python_fstring(string_value):
    loop = 0
    temporary_hold_of_single_quotes = ""
    was_single_quotes_found = False
    was_f_string_divider_found = False
    text_for_output = ""
    while loop < len(string_value):
        if temporary_hold_of_single_quotes == "''''''":
            was_f_string_divider_found = True
        if was_f_string_divider_found == False:
            if was_single_quotes_found == False:
                if string_value[loop:loop + 1] != "'":
                    text_for_output += string_value[loop:loop + 1]
                elif string_value[loop:loop + 1] == "'":
                    was_single_quotes_found = True
                    temporary_hold_of_single_quotes += (
                        string_value[loop:loop + 1]
                    )
            elif was_single_quotes_found == True:
                if string_value[loop:loop + 1] != "'":
                    text_for_output += temporary_hold_of_single_quotes
                    text_for_output += string_value[loop:loop + 1]
                    temporary_hold_of_single_quotes = ""
                    was_single_quotes_found = False
                elif string_value[loop:loop + 1] == "'":
                    temporary_hold_of_single_quotes += (
                        string_values[loop:loop + 1]
                    )
        elif was_f_string_divider_found == True:
            text_for_output = text_for_output[:-1]
            was_double_quotes_found = False
            was_f_string_divider_found = False
            temporary_hold_of_single_quotes = ""
        loop += 1
    return text_for_output[1:-1]

def Python_read_file(FILE_PATH):
    open_file = open(FILE_PATH, "r").read()
    open(FILE_PATH).close()
    return open_file

def Python_read_binary_of_file(FILE_PATH):
    open_file = open(FILE_PATH, "rb").read()
    open(FILE_PATH).close()
    return open_file
    
def Python_write_file(FILE_PATH, STRING_VALUE):
    open(FILE_PATH, "a").write(STRING_VALUE)
    open(FILE_PATH).close()

def Python_write_binary_of_file(FILE_PATH, STRING_VALUE):
    open(FILE_PATH, "ab").write(STRING_VALUE)
    open(FILE_PATH).close()

def Python_overwrite_file(FILE_PATH, STRING_VALUE):
    open(FILE_PATH, "w").write(STRING_VALUE)
    open(FILE_PATH).close()

def Python_overwrite_binary_of_file(FILE_PATH, STRING_VALUE):
    open(FILE_PATH, "wb").write(STRING_VALUE)
    open(FILE_PATH).close()

def Python_type(ANY_VALUE):
    return type(ANY_VALUE)

def Python_length(ANY_VALUE):
    return len(ANY_VALUE)


import os

def OS_exit_Main():
    os.sys.exit()

def OS_environment(ANY_TAG, ANY_VALUE):
    os.environ[ANY_TAG] = ANY_VALUE

def OS_initialize_directory(directory_path):
    os.makedirs(directory_path)

def OS_return_boolean_filesystem(filesystem_path):
    return os.path.exists(filesystem_path)

def OS_return_boolean_file(file_path):
    return os.path.isfile(file_path) 

def OS_return_boolean_directory(directory_path):
    return os.path.isdir(directory_path)

def OS_return_list_of_directory_files(directory_path):
    return os.listdir(directory_path)

def OS_delete_file(file_path):
    os.remove(file_path)

def OS_return_path_of_home_user():
    return os.path.expanduser("~")

def OS_return_absolute_path(relative_path_of_filesystem):
    return os.path.abspath(relative_path_of_filesystem)

def OS_return_resolution_path_of_symbolic_link(relative_path_of_symbolic_link):
    return os.path.realpath(relative_path_of_symbolic_link)

def OS_return_function_parameters():
    return os.sys.argv


import subprocess

def SubProcess_Initialize(functions):
    subprocess.run(functions, shell=True)

def SubProcess_Parallel_Initialize(functions):
    subprocess.Popen(functions, shell=True)


import signal

def Signal_signal(signal_type, function):
    signal.signal(signal_type, function)

def Signal_return_signal_for_interruption():
    return signal.SIGINT

def Signal_return_signal_for_termination():
    return signal.SIGTERM


