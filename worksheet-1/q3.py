with open('words.txt', 'r', encoding="utf-8") as f:
    for line in f:
        line = line.casefold()
        words = line.split(" ")
        for word in words:
            print("(" + word.strip() + ")", end=" ")
        print()