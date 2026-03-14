
---

Author: devbyte1328

Document: STANDARDS.md

Version: 0.0.32

Last Updated: 14-03-2026

---

This document is for development purposes. If you are reading this, it is

probably because the document was added to a project, allowing readers to

reference the standards. Regardless of your motive, I hope you find value.

---

# The Truth Will Set You Free

Enough pretending. Software development lives in a fractured world. Languages,

frameworks, conventions, distributions. STOP. Keep naming them and you'll get

stuck in a forever loop. We tried to build a universal tower, and like the

builders of Babel, we now live with the consequences. Endless dialects, endless

disagreement, and endless reinvention. Understanding everything is impossible.

This document makes a simpler choice. It discards the majority of solutions and

bases everything on a single core concept, functions. It is not negotiable. It

is set. The adherent must revert to first principles. These standards will not

appeal to everyone, and they are not intended to.

---

# Purpose of This Document

This document sets standards for software development. The standards are

intended to allow most of the focus to be directed to the development of the

solution. The practice of these standards will have the adherent revert to

basics while preserving the capabilities of standardized technologies. The

author reserves the option to extend these standards to any technology,

technology stack, and general software development practices in future versions

of this document.

---

# Look into the fray before you jump in

Practicing these standards and onboarding to them is inconvenient and

difficult. This document redefines existing concepts and frequently violates

established nomenclature. This increases the difficulty of writing

documentation and communicating about the code with developers who are unaware

of, or unwilling to practice, these standards. There is a lot of overwritten

and excluded code, concepts, and conventions. Continuous maintenance of the

compatibility layer for these standards is required. And for the last part,

though it is more of a social issue than a practical one, during scrutiny you

are probably going to have to contend with arguments of "technology misuse". I

hope you are already used to the last part.

---

# But look on the bright side

After the onboarding process, the adherent gains the benefit of being able to

devote most of his time and energy to developing the solution rather than

contending with frequently occurring problems during development. The

filesystem and codebase become easier to read. Compatibility layers remove the

need to read documentation and/or learn the nomenclature of the imported

technology. Resolving multiple methodologies is no longer necessary (the

"multiple approaches to the same solution" problem). A coding style is

introduced, providing consistency within the code. And finally, it feels like

the "house is tidy."

---

## Definitions 📋

### 𝐅𝐮𝐧𝐜𝐭𝐢𝐨𝐧

The core concept in software technology, it refers to the most basic form of

code.

### 𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞

The core function that begins the compilation of functions passed into the

parameters.

### 𝐓𝐚𝐠 𝐋𝐢𝐬𝐭

Formerly known in Python as the data type *"Dictionary"*, a Tag List is a

mutable, unordered collection of items, where each item consists of a unique

tag and a corresponding value. Tag Lists allow fast retrieval of values based

on their tags.

### 𝐌𝐮𝐥𝐭𝐢-𝐖𝐨𝐫𝐝 𝐀𝐛𝐛𝐫𝐞𝐯𝐢𝐚𝐭𝐢𝐨𝐧

A shortened form created from multiple words by combining the initial

letters of each word. it refers to identifiers formed

from the first letters of a multi-word name.

### 𝐒𝐢𝐧𝐠𝐥𝐞-𝐖𝐨𝐫𝐝 𝐀𝐛𝐛𝐫𝐞𝐯𝐢𝐚𝐭𝐢𝐨𝐧

A shortened form created from a single word by reducing its length while

attempting to refer to that original word. it refers to

simplified identifiers derived from one word.

### 𝐇𝐲𝐩𝐞𝐫-𝐓𝐞𝐜𝐡𝐧𝐢𝐜𝐚𝐥 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞

A multi-purpose general language that is one level removed from practically

being a programming language. It can be used for both human-to-human and

human-to-LLM communication. On the complete opposite end of the

spectrum there is the "High-Level Language"/"Natural Language".

### 𝐇𝐢𝐠𝐡-𝐋𝐞𝐯𝐞𝐥 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞

A general language that MAY fall under the same definition as a human

language depending on the epistemology used to describe the definition.

On the complete opposite end of the spectrum there is the "Programming

Language", and one level before it is the "Hyper-Technical Language".

---

## Imported Standards 📋

This document takes precedence over any imported standards.

For versioning scheme use

**Semantic Versioning 2.0.0** *(Full practice without any exception)*

```
https://semver.org
```

