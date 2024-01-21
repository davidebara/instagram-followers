# Instagram followers and following

This repository contains two Python scripts:

1. **retrieve.py**: A script that extracts usernames from an HTML file containing Instagram data.
2. **compare.py**: A script that compares elements in `followers.txt` and `following.txt` and displays elements exclusively in each file.

## Requirements

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Setup

1. After downloading your data from Meta, move these two scripts inside the `followers_and_following` folder. The folder structure should look something like this:

   ```
   connections/followers_and_following
   ```

2. Install required libraries
    ```bash
    pip install beautifulsoup4
    ```

3. Change file names inside the `retrieve.py` file (Optional)
    

## Usage
### HTML Parser
Run the `retrieve.py` script to extract usernames from an HTML file.
```bash
python html_parser.py
```

### File comparator
Run the `compare.py` script to compare elements in `followers.txt` and `following.txt`.
```bash
python file_comparator.py
```
The exclusive elements will be written to `users.txt`.