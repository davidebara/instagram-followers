def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().splitlines()
    return set(content)

def compare_and_write_to_file(file1, file2, output_file):
    followers = read_file(file1)
    following = read_file(file2)

    followers_exclusive = followers - following
    following_exclusive = following - followers

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Elements exclusively in followers.txt:\n")
        for element in followers_exclusive:
            file.write(element + '\n')

        file.write("\nElements exclusively in following.txt:\n")
        for element in following_exclusive:
            file.write(element + '\n')

if __name__ == "__main__":
    followers_file = "followers.txt"
    following_file = "following.txt"
    output_file = "users.txt"

    compare_and_write_to_file(followers_file, following_file, output_file)
    print(f"Exclusive elements written to {output_file}")
