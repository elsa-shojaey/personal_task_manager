name = input("Enter your name: ")
print(f"Welcome, {name}")

tasks = []
while True:
    task = input("Enter a task or type 'done' to finish: ")
    if task.lower() == "done":
        break
