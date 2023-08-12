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


# Searches a file for all occurrences of timestamps.
def get_times(file):
    regex = r'\b\d+:\d{2}\b'
    line_list = []

    for line in file:

        match = re.findall(regex, line)

        if match:
            for currentMatch in match:
                line_list.append(currentMatch)

    return line_list


def ensure_txt_extension(filename):
    if not filename.endswith(".txt"):
        filename += ".txt"
    return filename


def main():
    print("Welcome to the Timestamp Parser!")

    file_found = False

    while not file_found:
        filename = input("Enter the name of the text file to scan.\n"
                         "(It should be placed in the same directory as TimestampParser.py)\nFile Name: ")
        filename = ensure_txt_extension(filename)

        try:
            with open(filename, "r") as file:
                file_found = True
                input_valid = False

                while not input_valid:
                    audio_duration = input("\nEnter the duration of the audio file which the timestamps are from.\n"
                                           "Use the format minutes:seconds\nAudio Duration: ")
                    try:
                        audio_duration = audio_duration.split(":")
                        audio_duration = (int(audio_duration[0]), int(audio_duration[1]))
                        input_valid = True

                    except ValueError:
                        print(f"\nInput'{audio_duration}' is not a valid duration.\n"
                              f"Enter the duration in the form of minutes:seconds.\n"
                              f"For example: 35:45, or 120:50")

                times = get_times(file)
                print_durations(times, audio_duration)

        except FileNotFoundError:
            print(f"\nFile '{filename}' not found.\n"
                  f"Verify that the file is in the same directory as TimestampParser.py\n"
                  f"Only input .txt files.")


if __name__ == "__main__":
    main()
