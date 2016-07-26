from distutils.core import setup
import Cython
from Cython.Build import cythonize

def compile_to_pyd(filepath, filename):
    """
        Helper function that handles exceptions and tells what file actually generates exceptions.

        This should help fix some issues with things.
    """
    try:
        setup(ext_modules = cythonize(filepath + filename, language_level=3))
    except Cython.Compiler.Errors.CompileError:
        print('Failed to compile {0} to a pyd.\nFix the Error(s) and then try to compile the file again.'.format(filename))
    except ValueError:
        print('The file {0} was not found.\nPlease make sure the file exists and then try again.'.format(filename))
