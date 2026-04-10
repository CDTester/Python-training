# Python-training

Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:
- web development (server-side),
- software development,
- mathematics,
- system scripting.

Python can: 
- be used on a server to create web applications.
- be used alongside software to create workflows.
- connect to database systems. It can also read and modify files.
- be used to handle big data and perform complex mathematics.
- be used for rapid prototyping, or for production-ready software development.

Why Python?
- Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
- Python has a simple syntax similar to the English language.
- Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
- Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
- Python can be treated in a procedural way, an object-oriented way or a functional way.

Good to know
- The most recent major version of Python is Python 3, which we shall be using in this tutorial.
- In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.

Python Syntax compared to other programming languages
- Python was designed for readability, and has some similarities to the English language with influence from mathematics.
- Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
- Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

## Virtual Environments
A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.

It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.

Think of a virtual environment as a separate container for each Python project. Each container:
- Has its own Python interpreter
- Has its own set of installed packages
- Is isolated from other virtual environments
- Can have different versions of the same package

Using virtual environments is important because:
- It prevents package version conflicts between projects
- Makes projects more portable and reproducible
- Keeps your system Python installation clean
- Allows testing with different Python versions

Create a new virtual environment using:
```bash
python -m venv myfirstproject
```

You can then activate this environment using:
```bash
myfirstproject\Scripts\activate
```

## INSTALLING modules
Use `pip3` to install packages you do not have.

e.g.
```bash
pip3 install selenium
```

Or you can use the `requirements.txt` file to install all the modulees needed. e.g.
```bash
pip3 install -r requirements.txt
```

