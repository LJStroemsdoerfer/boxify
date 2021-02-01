# import libs
import re 
import os
import sys

# main class
class understander:
    """
    main class that understands the provided code

    understander() parses and analyzes the code from the user and provides the
    details needed to successfully containerize the user's API.
    """

    # define init method
    def __init__(self, script):

        # define slots
        self.wd = os.getcwd()

        # name of the file
        self.script = script

        # running from the same dir
        self.script_in_dir = self.script in os.listdir()

        # check python version
        major_v = str(sys.version_info[0])
        minor_v = str(sys.version_info[1])
        micro_v = str(sys.version_info[2])

        # write to slot
        self.py_version = str(major_v + '.' + minor_v + '.' + micro_v)



