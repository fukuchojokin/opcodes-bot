def search(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return line[-3:]
        return 'Does not match!'


def take_input():
    to_search = input("Enter string to search: ").upper()
    result = search("opcodes8085.txt", to_search)
    print(result)
    take_input()


if __name__ == '__main__':
    take_input()
