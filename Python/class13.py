#----------------------------Packages--------------------------------------------------------------
# Packages is like a folder(which we have in our laptop where we store lot of files) in Python where we can use lots of libraries
#like we store in folder in laptop lot of files here in package we store librraies.

#-------------------------------libraries--------------------------
# a library is a python file where we store a lot of functions are there which someone else has created and we can use it'# in our code 
# that means those functions we can use from these python file(library). other functions are not in library they are
#directly available in python because they were created at the time when python was created eg : input(), print(),
#reverse(), sort() and many more. but python keeps on getting upgraded by adding new functions to it.
# These new functions are added in python files which we say library and we use from those library.
# There are so many libraries like gaming libraries, software library, website libraries etc..     

#in order to use functions from these library we first need to connect with these libraies using import

#There are three ways to connect with library :
#1. from libraryname import * 
#2. import libraryname ( first import all functions from library)
#3. from library import functioname( ths import only one functio and we can only use that function)

#Example : use random library
import random

#randint() : generates a random number beteen given range
a=random.randint(1, 3)
print(a)

#------------------------Connect two python file--------------------------------------
#Steps to connect
#1. create a new python file
#2. inside that create a function or class and do all coding in that function or class
#3. come back to other python file. at top import second file.
#by using import w econnect to library and by using import only we connect with two python files.
#import function at top
#from filename import function
#call the function : functioname()

from new import hi
hi()


