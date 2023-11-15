
### Name three things that exception processing is good for:

    1. Error Handling : Exceptions provide a way to respond to errors that occur during program execution.
                        Proper exception handling can help you deal with these errors gracefully without crashing the program.
                    
    2. Program Continuation: By catching exceptions, a program can recover from the error condition and continue
                            execution further operation, which is particularly important in robust and fault-tolerant 
                            systems.
                        
    3. Resource Management: Exceptions help ensure that resources (like file handles or network connections) are
                            properly released, even when an error occurs. This is often done using 'try...finally'
                            blocks or context manager('with' statement).
                        
### If an exception is raised and not handled:

    An unhandled exception will cause the program to terminate immediately. Python will print a traceback to the console,
    which includes details about the exception and the state of the stack when the exception occurred.

### Recovering from an exception:

    A script can recover from an exception by using a 'try... except' block. The code that might raise an exception 
    goes in the 'try' block, and the code that handles the exception goes in the 'except' block. After the exception
    is handled, the script can proceed with its execution.


### The 'try' statement is for:

    The 'try' statement is used to catch and handle exceptions. It defines a block of code to be tested for errors
    while it is being executed.

### Two common variations of the 'try' statement:

    1. 'try...except': This is used to catch and handle exceptions that may be raised in the 'try' block.
    2. 'try...finally': This is used to define cleanup actions that must be executed under all circumstances.
                        A 'finally' block will run whether or not an exception was caught.
                    

### The 'raise' statement is for:

    The 'raise' statement is used to throw an exception if a certain condition occurs. This is used to 
    force an exception to occur and is typically used within an 'except' block to re-raise an exception
    or to raise a specific exception with a custom message.

