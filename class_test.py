class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✓" if self.done else " "
        return "[" + status + "] " + self.title

    def to_dict(self):
        return {"title": self.title, "done": self.done}

t1 = Task("Swimming")
t1.mark_done()
print(t1.to_dict())