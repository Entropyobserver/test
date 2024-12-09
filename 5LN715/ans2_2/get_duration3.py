import json

def get_lines(path):
    with open(path, 'r',encoding= 'utf-8') as f:
        lines = f.readlines()
    return lines

def get_duration(lines):
    id_durations = {}
    for line in lines:
        columns = line.split(';')
        try:
            if len(columns) > 6: # makes sure cloumn1 to column5 are valid lines
                if columns[1].strip().isdigit():#duration in column1,makes sure it is a number
                    
                    word = columns[5].strip().lower()# word in column5
                    #word = columns[5].strip()# word in column5
                    duration = int(columns[1])/24/10000# MAUS,the duration is in Hertz (Hz). To convert this duration into seconds, divide the Hertz value by the sampling rate (the number of samples per second).
                    if word in id_durations:
                        id_durations[word] += duration
                    else:
                        id_durations[word] = duration
        except Exception as e:
            print(f"Error: {e}")
    return id_durations

def save_to_json(data, path): 
    with open(path, 'w') as f: 
        json.dump(data, f, indent=4)#formatting it with a 4-space indentation for each level of nested data

if __name__ == "__main__":
    #path = '/home/yaxi4987/5LN715/ans2/merged.csv'
    #path = r'D:\J\Desktop\language technology\s\5LN715\ans2\merged.csv'
    #path = r'D:\J\Desktop\language technology\course\ans2 copy\sentence_15.csv'
    path = r"D:\J\Desktop\language technology\course\ans2 copy\sentence_15.csv"
    lines = get_lines(path)
    #print(lines[:10])
    durations = get_duration(lines)
    #print(durations)
    #for key, value in durations.items(): 
    #    print(f"{key}: {value}")
    #cat sentence_*.csv > merged.csv
    #cat sentence_*.txt > merged.txt
    json_path = r'D:\J\Desktop\language technology\course\ans2 copy\duration15.json' 
    save_to_json(durations, json_path)
    print("Done")