# Personal Task Manager 
![Static Badge](https://img.shields.io/badge/python-3.12-blue)


A simple Personal Task Manager built with Python
## Table of contents


- [Features](#features)
- [Project Structure](#project-structure)
- [Requirments](#requirments)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Screenshots](#screen-shot)
- [Roadmap](#roadmap)
- [Author](#author)

## Features
- Task Management
  - Gets the user's name .
  - Allows the user to add multiple tasks .
  - Displays the tasks entered by the user .
- Task Storage
  - Saves the user's tasks in a `tasks.txt` file .
- Admin Mode
  - asks for the admin password .
  - checks if the password is correct .
  - keeps the private information  outside the main python file .
  - Loads the password from `.env` .

## Project Structure
```text
C:.
│   .env.example
│   .gitignore
│   main.py
│   tasks.py
│   README.md
│   requirements.txt
│
├───gifs
│       demo.gif
│
├───pictures
│       1.png
│       2.png
│       3.png
└───
```
### File Description
| file | description |
| --- |---|
| `main.py` | main file used to run program|
| `question.py` | Contains task-related functions .|
| `requirements.txt` | Lists the external Python packages required by the project. |
| `.env.example` | Shows the environment variable required for Admin Mode .|
| `.gitignore` | tells git which files and folders shold not be tracked|
| `README.md` | contains the project documentation|
| `pictures/` | stores project screenshots|
| `pictures\1.png` | screenshot of the game start|
| `pictures\2.png` | screenshot of the task section|
| `pictures\3.png` | screenshot of final result|
| `gifs/` | stores demo GIF files|
| `gifs/demo.gif` | shows the project demo|


## Requirements
Before running the project, make, sure you have:
- `python 3`
- `python-dotenv`


## Installation
1. open a terminal in the project folder.
2. check that python is installed:
```bash 
python --version
```
3. install the python packages:
```bash 
pip install -r requirements.txt
```
## Environment Setup
1. creat a `.env` file from `.env.example`:
```bash
cp .env.example .env
```
2. open the new `.env` file 
3. replace the example value with your own password 
```text
QUIZ_ADMIN_PASSWORD=your_password_here
```
4. save the file.
> Do not commit your `.env` file because it may contain private information

## Usage
1. open a terminal in the project folder 
2. run the program: 
```bash
python main.py
```
3. choose `yes` or `no` for admin mode
4. if you choose `yes`, enter the password from your `env` file
5. enter your name 
6. Add tasks one by one.
7. Type `done` when you finish adding tasks .
8. View your tasks .

## Example Output
```text
do u want to open admein mode ? yes/no: no

Enter your name: elsa
Welcome, elsa

Enter a task or type 'done' to finish: hello

Enter a task or type 'done' to finish: how are you

Enter a task or type 'done' to finish: done

Your tasks:
- hello
- how are you
```

## Screenshots
### Admin Mode
![start game](pictures\1.png)

### Adding and Display Tasks
![quiz](pictures\2.png)

### Final Result 
![final score](pictures\3.png)

## Demo
![quiz game demo](gifs\demo.gif)

## Roadmap
- [x] Get the user's name .
- [x] Add multiple tasks .
- [x] Display entered tasks .
- [x] Add Admin Mode
- [x] Load the admin password from `.env` .
- [x] Save task information to a file .
- [ ] Edit existing tasks .
- [ ] search for a task by name .

## Author

created by [elsa shojaey](https://github.com/elsa-shojaey)