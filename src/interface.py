import argparse
import os.path
import re

parser = argparse.ArgumentParser(description="Set a new initial timestamp for a .srt subtitle file")
parser.add_argument('filename', type=str, help="Name of the .srt file to edit.")
parser.add_argument('initial_timestamp', type=str, help="New initial timestamp of the first subtitle."
                                                                           " Represented as hh:mm:ss,msmsms.")


def file_check(filename):

    return os.path.isfile(filename)


def timestamp_check(str_timestamp):
    timestamp_pattern = r"(\d{2}:\d{2}:\d{2},\d{3})"

    return re.match(timestamp_pattern, str_timestamp)
