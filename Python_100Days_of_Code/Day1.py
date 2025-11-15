# Module: It's a file containing code written by someone else(usually) which can be imported and used in our programs.
# module---> Toolbox,  e.g. pyjokes
# to install Modules ----> pip install{module name}
#PiP: name of package manager or the standard package manager used for python.
    # Example: pip install flask
    #          pip install pyjokes
    # Code:
import pyjokes
joke = pyjokes.get_joke()
print(joke)

# Built in modules--> Pre-installed
# External modules--> installed using PIP