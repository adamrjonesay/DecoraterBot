from distutils.core import setup
import Cython
from Cython.Build import cythonize

def compile_to_pyd(filepath, filename):
    """
        Helper function that handles exceptions and tells what file actually generates exceptions.

        This should help fix some issues with things.
    """
    sourcefilename = filename.replace('.py', '.c')
    if filename == 'euctwfreq.py':
        print('[ERROR] {0} is a known file to make Microsoft\'s Incremental Linker cause a memory leak for some reason when it is compiled to a source file with the name of {1}.\nPlease contact Microsoft. (Visual Studio 2015)'.format(filename, sourcefilename))
    else:
        try:
            setup(ext_modules = cythonize(filepath + filename, language_level=3))
        except Cython.Compiler.Errors.CompileError:
            print('Failed to compile {0} to {1}.\nFix the Error(s) and then try to compile the file again.'.format(filename, sourcefilename))
        except ValueError:
            print('The file {0} was not found.\nPlease make sure the file exists and then try again.'.format(filename))
