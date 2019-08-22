import re
from datetime import datetime, time


class Subtitle:
    """
    class used to represent an instance of a subtitle stored in a .srt file
    'index' is the index number of the subtitle, >= 0
    'start' is the initial timestamp of the subtitle
    'end' is the final timestamp of the subtitle
    'sub_data' is the actual subtitle
    """
    def __init__(self):
        self.index = 0
        self.start = time()
        self.end = time()
        self.sub_data = ""

    def get_index(self):
        return self.index

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_sub_data(self):
        return self.sub_data

    def set_index(self, new_index):
        self.index = new_index

    def set_start(self, new_start):
        self.start = new_start

    def set_end(self, new_end):
        self.end = new_end

    def set_sub_data(self, new_sub_data):
        self.sub_data = new_sub_data

    def __str__(self):
        separator = " --> "
        string_format = r"%H:%M:%S,%f"
        start = self.get_start().strftime(string_format)[:-3]
        end = self.get_end().strftime(string_format)[:-3]
        return str(self.get_index()) + '\n' + start + separator + end + '\n' + self.get_sub_data()


def parse_subtitle(string):
    """
    :param string: string structured as it follows:
        - index
        - HOURS:MINUTE:SECONDS,MILLISECONDS --> HOURS:MINUTE:SECONDS,MILLISECONDS
        - subtitle
        to be converted to an instance of the subtitle class

    :return: a Subtitle object, storing the values read from the string
    """
# OUTPUT
    parsed_sub = Subtitle()

# ALGORITHM
    parsed_sub = parse_index(string, parsed_sub)
    parsed_sub = parse_timestamps(string, parsed_sub)
    parsed_sub = parse_sub_data(string, parsed_sub)
    return parsed_sub


def parse_index(string, parsed_sub):
    """

    :param string: string structured as it follows:
    - index
    - HOURS:MINUTE:SECONDS,MILLISECONDS --> HOURS:MINUTE:SECONDS,MILLISECONDS
    - subtitle
    in which to parse the index of the subtitle and set it in an instance of the Subtitle class.
    If the string has no index, the the Subtitle object index remains set to 0

    :param parsed_sub: instance of the class Subtitle, in which the user is storing
    the values parsed from the string

    :return: the updated "parsed_sub" Subtitle instance
    """

    index_pattern = r"(\A\d+)" + "\n"
    match = re.match(index_pattern, string)
    if match:
        index = int(match.group(0))
        parsed_sub.set_index(index)

    return parsed_sub


def parse_timestamps(string, parsed_sub):
    """

    :param string: string structured as it follows:
    - index
    - HOURS:MINUTE:SECONDS,MILLISECONDS --> HOURS:MINUTE:SECONDS,MILLISECONDS
    - subtitle
    in which to parse the timestamps of the subtitle and set them as "starts" and "end" fields of an instance
    of the Subtitle class.
    If the string has no timestamps, or is badly formatted, the the Subtitle object's timestamps remain set to
    00:00:00,000

    :param parsed_sub: instance of the class Subtitle, in which the user is storing the values parsed from the string

    :return: the updated "parsed_sub" Subtitle instance
    """

    start_time_position = 0
    end_time_position = 1

    timestamp_pattern = r"(\d{2}:\d{2}:\d{2},\d{3})"
    timestamp_format = "%H:%M:%S,%f"
    timestamp_indexes = re.findall(timestamp_pattern, string)
    if len(timestamp_indexes) > 0:
        starting_time = datetime.strptime(timestamp_indexes[start_time_position], timestamp_format)
        ending_time = datetime.strptime(timestamp_indexes[end_time_position], timestamp_format)
        parsed_sub.set_start(starting_time)
        parsed_sub.set_end(ending_time)

    return parsed_sub


def parse_sub_data(string, parsed_sub):
    """
    :param string: string structured as it follows:
    - index
    - HOURS:MINUTE:SECONDS,MILLISECONDS --> HOURS:MINUTE:SECONDS,MILLISECONDS
    - subtitle
    in which to parse the subtitle and store it in an instance of the Subtitle class
    If the string has no subtitle, the Subtitle object's field "sub_data" remains set to ""

    :param parsed_sub: instance of the class Subtitle, in which the user is storing the values parsed from the string

    :return: the updated "parsed_sub" Subtitle instance
    """

    sub_data = ""
    sub_data_index = 2
    split_string = string.split('\n')

    i = sub_data_index
    while i < len(split_string):
        sub_data = sub_data + split_string[i] + "\n"
        i = i + 1

    parsed_sub.set_sub_data(sub_data)

    return parsed_sub
