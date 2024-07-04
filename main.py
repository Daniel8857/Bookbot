def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = word_count(file_contents)
    characters = unique_characters(file_contents)
    char_list = dict_to_list(characters)
    report = sort_report(char_list)
    print_report(report, words)
    return
    
def word_count(text_file):
    words = text_file.split()
    return len(words)

def unique_characters(text_file):
    chars = {}
    lowered_text = text_file.lower()
    for c in lowered_text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 0

    return chars

def dict_to_list(dict):
    list = []
    for entry in dict:
        if entry.isalpha():
            list.append({"char": entry,"num": dict[entry]})
    return list

def sort_report(list):
    def sort_on(dict):
        return dict["num"]
    
    list.sort(reverse=True, key=sort_on)
    return list

def print_report(report, words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print()
    for dict in report:
        print(f"The '{dict['char']}' character was found {dict['num']} times")
    print()
    print("--- End report ---")
    return

main()