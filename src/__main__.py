import srt_fix
import interface
from datetime import datetime, time


def main():

    initial_time = time()
    args = interface.parser.parse_args()
    if interface.file_check(args.filename) and interface.timestamp_check(args.initial_timestamp):
        initial_time = datetime.strptime(args.initial_timestamp, r"%H:%M:%S,%f")
        sub_list = srt_fix.parse_file(args.filename)
        sub_list = srt_fix.set_starting_time_offset(sub_list, initial_time)
        srt_fix.write_file(args.filename, sub_list)

    if not interface.file_check(args.filename):
        print("Error: the file does not exist.")

    if not interface.timestamp_check(args.initial_timestamp):
        print("Error: the timestamp is badly formatted.")


main()
