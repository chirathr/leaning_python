### Advanced Python concepts

#### Generators

A Python `generator` is a function which returns a generator `iterator` (just an object we can iterate over) by calling `yield`.
`yield` may be called with a value, in which case that value is treated as the "generated" value. The next time next() is called on the generator iterator (i.e. in the next step in a for loop, for example), the generator resumes execution from where it called `yield`, not from the beginning of the function. All of the state, like the values of local variables, is recovered and the generator contiues to execute until the next call to `yield`.

[Examples](/context_managers)

#### Context managers

Context managers allow us to allocate and release resources precisely when required. For example opening a file using `with`
we don't have to worry about closing the file after use or after an `Exception`. Conext manager are implemented by specifiying an
enter code block that usually returns a handle to a resource and an exit block that closes the resource.

[Examples](/generators)

#### OOPs concepts in Python

- Instance attributes and methods
- Static attributes and methods
- class methods
- Abstract Base Class(ABC)

[Examples](/oops)
