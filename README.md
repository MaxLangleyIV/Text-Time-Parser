# Timestamp Parser

A Python script that extracts and presents a list durations from a text file containing timestamps. 

## The Problem:

When editing video content the producer may provide a list of timestamps and their corresponding visual elements. 
Some editing software requires element durations to be input as seconds.
This necessitates the repetitive calculation of durations by the editor.

## The Solution:

This script automates the task of finding the timestamps and performing the necessary calculations.
The results are then displayed in the terminal window as a formatted list.

## Getting Started

1. Clone the repository, or download the zip file and extract it to the location of your choice.

2. Ensure you have the latest Python installed on your system.
   ```
   https://www.python.org/downloads/
   ```
3. Place the text containing timestamps into a .txt file.
   For instance: If you receive an email containing the timestamps, copy and paste the message into a text file.

5. Determine the total duration of the project which the timestamps pertain to.
   For instance: If the timestamps are taken from an audio file, then find the duration of said file.

## Usage

Place your timestamped text file (e.g., ExampleText.txt) in the same directory as TimestampParser.py.

1. Open a terminal and navigate to the project directory: 
 
2. Run the parser with the command:
   ```
   python TimestampParser.py
   ```

3. Enter the name of the text file to scan and the duration of the associated file in the format of *minutes:seconds*.

The script will process the provided text file and display the durations associated with each timestamp.

## Files
**TimestampParser.py:** Contains the core functions for parsing timestamps and calculating durations.

**ParserUseExample.py:** Provides an example of how to use the Timestamp Parser with your own input.

**ExampleText.txt:** A sample text file with timestamps for demonstration purposes.

## Contributing
Contributions to the Timestamp Parser project are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.
