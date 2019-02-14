"""
@package utilities
file_name: custom_logger.py

"""
import inspect#Python inspect module is a very useful module which is used
# to introspect live objects in a program and look at the source code of
# modules, classes and functions which are used throughout a program.
import logging #module provides a way for applications to configure different
# log handlers and a way of routing log messages to these handlers

def customLogger(logLevel=logging.DEBUG):
    """
    logging module  provides a flexible
    framework for emitting log messages from Python.
    for each module to simply use a logger named like the module itself.
    This makes it easy for the application to route different modules
    differently.


    """
    # variable  loggerName Gets the name of the class / method from where this method is called to get the log messages
    loggerName = inspect.stack()[1][3] # contains the full name of the current module,
    #To emit a log message, a caller first requests a named logger.
    # The name can be used by the application to configure different rules
    # for different loggers. This logger then can be used to emit
    # simply-formatted messages at different log levels
    # (DEBUG, INFO, ERROR, etc.), which again can be used by the
    # application to handle messages of higher priority different
    # than those of a lower priority
    logger = logging.getLogger(loggerName)
    # By default,log all messages to set the log level as DEBUG
    logger.setLevel(logging.DEBUG)
    #Internally, the message is turned into a LogRecord object and
    # routed to a Handler object (fileHandler) registered for this logger.
    # The handler will then use a Formatter to turn the
    # LogRecord into a string and emit that string.

    fileHandler = logging.FileHandler("automation.log",mode='a')
    fileHandler.setLevel(logLevel)
    formatter = logging.Formatter('%(asctime)s: -%(name)s -%(levelname)s: %(message)s',
                    datefmt = '%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger