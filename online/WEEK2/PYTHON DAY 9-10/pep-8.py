def some_long_function_name_that_is_not_descriptive(argument1,argument2=None,argument3=None): # Long function name, no spaces around assignment operator, no line length limit
    """This docstring is very long and doesn't follow PEP 8""" # Long line, no triple quotes
    if argument1 > 10 and argument2 != None: # Missing spaces around operators, no line breaks
      return argument1 + argument2, argument3 # No spaces after comma
    else:  # No spaces after colon
      return argument1-argument2,argument3 #Missing spaces around operators
   # This is a comment without a leading space after the #
 # and it goes on and on and on
def another_function_with_bad_naming_conventions(my_variable, My_Other_Variable): #  Wrong naming conventions for arguments
  """This docstring is bad and should be removed.""" # No docstring
  my_variable = my_variable.upper()
  return my_variable + My_Other_Variable

 # Bad indentation
  print(f"The result is: {some_long_function_name_that_is_not_descriptive(5,10)}") # Bad indentation, no line breaks, long lines
  print(f"The result is: {another_function_with_bad_naming_conventions(10,20)}") # Bad indentation
  # Bad usage of blank lines

 #Here are some more bad practices:
 # Long lines that exceed the 79 character limit.
 # No blank lines between functions.
 # Inconsistent indentation (3 spaces instead of 4).
 # Incorrect naming conventions.
 # No documentation.
 # Using the wrong types (e.g., using a tuple when a list is needed).
 # Missing spaces around operators and commas.
 # No line breaks in long expressions.
 # Missing colon.

 #This shows a bad example of multiple statements on one line.
if True: print("hello"); print("world");

 #Bad use of assignment
x = y = z = 100
