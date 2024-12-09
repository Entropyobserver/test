import json

def get_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def get_duration(lines):
    """
    The get_duration function processes a list of lines from a file, extracts the duration of each word,
    and stores the  duration for each word and each sentence in a dictionary.
    The function assumes that the duration is provided in Hertz (Hz) and converts it to milliseconds.
    Parameters:
    lines: A list of strings, where each string represents a line from the input file.
    Returns:
    id_durations: A dictionary where the keys are words (in lowercase) and the values are the cumulative durations of those words in milliseconds.
    """
    id_durations = {}
    for line in lines:
        columns = line.split(';')
        try:
            if len(columns) > 6:  # makes sure column1 to column5 are valid lines
                if columns[1].strip().isdigit():  # duration in column1, makes sure it is a number
                    word = columns[5].strip().lower()  # word in column5
                    duration = int(columns[1]) / 24   # MAUS, the duration is in Hertz (Hz). To convert this duration into miliseconds, divide the Hertz value by the sampling rate .
                    if word in id_durations:
                        id_durations[word] += duration
                    else:
                        id_durations[word] = duration
        except Exception as e:
            print(f"Error: {e}")
    return id_durations


def save_to_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)  # formatting it with a 4-space indentation for each level of nested data

if __name__ == "__main__":
    # path = '/home/yaxi4987/5LN715/ans2/merged.csv'
    # path = r'D:\J\Desktop\language technology\s\5LN715\ans2\merged.csv'
    # path = r'D:\J\Desktop\language technology\course\ans2 copy\sentence_15.csv'
    path = r"D:\J\Desktop\language technology\course\ans2 copy\sentence_15.csv"
    lines = get_lines(path)
  
    word_duration = get_duration(lines)
    for key, value in word_duration.items():
        print(f"{key}: {value}")
        
    json_path = r'D:\J\Desktop\language technology\course\ans2 copy\word_duration15.json'
    save_to_json(word_duration, json_path)

    sentence_duration = sum(word_duration.values())
    print(f"Total Duration: {sentence_duration} seconds")

    json_path = r'D:\J\Desktop\language technology\course\ans2 copy\sentence_duration15.json'
    save_to_json(sentence_duration, json_path)
    print("Done")
