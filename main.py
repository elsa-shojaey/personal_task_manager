import os
from dotenv import load_dotenv
from tasks import add_task, display_tasks
load_dotenv()
admin_password = os.getenv("QUIZ_ADMIN_PASSWORD")
open_admin = input("do u want to open admein mode ? yes/no:")
if open_admin.lower() == "yes":
    entered_password = input("enter admin password")
    if entered_password == admin_password:
        print("admin! hi...")
    else:
        print("wrong password")
name = input("Enter your name: ")
print(f"Welcome, {name}")
tasks = []
while True:
    task = input("Enter a task or type 'done' to finish: ")
    if task.lower() == "done":
        break
        add_task(tasks, task)
display_tasks(tasks)

with open("tasks.txt", "a") as file:
    file.write(f"{name} - {tasks}\n") 