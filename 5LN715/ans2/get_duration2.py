def get_lines(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines

def get_duration(lines):
    id_durations = {}
    for line in lines:
        columns = line.strip().split(';')
        try:
            if len(columns) > 6:
                if columns[1].strip().isdigit():
                    word = columns[5].strip()
                    duration = int(columns[1])/24/10000
                    if word in id_durations:
                        id_durations[word] += duration
                    else:
                        id_durations[word] = duration
        except Exception as e:
            print(f"Error: {e}")
    return id_durations

if __name__ == "__main__":
    path = '/home/yaxi4987/5LN715/ans2/merged.csv'
    lines = get_lines(path)
    #print(lines[:10])
    durations = get_duration(lines)
    print(durations)
    for key, value in durations.items(): 
        print(f"{key}: {value}")
    #cat sentence_*.csv > merged.csv