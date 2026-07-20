import csv
import os

# Global in-memory list to store tasks
todos = []

def add_one_task(title):
    """Appends a new task dictionary to the in-memory list."""
    todos.append({"title": title})

def print_list():
    """Displays all pending tasks with their numeric positions."""
    for index, task in enumerate(todos, start=1):
        print(f"{index}. {task['title']}")

def delete_task(number_to_delete):
    """Removes a task from the list using its 1-based index position."""
    if 0 < number_to_delete <= len(todos):
        todos.pop(number_to_delete - 1)
    else:
        print("Invalid task number.")

def save_todos():
    """Persists current tasks into a todos.csv file."""
    with open("todos.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for task in todos:
            writer.writerow([task["title"]])

def load_todos():
    """Reads tasks from todos.csv back into the in-memory list."""
    if os.path.exists("todos.csv"):
        todos.clear()
        with open("todos.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    todos.append({"title": row[0]})

if __name__ == "__main__":
    print("Todo List CLI Started")
    
    # Test adding tasks
    add_one_task("Buy groceries")
    add_one_task("Walk the dog")
    
    # Test printing the list
    print("\nCurrent Tasks:")
    print_list()
    
    # Test saving tasks to CSV
    save_todos()
    print("\nTasks saved to todos.csv successfully!")