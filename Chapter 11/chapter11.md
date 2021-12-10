# Chapter 11 - Practice Questions

1. `assert spam >= 10`.
2. `assert eggs.lower() != bacon.lower()`.
3. `assert False`.
4. `import logging` and `logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')`.
5. `import logging` and `logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')`.
6. DEBUG, INFO, WARNING, ERROR, CRITICAL.
7. `logging.disable(logging.CRITICAL)`.
8. Because by using `print()` you had to comment them out to surpress the output, but with the `logging` module you can just add `logging.disable()` once to avoid outputs.
9. **Step In** will move the debugger to a function call. **Step Over** will quickly execute the function call without stepping into it. **Step Out** will quickly execute the rest of the code until it steps out of the function it currently is in.
10. When the program terminates or reaches a __breakpoint__.
11. A breakpoint forces the debugger to pause whenever the program execution reaches that line.
12. A breakpoint can be set by clicking on the line number of the code.