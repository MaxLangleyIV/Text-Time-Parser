# Timestamp Parser

The Timestamp Parser is a Python script that allows you to extract durations from a text file containing timestamps. It's particularly useful for tasks like podcast editing, where you want to associate specific images with their starting timestamps.

## Table of Contents
- [Description](#description)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Files](#files)
- [Contributing](#contributing)
- [License](#license)

## Description

The Timestamp Parser is a utility designed to work with timestamped text files, commonly used in podcast editing or other media production workflows. It extracts the timestamps and calculates the duration between each entry to provide an overview of each segment's length.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/MaxLangleyIV/TimestampParser.git

2. Ensure you have Python installed on your system.

3. Open a terminal and navigate to the project directory: "cd ...\TimestampParser"

##Usage
Place your timestamped text file (e.g., ExampleText.txt) in the same directory as TimestampParser.py.

Open a terminal and run the script:

python TimestampParser.py
Follow the prompts:

Enter the name of the text file to scan.
Enter the duration of the audio file in the format minutes:seconds.

The script will process the provided text file and display the durations associated with each timestamp.

##Files
TimestampParser.py: Contains the core functions for parsing timestamps and calculating durations.

ParserUseExample.py: Provides an example of how to use the Timestamp Parser with your own input.

ExampleText.txt: A sample text file with timestamps for demonstration purposes.