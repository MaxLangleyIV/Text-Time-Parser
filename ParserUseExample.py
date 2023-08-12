import TimestampParser

# Timestamp Parser is best used by executing TimestampParser.py in the Windows Command Promp
# (or the terminal of your choice). The following is only for demonstration.


# Open example text file.
test_text = open("ExampleText.txt", "r")

# Declare duration of the audio file as a tuple as: (minutes, seconds)
audio_duration = (46, 25)

# Perform the test.
TimestampParser.print_durations(TimestampParser.get_times(test_text), audio_duration)

# Close example text file.
test_text.close()
