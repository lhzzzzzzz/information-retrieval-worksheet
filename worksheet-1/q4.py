def output_style(dictionary):
    print("--------------------")
    for key, value in dictionary.items():
        print(f"{value}: {key}")
    print("--------------------")

with open('words.txt', 'r', encoding="utf-8") as f:
    words_dict = {}
    for line in f:
        line = line.casefold().strip()
        if line:
            line = line.casefold()
            words = line.split(" ")
            for word in words:
                word = word.strip()
                if word in words_dict:
                    num = words_dict.get(word)
                    words_dict[word] = num + 1
                else:
                    words_dict[word] = 1

output_style(words_dict)
