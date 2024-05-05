import os
import re
import sys


def search_text_in_files(folder_path, search_text):
    log_files = [file for file in os.listdir(folder_path) if file.endswith(".log")]

    for log_file in log_files:
        with open(os.path.join(folder_path, log_file), 'r') as file:
            line_number = 0
            for line in file:
                line_number += 1
                if search_text in line:
                    print(f"Text '{search_text}' found in file: {log_file}, line number: {line_number}")
                    words = re.split(r'\s+', line)
                    index = words.index(search_text)
                    start_index = max(0, index - 5)
                    end_index = min(len(words), index + 6)
                    context = " ".join(words[start_index:end_index])
                    print(f"Context: {context}")


if len(sys.argv) < 4:
    print("Usage: analyzer.py <folder> --text <search_text>")
    sys.exit(1)

folder_path = sys.argv[1]
search_text = sys.argv[3]

search_text_in_files(folder_path, search_text)
