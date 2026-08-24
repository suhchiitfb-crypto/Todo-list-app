tasks = [
    {"title": "Swimming", "done": False},
    {"title": "Reading", "done": True}
]

for task in tasks:
    status = "✓" if task["done"] else " "
    print("[" + status + "] " + task["title"])