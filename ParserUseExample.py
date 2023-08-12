import TimeStampParser

# Open example text file.
test_text = open("exampleTimesToParse.txt", "r")

# Declare duration of the audio file as a tuple as: (minutes, seconds)
audio_duration = (46, 25)

# Perform the test.
TimeStampParser.print_durations(TimeStampParser.get_times(test_text), audio_duration)

# Close example text file.
test_text.close()
