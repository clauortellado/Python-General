# Easy way to convert docx to PDF with the language python’s docx2pdf module.
# It be used to convert files singly or in bulk using the command line or a python program.
# This module does not come built-in with Python. 
# To install this module type the below command in the terminal.
# pip install docx2pdf

# Python3 program to convert docx to pdf 
# using docx2pdf module 

# Import the convert method from the 
# docx2pdf module 
from docx2pdf import convert 

# Converting docx present in the same folder as the python file 
convert("Test.docx") 

# Converting docx specifying both the input and output paths 
convert("Trabajitos\Test.docx", "Other_Folder\test.pdf") 

# Notice that the output filename need not be the same as the docx 
# Bulk Conversion 
convert("Trabajitos\") 
