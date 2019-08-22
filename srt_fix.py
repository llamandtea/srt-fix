import subtitle


def parse_file(filename):
    """
    :param filename: string containing the name of the .srt file to parse
    :return: a list of Subtitles objects, representing the subtitles stored in the file
    """
    with open(filename, 'r', encoding='utf-8-sig') as fp:
        read_string = fp.read()

    string_sub_array = read_string.split("\n\n")
    sub_list = []

    i = 0
    while i < len(string_sub_array) - 1:
        sub = subtitle.parse_subtitle(string_sub_array[i])
        sub_list.append(sub)
        i = i + 1

    return sub_list


def write_file(filename, sub_list):
    """
    :param filename: string of the .srt file where to write
    :param sub_list: the list of the Subtitle objects to write to the file
    """
    with open(filename, 'w', encoding='utf-8-sig') as fp:
        for sub in sub_list:
            fp.write(sub.__str__())
            fp.write('\n')


def set_starting_time_offset(sub_list, new_starting_time):
    """
    :param sub_list: list of Subtitle objects where to shift the subtitle timestamps
    :param new_starting_time: timestamp where the subtitles should start
    :return: updated subtitles list
    """
    old_starting_time = sub_list[0].get_start()

    if new_starting_time > old_starting_time:
        for sub in sub_list:
            sub.set_start(sub.get_start() + (new_starting_time - old_starting_time))
            sub.set_end(sub.get_end() + (new_starting_time - old_starting_time))
    else:
        for sub in sub_list:
            sub.set_start(sub.get_start() - (old_starting_time - new_starting_time))
            sub.set_end(sub.get_end() - (old_starting_time - new_starting_time))

    return sub_list
