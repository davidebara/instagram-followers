from bs4 import BeautifulSoup

def extract_usernames(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    usernames = []
    for div in soup.find_all('div', class_='pam _3-95 _2ph- _a6-g uiBoxWhite noborder'):
        username_div = div.find('div').find('div').find('div').find('a')
        if username_div:
            username = username_div.text.strip()
            usernames.append(username)

    return usernames

def write_to_txt(usernames, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for username in usernames:
            file.write(username + '\n')

if __name__ == "__main__":
    # Input files
    followers_input = "followers_1.html"
    following_input = "following.html"
    
    # Output files
    followers_output = "followers.txt"
    following_output = "following.txt"

    followers = extract_usernames(followers_input)
    following = extract_usernames(following_input)

    write_to_txt(followers, followers_output)
    write_to_txt(following, following_output)
    print(f"Usernames written to {followers_output} and {following_output}")
