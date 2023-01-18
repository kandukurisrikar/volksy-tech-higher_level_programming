#!/usr/bin/python3
"""write a file"""


def write_file(filename="", text=""):
    """write"""
    if filename:
        with open(filename, mode = 'w', encoding = 'UTF-8') as f:
            return(f.write(text))

