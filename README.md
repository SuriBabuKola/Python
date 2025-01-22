# Shell Scripting vs Python
* Certainly! The choice between using Shell Scripting and Python in DevOps depends on the specific task or problem you're trying to solve. Both have their strengths and are suitable for different scenarios. Here are some guidelines to help you decide when to use each:

## When Use Shell Scripting:
* **System Administration Tasks:** Shell scripting is excellent for automating routine system administration tasks like managing files, directories, and processes. You can use shell scripts for tasks like starting/stopping services, managing users, and basic file manipulation.
* **Command Line Interactions:** If your task primarily involves running command line tools and utilities, shell scripting can be more efficient. It's easy to call and control these utilities from a shell script.
* **Rapid Prototyping:** If you need to quickly prototype a solution or perform one-off tasks, shell scripting is usually faster to write and execute. It's great for ad-hoc tasks.
* **Text Processing:** Shell scripting is well-suited for tasks that involve text manipulation, such as parsing log files, searching and replacing text, or extracting data from text-based sources.
* **Environment Variables and Configuration:** Shell scripts are useful for managing environment variables and configuring your system.

## When Use Python:
* **Complex Logic:** Python is a full-fledged programming language and is well-suited for tasks that involve complex logic, data structures, and algorithms. If your task requires extensive data manipulation, Python can be a more powerful choice.
* **Cross-Platform Compatibility:** Python is more platform-independent than shell scripting, making it a better choice for tasks that need to run on different operating systems.
* **API Integration:** Python has extensive libraries and modules for interacting with APIs, databases, and web services. If your task involves working with APIs, Python may be a better choice.
* **Reusable Code:** If you plan to reuse your code or build larger applications, Python's structure and modularity make it easier to manage and maintain.
* **Error Handling:** Python provides better error handling and debugging capabilities, which can be valuable in DevOps where reliability is crucial.
* **Advanced Data Processing:** If your task involves advanced data processing, data analysis, or machine learning, Python's rich ecosystem of libraries (e.g., Pandas, NumPy, SciPy) makes it a more suitable choice.