For ANY protocol documentation use

**RFC 2119**

```
https://rfc-editor.org/rfc/rfc2119
```

For coding styles and/or conventions use

**Python PEP 8** *(Except for parts that are overwritten or forbidden)*

```
https://peps.python.org/pep-0008
```

---

## Naming Framework Standard 📋

The naming framework consists of three rules, **Word Groups**, **Dataist Word

Types**, and **Connectors**. One to two words is a word group, each word is one

of four word types, between each word group there is one of three connectors

#### Word Groups

- *`any base-script`***`(Functionist)`** The name of the base-script itself

    and "return" to disclose functions that return data

- *`any words`***`(Dataist)`** - Containing any of categorizationist and/or

    researchist word types

#### Dataist Word Types

- *`any word`***`(Categorizationist)`** - A hyper-technical/high-level term that

    describes the stored value/function/solution definition
    
- *`any word`***`(Researchist)`** - a Mathematics/Technologies based term/data type

    that describes the stored value/function/solution definition

#### Connectors

- `of` - Bases the variable/function/solution definition/data type to the

    group on the right.
    
- `with` - Combines the left group with the right group.

- `for` - Describes what variable/function/solution definition will use the


    stored value

#### MUST ❗

- Put underscore between each word
- Uppercase each letter of any name with multi-word abbreviation.
- Treat multi-word abbreviation names as an entire dataist categorizationist
word type
- Use only the categorizationist and researchist word types for variables.
- Use functionist and dataist word groups for functions
- Prefix the name of base-script for functions.
- Uppercase each first letter of each word for base-script function name with
one or two words.

#### MUST NOT ❗
- Have the `for` connector use the name of the base-script it's in.
- Use `of` to base functionist word group

#### MAY ❗
- Pick any word amount to sufficiently describe variable/function
- Have functionist group type with the second word `return` to indicate it's
function returns data.


            ### 📌 **Variables**

            ### 📌 **Functions**


#### Examples

```
one_word = "script"

two_words = "script_path"

three_words = "path_of_script"

four_words = "path_of_python_script_for_LLM"

six_words = "path_of_python_script_with_line_numbers_for_LLM"

seven_words = "directory_path_of_python_scripts_with_line_numbers_for_LLM"

eight_words = "directory_path_of_python_scripts_with_prefix_of_line_numbers_for_LLM"
```


#### Examples

Correct ✅
```
from Scripts.Logs import *
from Scripts.System_Prompts import *

OS_initialize_directory("output")

PATH_OF_HOME_USER = OS_return_path_of_home_user()

PATH_OF_STE = f"{PATH_OF_HOME_USER}/Models/all-MiniLM-L6-v2"

def Logs_log(input_of_log_type, input_of_log_scope, input_of_log_text):
    pass
```

Wrong ❌
```
from utils.logs import *
from utils.system_prompts import *

os.makedirs("output", exist_ok=True)

PATH_OF_SENTENCE_TRANSFORMER_ENCODER = os.path.expanduser("~\Models\all-MiniLM-L6-v2")

def log_for_Logs(input_log_type, input_log_scope, input_log_text):
    pass
```

---
## Working Directory Standards 📋
Includes standards for Filsystems and codebases.
> [!NOTE]
> These rules are exceptions to human text and code comments.

### Adherent Requirements

#### MUST ❗
- Ignore the non-standardized names of automatically generated filesystems and
codebases.
- Name variables and functions using **capitalized multi-word abbreviations**
when introducing multi-word solution definitions (e.g., `"IDR"` for
`"instruction_dependency_resolutions"`).
- Use `/` when defining filesystem path values.
- For filesystem names:
  - Capitalize the first letter of each major word.
  - Use lowercase for minor words.
  - Separate all words with underscores.
- Fully capitalize Markdown filenames.
- Version-control Python scripts that are imported with `pip`.
- Use the file `Scripts.pip` for storing pip-managed Python scripts.

#### MUST NOT ❗
- Use single-word abbreviations (e.g., `"doc"` for `"documentations"`).
- Use `\` when defining filesystem path values. Docker resolves OS runtime compatibility issues, making `/` the preferred standard.
- Leave Python scripts imported with `pip` in rolling release.
- Use `requirements.txt` for storing pip-managed Python scripts.

#### MAY ❗
- Avoid using the same type of connector more than once within the same name.

### Examples

Correct ✅
```
PATH_OF_STE = f"{PATH_OF_HOME_USER}/Models/all-MiniLM-L6-v2"

