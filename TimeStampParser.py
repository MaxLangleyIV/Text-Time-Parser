'''
Max Langley IV
LLLP Photo Duration Calculator
'''

import re


def print_durations(times, audio_duration):
    photo_id = 1
    duration = 0
    previous_duration = 0

    i = 0
    for item in times:

        item = tuple(item.split(":"))

        # Try to get next item in list
        try:
            item2 = tuple(times[i + 1].split(":"))

        except IndexError:
            # Final timestamp, so calculate final duration using total audio duration instead of next timestamp.
            duration = ((audio_duration[0] * 60) + audio_duration[1]) - ((int(item[0]) * 60) + int(item[1]))
            print("Photo: %2i  |Seconds: %5i  |Start Time: %s\n" % (photo_id, duration, str(item[0] + ":" + item[1])))
            return

        duration = ((int(item2[0]) * 60) + int(item2[1])) - ((int(item[0]) * 60) + int(item[1]))

        print("Photo: %2i  |Seconds: %5i  |Start Time: %s\n" % (photo_id, duration, str(item[0] + ":" + item[1])))

        previous_duration += duration
        photo_id += 1
        i += 1

    return


def get_times(file):
    regex = r'\b\d+:\d{2}\b'
    line_list = []

    for line in file:

        match = re.findall(regex, line)

        if match:
            for currentMatch in match:
                line_list.append(currentMatch)

    return line_list


