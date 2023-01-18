#!/usr/bin/python3
"""write append"""


def append_write(filename="", text=""):
    """append"""
    if filename:
        with open(filename, mode='append', encoding='UTF-8') as f:
            return(f.append(text))