instruction = ""

IDR = []

instruction_dependancies = ["abc", "def", "ghi"]
```

Wrong ❌
```
PATH_OF_SENTENCE_TRANSFORMER_ENCODER = os.path.expanduser("~\Models\all-MiniLM-L6-v2")

Instruction = ""

instruction_dependancy_resolutions = []

ID = ["abc", "def", "ghi"]
```

Correct ✅
```
.
├── Documentations
│   ├── STANDARDS.md
│   └── USEFUL_RESOURCES.md
├── .git
├── .gitignore
├── .Immutables.py
├── LICENSE
├── Logs
│   ├── LLM.log
│   └── Main.log
├── Main.py
├── __pycache__
├── README.md
├── Scripts.pip
├── Standards.py
├── Scripts
│   ├── Logs.py
│   └── System_Prompts.py
└── Virtual_Environment
```

Wrong ❌
```
.
├── doc
│   ├── standards.md
│   └── ur.md
├── .git
├── .gitignore
├── .immutables.py
├── LICENSE
├── logs
│   ├── llm.log
│   └── main.log
├── init.py
├── __pycache__
├── readme.md
├── requirements.txt
├── standards.py
├── libs
│   ├── logs.py
│   └── system_prompts.py
└── venv
```

#### MUST ❗
The following files **must exist** in the working directory:

- `Standards.py`
- `README.md`
- `Main.py`
- `Dockerfile`
- `.git`
- `.gitignore`

`Standards.py` may be placed either in the working directory or inside the
`Documentations/` directory.

`Main.py` must serve as the **entry point script**.

`Main.py` must also be the location where the **public API is declared**.

`Main.py` and `README.md` must both include the **solution version**.

Private solutions must include, at minimum, initialization instructions in
`README.md` written in **hyper-technical language**.

Public solutions must include initialization instructions in `README.md`
written in **high-level language**.

---

## Python Standards.py 📋

`Standards.py` acts as the **compatibility layer for the standards**.  
It is a crude but effective method of redefining Python behavior so that it
conforms to the standards defined in this document.

When writing code or importing scripts, **first update the compatibility layer**
to include the necessary corrections.

To access the standardized definitions in a target script, include the
following at the top of the file:

```
from Standards import *
```

#### MUST ❗

> [!NOTE]
> Exception: `importlib.util`

- `Standards.py` must contain **two empty lines above and below the script**.
- Each **script import section** must contain **two empty lines above and below**.
- Each **function** must contain **one empty line above and below**.
- Functions must **not contain empty lines internally**.
- Each function must **begin with the name of the base script being standardized**.

### Template for `Standards.py`

```


# Python

integer = int
string = str
title_list = dict

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


def Python_integer(any_value):
    return int(any_value)


def Python_string(any_value):
    return str(any_value)


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
                    temporary_hold_of_single_quotes += string_value[loop:loop + 1]
            elif was_single_quotes_found == True:
                if string_value[loop:loop + 1] != "'":
                    text_for_output += temporary_hold_of_single_quotes
                    text_for_output += string_value[loop:loop + 1]
                    temporary_hold_of_single_quotes = ""
                    was_single_quotes_found = False
                elif string_value[loop:loop + 1] == "'":
                    temporary_hold_of_single_quotes += string_values[loop:loop + 1]
        elif was_f_string_divider_found == True:
            text_for_output = text_for_output[:-1]
            was_double_quotes_found = False
            was_f_string_divider_found = False
            temporary_hold_of_single_quotes = ""
        loop += 1
    return text_for_output[1:-1]


def Python_titles_list(title_list):
    return list(title_list)


def Python_read_file(FILE_PATH):
    open_file = open(FILE_PATH, "r").read()
    open(FILE_PATH).close()
    return open_file


def Python_write_file(FILE_PATH, STRING_VALUE):
    open(FILE_PATH, "a").write(STRING_VALUE)
    open(FILE_PATH).close()


def Python_overwrite_file(FILE_PATH, STRING_VALUE):
    open(FILE_PATH, "w").write(STRING_VALUE)
    open(FILE_PATH).close()


def Python_type(ANY_VALUE)
    return type(ANY_VALUE)


def Python_length(ANY_VALUE):
    return len(ANY_VALUE)


import os


def OS_initalize_directory(directory_path):
    os.makedirs(directory_path)


