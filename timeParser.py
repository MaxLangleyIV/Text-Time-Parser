'''
Max Langley IV
LLLP Photo Duration Calculator
'''

import re


def time_list():
    times = []
    raw_time = tuple(input("Enter time in minutes and seconds: ").split(":"))

    while raw_time > ("",):
        times.append(raw_time)
        raw_time = tuple(input("Enter time in minutes and seconds: ").split(":"))

    return times


def calculator(times):
    photo_id = 1
    duration = 0
    previous_duration = 0

    for item in times[1:]:
        item = tuple(item[0].split(":"))

        # in case nothing before the ":", might need better fix
        if item[0] == ") ":
            item = ("0", item[1])

        print(item)
        duration = ((int(item[0]) * 60) + int(item[1])) - previous_duration

        print("Photo: %2i  |Seconds: %5i  |End Time: %s" % (photo_id,  duration, str(item[0] + ":" + item[1])))

        previous_duration += duration
        photo_id += 1

    return


def times_from_file(file_name):
    regex = "..:..|.:.."
    this_file = open(file_name)
    line_list = []

    for line in this_file:

        if (line[0] == "(") | line[0].isdigit():
            line_list.append(re.findall(regex, line))

    this_file.close()
    return line_list


times = times_from_file(input("Enter path for text file: "))
calculator(times)


