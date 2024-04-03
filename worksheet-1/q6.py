def output_style(dictionary):
    print("--------------------")
    for key, value in dictionary:
        print(f"{key}: {value}")
    print("--------------------")

with open('preprocessed_documents.txt', 'r', encoding='utf-8') as f:
    words_dict = {}
    for line in f:
        line = line.casefold().strip()
        if line:
            words = line.split()
        file_id = words[0]
        file_info = words[1:]
        for word in file_info:
            word = word.strip()
            if word in words_dict:
                if file_id not in words_dict[word]:
                    words_dict[word].append(file_id)
            else:
                words_dict[word] = [file_id]
            
output_style(sorted(words_dict.items(), key=lambda item: item[0], reverse=False))