def OS_return_boolean_of_directory_initialization(directory_path):
    return os.path.isdir(directory_name)


def OS_list_files_in_directory(directory_path):
    return os.listdir(directory_path)


def OS_delete_file(file_path):
    os.remove(file_path)


def OS_return_path_of_home_user():
    return os.path.expanduser("~")


```

## Python Immutables 📋

`Tuples` and `Frozen Dataclasses` are **not recognized as immutable types**
under these standards, and their use is **forbidden** under the *Python Code
Rules*.

At the time of writing, Python does not provide a true immutable data type.

However, the concept of immutability can improve code readability by clearly
expressing intent. Therefore, developers are encouraged to experiment with
**fake immutables** (yes, seriously).

Inside the working directory, create a file named:

```
.Immutables.py
```

This file will store and expose the fake immutable values.

Instructions for using `.Immutables.py` are provided in the section
**Python .Immutables.py**.



## Python .Immutables.py

To support fake immutables, the data type will simply be referred to as
**immutables**.

#### MUST ❗

- `.Immutables.py` must contain **two empty lines above and below the script**.
- The **Variables Naming Framework** must be followed.
- The **entire script must be capitalized**.
- There must be **no empty lines between immutables**.

To import immutable values:

1. Ensure `Standards.py` has been imported using:

```
from Standards import *
```

2. Initialize the constant with the prefix `IMMUTABLE`.
3. Pass the immutable reference into `load_immutables()`.
4. Assign the returned value to the constant.

### Example

`.Immutables.py`

```


LIST_DEBUG = ["DEBUG"]
LIST_OF_ERROR_CRITICAL = ["ERROR", "CRITICAL"]


```

`Scripts/Log.py`

```
from Standards import *

IMMUTABLE_LIST_DEBUG = load_immutables("LIST_DEBUG")
IMMUTABLE_LIST_OF_ERROR_CRITICAL = load_immutables("LIST_OF_ERROR_CRITICAL")

LIST_OF_LOG_TYPES = (
    IMMUTABLE_LIST_DEBUG
    + ["INFO", "WARNING"]
    + IMMUTABLE_LIST_OF_ERROR_CRITICAL
)
```

## Python Code Standards 📋

### Adherent Requirements

#### MUST ❗

Apply compatibility workarounds to imported technologies so they comply with
these standards.  
(In Python, this is implemented through `Standards.py`.)

Maintain a **maximum line length of 79 characters**.

If a variable name causes a line to exceed this limit, **remove words from the
variable name**.

Code using only references to the **standardized Python definitions**.

```
Python Data Types:
"Integers", "Floats", "Strings", "Booleans", "Lists", and "Tag Lists"

Python Naming Convention:
"Constants"

Python Property Type:
"Immutables"

Python Functions:
"Imports", "Built-in", "Base-script", "Whiles", and
"Condition Functions"
("Ifs", "Elifs", "Elses", "Ins", "Not Ins", "Trys", "Excepts", "Finallys", and "Raises")
```

### Python Indexing Standard 📋

If an index is corrected using `+1` or `-1` because Python indexing starts
at `0`, a comment must be added explaining the correction.

Example:

```
string_of_loop_for_IDR = Python_string(loop_for_IDR + 1)
# "+ 1" because of Python indexing...
```

### Python While Function Standard 📋

`break` **may be used** to exit the loop.

```
loop = 0
...
while loop < ...:
    ...
        break
    ...
    loop += 1
```

### Python Condition Function Standard 📋

- **If** — used for the primary intended data manipulation.
- **Elif** — used for secondary or exceptional cases.
- **Else** — used only when absolutely necessary.
- **Raise** statements must use **Python's standard error hierarchy**.

A reference list of Python exceptions can be found here:

```
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
```

#### MUST NOT ❗

Do **not modify the base implementation of the imported technology** to
enforce these standards.

Example: modifying **CPython** itself to comply with these standards.

> [!NOTE]
> Exceptions apply only to:
> - `Standards.py`
> - Python data type redefinitions
> - Python condition functions

The following legacy Python constructs **must not be used**:

```
Classes
Frozen Classes
Tuples
Object Methods
Lambdas
For Loops
Is (comparison operator)
Nested While Loops
Functions within functions
Functions that return functions
Dunder methods
Using "not" before "in"
```

MUST NOT USE IMPORTS:
pathlib
sys
shutil
