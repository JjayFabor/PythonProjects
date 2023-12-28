# Task Tracker

A simple command-line task tracker written in Python.

## Getting Started

### Prerequisites

- Python 3.7

## Installation

**Go to the folder where you want to try the project**

   ```bash
   cd TaskTracker 
   ```

## Usage

### Adding a task
To add the a new task, use the following command:
```bash
        python task_tracker.py add --title "Task 1" --description "Description of Task 1" --due "2023-12-31" 
```

* Options:
    * `-t` or `title`: Title of the task (required).
    * `--description` or `-d`: Description of the task (required).
    * `--due`: Due date of the task (optional).

### Listing Tasks
To list all the tasks, use the following command:
```bash
    python task_tracker.py list
```

## Command Line Options

### **`add`**
Add a new task to the task tracker.

### **`list`**
List all tasks in the tracker