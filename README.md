# Decorators

This repo presents solutions (my own implementations) to decorators-related challenges and other relevant examples from the Udemy course "The Modern Python 3 Bootcamp".

__<ins>Specifics</ins>__

1) The script `decorator.py` presents a simple decorator example.

2) In the file `decorators_signatures.py` we have an example of decorators with different arguments.

3) The scripts `metadata_not_preserved.py` and `metadata_preserved.py` show an issue regarding metadata preservation when using decorators and how to solve it respectively.

4) In the `speed_test_decorator.py` file we build a decorator that tests the speed of a function (meaning it calculates how long its execution takes).

5) The script `show_args_kwargs.py` presents a decorator that before invoking the function passed to it, prints a tuple with the positional arguments and a dictionary with the keyword arguments.

6) The `no_kwargs.py` file creates a decorator that prevents a function from being called with any keyword arguments.

7) The `double_return.py` script produces a decorator which returns a list with two copies of the inner function's return value.

8) In the `fewer_than_three_args.py` file we construct a decorator that allows a function passed to it to be invoked only if there are fewer than three positional arguments passed to the latter.

9) A decorator that enables a function passed to it to be invoked only if all of the arguments passed to it are integers is built in the `only_ints.py` file.

10) In the `authorized.py` file we define a decorator which allows a function passed into it to be invoked only if a keyword argument named "role" that has the value "admin" is passed into the latter.

11) The `decorator_with_argument.py` file shows how to create a decorator that accepts an argument. This decorator is used to ensure that the first argument passed into a function has a specific value.

12) The `enforce_arg_types.py` script creates a decorator that accepts specific argument types (as arguments) and ensures that only these types can be passed into a function. In case different ones are given it converts them to the expected ones if possible.

13) In the `delay.py` file we build a decorator that accepts a time period (in seconds) as an argument and delays the execution of the function beind decorated by that amount of time.
