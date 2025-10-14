class Task:

    def __init__(self, title, done=False):
        self.title = title
        self.done = done
    
    def mark_done(self):

        """Mark the task as finished."""
        self.done = True

    def mark_undone(self):
        """Mark the task as unfinished."""
        self.done = False
    
    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.title}"