# Python
## Installing Python
* [Refer Here](https://www.python.org/downloads/) for Official site
* In Official site, go to `Downloads` and choose `OS`
* Download required Version and Install it (Choose Windows)
* After installation check version `py --version`
  ![preview](./Images/Python1.png)

## GitHub Workspace for Python
* Go to GitHub Repo, click `Code --> Codespaces` and click `Add(+)`
* A Codespaces Workspace is Opened
* In that, Python is already installed and check Version `python --version`

## Run Sample Project
* Write a Sample Python Project to print Hello World
  * Create a file with `.py` extension
  * Add the following code to the file:
    ```python
    print("Hello, World!")
    ```
  * Run the Python file using the command, use `py <filename>` for Windows and `python <filename>` for remaining
  ![preview](./Images/Python2.png)
  ![preview](./Images/Python3.png)


# Data Types
* In programming, a data type is a classification or categorization that specifies which type of value a variable can hold.
* Data types are essential because they determine how data is stored in memory and what operations can be performed on that data.
* Python, like many programming languages, supports several built-in data types. Here are some of the common data types in Python:
  * **Numeric Data Types:**
    * **int:** Represents integers (whole numbers). Example: `x = 5`
    * **float:** Represents floating-point numbers (numbers with decimal points). Example: `y = 3.14`
    * **complex:** Represents complex numbers. Example: `z = 2 + 3j`
  * **Sequence Types:**
    * **str:** Represents strings (sequences of characters). Example: `text = "Hello, World"`
    * **list:** Represents lists (ordered, mutable sequences). Example: `my_list = [1, 2, 3]`
    * **tuple:** Represents tuples (ordered, immutable sequences). Example: `my_tuple = (1, 2, 3)`
  * **Mapping Type:**
    * **dict:** Represents dictionaries (key-value pairs). Example: `my_dict = {'name': 'John', 'age': 30}`
  * **Set Types:**
    * **set:** Represents sets (unordered collections of unique elements). Example: `my_set = {1, 2, 3}`
    * **frozenset:** Represents immutable sets. Example: `my_frozenset = frozenset([1, 2, 3])`
  * **Boolean Type:**
    * **bool:** Represents Boolean values (`True` or `False`). Example: `is_valid = True`
  * **Binary Types:**
    * **bytes:** Represents immutable sequences of bytes. Example: `data = b'Hello'`
    * **bytearray:** Represents mutable sequences of bytes. Example: `data = bytearray(b'Hello')`
  * **None Type:**
    * **NoneType:** Represents the `None` object, which is used to indicate the absence of a value or a null value.
  * **Custom Data Types:**
    * You can also define your custom data types using classes and objects.

## Strings
1. **String Data Type in Python:**
   * In Python, a string is a sequence of characters, enclosed within single (' '), double (" "), or triple (''' ''' or """ """) quotes.
   * Strings are immutable, meaning you cannot change the characters within a string directly. Instead, you create new strings.
   * You can access individual characters in a string using indexing, e.g., `my_string[0]` will give you the first character.
   * Strings support various built-in methods, such as `len()`, `upper()`, `lower()`, `strip()`, `replace()`, and more, for manipulation.
2. **String Manipulation and Formatting:**
   * **Concatenation:** You can combine strings using the `+` operator.
   * **Substrings:** Use slicing to extract portions of a string, e.g., `my_string[2:5]` will extract characters from the 2nd to the 4th position.
   * **String interpolation:** Python supports various ways to format strings, including f-strings (f"...{variable}..."), %-formatting ("%s %d" % ("string", 42)), and `str.format()`.
   * **Escape sequences:** Special characters like newline (\n), tab (\t), and others are represented using escape sequences.
   * **String methods:** Python provides many built-in methods for string manipulation, such as `split()`, `join()`, and `startswith()`.

## Numberic Data Type
1. **Numeric Data Types in Python (int, float):**
   * Python supports two primary numeric data types: **int** for integers and **float** for floating-point numbers.
   * Integers are whole numbers, and floats can represent both whole and fractional numbers.
   * You can perform arithmetic operations on these types, including addition, subtraction, multiplication, division, and more.
   * Be aware of potential issues with floating-point precision, which can lead to small inaccuracies in calculations.
   * Python also provides built-in functions for mathematical operations, such as `abs()`, `round()`, and `math` module for advanced functions.

## Regex
1. **Regular Expressions for Text Processing:**
    * Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
    * The `re` module in Python is used for working with regular expressions.
    * Common metacharacters: `.` (any character), `*` (zero or more), `+` (one or more), `?` (zero or one), `[]` (character class), `|` (OR), `^` (start of a line), `$` (end of a line), etc.
    * Examples of regex usage: matching emails, phone numbers, or extracting data from text.
    * `re` module functions include `re.match()`, `re.search()`, `re.findall()`, and `re.sub()` for pattern matching and replacement.
    * Common Use Cases of `re` Module:
      * **Search:** Check if a pattern exists in a string.
      * **Match:** Check if a pattern matches at the start or in the entire string.
      * **Split:** Break a string into substrings based on a delimiter or pattern.
      * **Substitute:** Replace parts of a string with other text based on a pattern.

## Examples
* **String_Concatenation:**
    ```python
    value1 = "Hello"
    value2 = "World!"

    result = value1 + " " + value2
    print(result)
    ```
  * String Concatenation refers to combining two or more strings into one string. This is typically done using the `+` operator.
  ![preview](./Images/Python4.png)
* **String_Length:**
    ```python
    text = "Python is High level programming language"
    length = len(text)
    print("Length of the String:", length)
    ```
  * This function returns the number of characters in the string, including spaces, punctuation, and special characters.
  ![preview](./Images/Python5.png)
* **String_Lower & Upper Cases:**
    ```python
    text = "Python is Dynamic Programming language"
    
    lowercase = text.lower()
    uppercase = text.upper()

    print("LowerCase:", lowercase)
    print("UpperCase:", uppercase)
    ```
  * Easily convert a string to lowercase or uppercase using the built-in string methods l`ower()` and `upper()`, respectively
  ![preview](./Images/Python6.png)
* **String_Replace:**
    ```python
    text = "Python is Awesome"
    new_text = text.replace("Awesome", "Great")
    print("Modified Text:", new_text)
    ```
  * Is used to replace a specified substring with another substring within a string. It returns a new string with the replacements made and does not modify the original string.
  ![preview](./Images/Python7.png)
* **String_Split:**
    ```python
    text = "Python is Dynamic Programming language"
    words = text.split()
    print("Words:", words)
    ```
  * Is used to divide a string into a list of substrings based on a specified delimiter. By default, it splits the string at whitespace characters (spaces, tabs, newlines).
  ![preview](./Images/Python8.png)
* **String_Strip:**
    ```python
    text = "    This text has an extra spaces    "
    stripped_text = text.strip()
    print("Stripped Text:", stripped_text)
    ```
  * Is used to remove leading and trailing whitespace (or other specified characters) from a string. It does not modify the original string but returns a new string with the removed characters.
  ![preview](./Images/Python9.png)
* **String_Substring:**
    ```python
    text = "Python is Dynamic Programming language"
    substring = "is"

    if substring in text:
      print(substring, "found in the text")
    else:
      print(substring, "not found in the text")
    ```
  * The code is checking whether a specific smaller string (substring) is present within a larger string (text).
  ![preview](./Images/Python10.png)
* **Int:**
    ```python
    #Integer Variables
    num1 = 10
    num2 = 5

    #Integer Division
    result_1 = num1 // num2
    print("Integer Division:", result_1)

    #Modulus (Remainder)
    result_2 = num1 % num2
    print("Modulus (Remainder):", result_2)

    #Absolute Value
    result_3 = abs(-7)
    print("Absolute Value:", result_3)
    ```
  * **Integer Division (//):** The `//` operator performs integer division, which divides the two numbers and discards the remainder, returning only the quotient as an integer.
  * **Modulus (Remainder) (%):** The `%` operator calculates the remainder of the division of one number by another.
  * **Absolute Value (abs()):** The `abs()` function returns the absolute value of a number, which is the non-negative version of the number.
  ![preview](./Images/Python11.png)
* **Float:**
    ```python
    #Float Variables
    num1 = 6.0
    num2 = 2.5

    #Basic Arithmetic
    result_1 = num1 + num2
    print("Addition:", result_1)

    result_2 = num1 - num2
    print("Subtraction:", result_2)

    result_3 = num1 * num2
    print("Multiplication:", result_3)

    result_4 = num1 / num2
    print("Division:", result_4)

    #Rounding
    result_5 = round(5.2194578232, 2) #Rounds to 2 decimal places
    print("Rounded:", result_5)
    ```
  * **Basic Arithmetic Operations:** Addition (`+`), Subtraction (`-`), Multiplication (`*`) & Division (`/`)
  * **Rounding (round()):** The `round()` function rounds a number to a specified number of decimal places. Here, `5.2194578232` is rounded to 2 decimal places.
  ![preview](./Images/Python12.png)
* **Regex (The Regular Expression Module):**
  * **Search:**
      ```python
      import re

      text = "I am learning Python for DevOps"
      pattern = r"Python"

      search = re.search(pattern, text)

      if search:
        print("Pattern Found:", search.group())   #Prints the matched text
        print("Start Position:", search.start())  #Start index of the match
        print("End Position:", search.end())      #End index of the match
      else:
        print("Pattern not Found")
      ```
    * `re.search()` is used to Scans the entire string to **find the pattern anywhere**.
    * In Pattern, The `r` before the string denotes a `raw string`, ensuring special characters (like `\`) are treated literally.
  ![preview](./Images/Python13.png)
  * **Match:**
      ```python
      import re

      text = "I am learning Python for DevOps"
      pattern = r"Python"

      match = re.match(pattern, text)

      if match:
        print("Match Found=", match.group())
      else:
        print("Match not Found")
      ```
    * `re.match()` is used to Checks for a **match only at the beginning of the string**.
  ![preview](./Images/Python14.png)
  * **Replace:**
      ```python
      import re

      text = "I am learning Python for DevOps"
      pattern = r"DevOps"

      replacement = "Company Requirement"

      new_text = re.sub(pattern, replacement, text)
      print("Modified Text:", new_text)
      ```
    * `re.sub()` is used to **search for a pattern in a string and replace it with a new value**.
  ![preview](./Images/Python15.png)
  * **Split:**
      ```python
      import re

      text = "Git,Jenkins,Terraform,Docker,Kubernetes,Python"
      pattern = r","

      split_result = re.split(pattern, text)
      print("Split Result:", split_result)
      ```
    * `re.split()` is used to **split a string based on a specific pattern** (in this case, a comma `,`).
  ![preview](./Images/Python16.png)


# Keywords in Python
* Keywords are reserved words in Python that have predefined meanings and cannot be used as variable names or identifiers.
* These words are used to define the structure and logic of the program.
* They are an integral part of the Python language and are case-sensitive, which means you must use them exactly as specified.
* Here are some important Python keywords:
  * **and:** A logical operator that returns `True` only if `both conditions are True`.
  * **or:** A logical operator that returns `True` if `at least one condition is True`.
  * **not:** A logical operator that flips the condition. If `it’s True, it becomes False`, and vice versa.
  * **if:** Starts a conditional block. `If` the condition is `True`, `the code inside runs`.
  * **else:** `Runs a block of code` if the `if` condition is `False`.
  * **elif:** Short for "else if," it is used to check additional conditions after an `if` statement and is used in combination with `if` and `else`.
  * **while:** It is used to create a loop that `repeatedly executes a block of code` as long as a `specified condition is true`.
  * **for:** It is used to create a loop that iterates over a sequence (such as a list, tuple, or string) and `executes a block of code for each item in the sequence`.
  * **in:** Used with `if`, it checks if a value is present in a sequence.
  * **try:** It is the beginning of a block of code that is subject to exception handling. It is followed by `except` to catch and handle exceptions.
  * **except:** Used with `try`, it defines a block of code to execute when an exception is raised in the corresponding `try` block.
  * **finally:** Used with `try`, it defines a block of code that is always executed, whether an exception is raised or not.
  * **def:** It is used to `define a function` in Python.
  * **return:** It is used within a function to `specify the value that the function should return`.
  * **class:** It is used to define a class, which is a blueprint for creating objects in object-oriented programming.
  * **import:** It is used to `import modules` or libraries to access their functions, classes, or variables.
  * **from:** Used with `import` to specify which specific components from a module should be imported.
  * **as:** Used with `import` to create an alias for a module, making it easier to reference in the code.
  * **True:** It represents a boolean value for `true`.
  * **False:** It represents a boolean value for `false`.
  * **None:** It represents a special `null value` or `absence of value`.
  * **is:** It is used for identity comparison, checking if two variables refer to the same object in memory.
  * **lambda:** It is used to create small, anonymous functions (lambda functions).
  * **with:** It is used for context management, ensuring that certain operations are performed before and after a block of code.
  * **global:** It is used to declare a global variable within a function's scope.
  * **nonlocal:** It is used to declare a variable as nonlocal, which allows modifying a variable in an enclosing (but non-global) scope.


# Understanding Variables in Python
* In Python, a variable is a named storage location used to store data.
* Variables are essential for programming as they allow us to work with data, manipulate it, and make our code more flexible and reusable.
* **Example:**
    ```python
    #Assigning a Value to a Variable
    my_variable = 24

    #Accessing the Value of a Variable
    print(my_variable)
    ```
  * When you print the Variable, it prints the value assigned to that Variable.
  ![preview](./Images/Python17.png)

## Variable Scope and Lifetime:
* **Variable Scope:** In Python, Variables have different Scopes, which determine where in the code the Variable can be accessed. There are mainly two types of Variable Scopes:
  1. **Local Scope:** Variables defined within a function have local scope and are only accessible inside that function.
      ```python
      def my_function():
        s = 22    #Local Variable
        print(s)
      
      my_function()
      print(s)
      ```
       * The Variable `s` is a Local Variable because it is defined inside the `my_function`. When you print the Variable `s` directly, it raises an error because the Variable `s` is not defined outside the function.
  ![preview](./Images/Python18.png)
  1. **Global Scope:** Variables defined outside of any function have global scope and can be accessed throughout the entire code.
      ```python
      k = 44    #Global Variable

      def my_function():
        print(k)
      
      my_function()
      print(k)
      ```
       * The Variable `k` is a Global Variable because it is not defined inside any function. When you print `k` inside `my_function` and outside of function, in both cases it prints the Variable Value because global variables are accessible throughout the entire program.
  ![preview](./Images/Python19.png)
* **Variable Lifetime:**
  * The Lifetime of a Variable is determined by when it is created and when it is destroyed or goes out of scope.
  * Local variables exist only while the function is being executed, while global variables exist for the entire duration of the program.

## Variable Naming Conventions and Best Practices
* It's important to follow naming conventions and best practices for Variables to write clean and maintainable code:
  * Variable Names should be Descriptive and indicate their Purpose.
  * Use Lowercase Letters and separate words with Underscores `_` (snake_case) for Variable Names.
  * Avoid using Reserved Words `(Keywords)` for Variable Names.
  * Choose Meaningful Names for Variables.
* **Example:**
    ```python
    #Good Variable Naming
    user_name = "Suresh"
    total_items = 22

    #Avoid using of Reserved Words
    class = "Python"  #Not Recommended

    #Use Meaningful Names
    s = 10                #Less Clear
    num_of_students = 10  #More Descriptive
    ```

## Explanation of Variable Updates
* In Python, when you assign a value to a variable, it overwrites the previous value stored in that variable.
* After updating a variable, any further use of that variable will refer to the updated value, not the original one.
* **No Conflicts:** There are no conflicts because Python allows variables to be re-assigned at any point in your code. The last assigned value is what the variable holds.
* **Example:**
    ```python
    port = 80
    print(f"Port: {port}")

    port = 443
    print(f"Updated Port: {port}")
    ```
  ![preview](./Images/Python20.png)
  * **First Assignment:**
    * When `port = 80` is defined, the variable `port` stores the value `80`.
    * The first `print(f"Port: {port}")` fetches the current value of `port` (which is `80`) and prints it.
  * **Re-assignment:**
    * When `port = 443` is executed, Python replaces the previous value of `port` with the new value (`443`).
    * Now, any further reference to `port` will use the updated value (`443`).
  * **No Conflicts:**
    * Python works in a linear, top-to-bottom manner.
    * When a variable is updated, it simply stores the new value, and the old value is no longer relevant.

# Exercises
* **Example:** Using Variables to Store and Manipulate Configuration Data in a DevOps Context
  * In a DevOps context, you often need to manage configuration data for various services or environments.
  * Variables are essential for this purpose.
  * Let's consider a scenario where we need to store and manipulate configuration data for a web server.
    ```python
    #Define Configuration Variables for a Wed Server
    server_name = "My_Nginx_Server"
    port = 80
    is_https_enabled = False
    max_connections = 500

    #Print the Configuration
    print(f"Server Name: {server_name}")
    print(f"Port: {port}")
    print(f"HTTPs Enabled: {is_https_enabled}")
    print(f"Max Connections: {max_connections}")

    #Update Configuration Values
    port = 443
    is_https_enabled = True

    #Print the Updated Configuration
    print(f"Updated Port: {port}")
    print(f"HTTPs Enabled: {is_https_enabled}")
    ```
    * In this example, we use variables to store and manipulate configuration data for a web server.
    * This allows us to easily update and manage the server's configuration in a DevOps context.
  ![preview](./Images/Python21.png)


# Some Important Points
## Formatted Strings (f)
* The `f` in `print(f"...")` is used to create **f-strings** (short for **formatted strings**) in Python.
* F-strings are a way to embed expressions inside string literals, using curly braces `{}`.
* They make it easy to include variable values or expressions directly within a string.
* The formate is `print(f"Name: {Var_Name}")`
* **Example:**
    ```python
    port = 80
    print(f"Port: {port}")
    ```