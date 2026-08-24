import json

tasks = ["Swimming", "Reading"]

with open("tasks.json", "w") as file:
    json.dump(tasks, file)

print("Saved!")
import json

with open("tasks.json", "r") as file:
    loaded_tasks = json.load(file)

print(loaded_tasks)
print(type(loaded_tasks))