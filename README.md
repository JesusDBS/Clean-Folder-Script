# Clean-Folder-Script
A simple Python script for cleaning your folders.

## Description
This is a simple script written in Python that allows you to delete all the files of a folder effortlessly, also you can delete inner folders. It is especially useful for **cleaning your Downloads folder**.

## Usage
To use this script you need to follow these instructions:
1. Fork this repository
2. Clone your forked repository in your local machine
3. Create a `config.json` file and add the following keys:
```JavaScript
{
    "dir_path": ["absolute", "path", "to", "your", "folder"],
    "remove_folders_too": true
}
```
4. Add your `config.json` file in the root of this project
5. Open a terminal and run the main.py script as follows:
```
python main.py
```
---
**Note**: The path to your folder **has to be absolute** for the script to find it.

**Note**: If you don't want to delete the folders contained in the folder to be cleaned make sure `remove_folders_too` key is set to `false`. 

## Contributing
This project is open to improvements. If you think you can improve this project, please make a pull request explaining your changes and why they are worth to be integrated..

## License
[MIT](https://choosealicense.com/licenses/mit/)