def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    words = file_contents.split()
    word_count = len(words)
    print(word_count)
   
    lowercase_file = file_contents.lower()
    monster_count = lowercase_file.count("monster")
    frankenstein_count = lowercase_file.count("frankenstein")
    creature_count = lowercase_file.count("creature")
    print(monster_count)
    print(frankenstein_count)
    print(creature_count)
   
    character_num = {}
    for character in lowercase_file:
        if character not in character_num:
            character_num[character] = 1
        else:
            character_num[character] += 1
    print(character_num)


    character_list = [{"char": char, "num": num} for char, num in character_num.items() if char.isalpha()]
    character_list.sort(key=lambda entry: entry["num"], reverse=True)
    for entry in character_list:
        char = entry["char"]
        num = entry["num"]
        print(f"The '{char}' character was found {num} times")


main()

