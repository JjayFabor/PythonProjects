# Task Tracker

A simple command-line task tracker written in Python.

## Getting Started

### Prerequisites

- Python 3.7 or higher

## Installation

**Go to the folder where you want to try the project**

   ```bash
   cd TaskTracker
   pip install -r requirements.txt
   ```

## Usage

### Adding a task
To add the a new task, use the following command:
```bash
        python task_tracker.py add --title "Task 1" --description "Description of Task 1" --due "2023-12-31" 
```

* Options:
    * `title`: Title of the task (required).
    * `--description` or `-d`: Description of the task (required).
    * `--date`: Due date of the task in the format YYYY-MM-DD (optional, defaults to tomorrow's date if not provided).
    * `--time`: Due time of the task in the format HH:MM (optional).
    * `--priority` or `-p`: Priority of the task  (optional: 'Low | Medium | High',  defaults to "Low" if not provided).

### Listing Tasks
To list all the tasks, use the following command:
```bash
    python task_tracker.py list
```
### Deleting a Task
To delete a specific task, use the following command:
```bash
    python task_tracker.py delete 'Task 1'
```

### Deleting all the task (Delete the file for the tasks)
To delete all the tasks for the day or delete the text file, use the following command:
```bash
    python task_tracker.py delete-all
```

# Command Line Options

### **`add`**
Add a new task to the task tracker.

### **`list`**
List all tasks in the tracker

### **`delete`**
Delete or remove a specific task.

* Options: 
    - `title`: Title of the task to be deleted.

### **`delete-all`**
Delete the file or delete all tasks.