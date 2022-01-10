# Llull - The legendary programming language

## Setup

- Dependencies
  `python3`

- Activate virtual environment

  `$ python3 -m venv venv/`

  `$ source venv/bin/activate`

- Install dependencies

  `$ pip install -r requirements.txt`

## Execute a Llull program

Llull programs can be executed with no arguments like this:
  * `$ llull.py program.llull` In this case, it is required to have a method called `main`, otherwise
    it will print an exception.

  * The other way of executing Llull programs is passing an extra argument to indicate the starting method
    like this `llull.py program.llull <method>`.
    If the method is not defined in `program.llull` it will obviously
    print an exception. Also, it is necessary to pass as many arguments as the method indicated requires
    `llull.py program.llull <method> <arg1> <arg2> ... <argN>`

## Llull prettier

A prettier has been implemented to correctly format Llull programs.

Type `$ beat.py program.llull` to get the formatted code.

<img width="398" alt="Screenshot 2022-01-10 at 18 14 29" src="https://user-images.githubusercontent.com/80031479/148808868-15d28801-ae21-4a28-b9ff-4916fd27b87c.png">


## Important notes

- `read` can only read into a non existing variable. This variable is stored the same as in assign operations.

- There can't be a table and a variable with the same name.

- Tables are passed by reference.

- It's not possible to perform recursion where a mehod calls itself two times in an iteration.

- Strings can't contain character `#`. This character is used for comments.

## Exceptions

Llull's compiler is able to detect the following exceptions:
  - Invalid number of exceptions for method X.
  - There is no method X defined.
  - Variable X does not exist.
  - Variable X already exists. This is caused when trying to read into a variable that already exists.
  - There already exists a parameter with name X. If a new variable is declared and it has the same name as a parameter of he current method.
  - Can't divide by 0. When tryint to divide a number by 0.
  - Method X already exists. When detects a declaration of a method that already exists.
  - Parameter already X exists. When in the method definition two parameters have the same name.
  - There already exists a table with name X.
  - Invalid index to access table. When trying to access a table's index which does not exist.
  - Table X does not exist.


## Grammar AST representations

You can visit all the ASTs opening the file `llull.rrd.html` using a web browser.

## Dependencies

* autopep8
* pycodestyle
* antlr4-python3-runtime
* colored

## Author
@quimbaget
