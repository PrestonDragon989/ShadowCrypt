#!/usr/bin/env python3
"""A Purge file. A file that purges other files, """
import argparse

class Purge:
    def __init__(self):
        # Arguments
        self.args = None

    def get_arguments(self):
        # Setting & Getting Parameters
        parser = argparse.ArgumentParser(description='Command to purge (delete) files')
        parser.add_argument('-a', '--all', action='store_true', help='Delete all files')
        parser.add_argument('-u', '--unlocked', action='store_true', help='Delete all files that don\'t have the .locked extension')
        parser.add_argument('-l', '--locked', action='store_true', help='Delete all files with the .locked extension')
        parser.add_argument('-s', '--specific', metavar='EXT', nargs='+', help='Specific file extensions to delete (separated by commas)')
        parser.add_argument('-d', '--directories', metavar='EXT', nargs='+', help='Specify what directories you wish to purge (Default is current)')
        self.args = parser.parse_args()

        print('All:', self.args.all)
        print('Unlocked:', self.args.unlocked)
        print('Locked:', self.args.locked)
        print('Specific:', self.args.specific)
        print('Directory:',self.args.directories)

    def perform_action(self):
        pass

if __name__ == "__main__":
    purge = Purge()
    purge.get_arguments()