import argparse
from datetime import datetime, timedelta
import os

def addTask(args):
    """
    Add a task to the task tracker.

    Args:
        args: The parsed command-line arguments.

    Raises:
        argparse.ArgumentTypeError: If required arguments are not provided.
    """
    if not args.description:
        raise argparse.ArgumentTypeError('Description is required')
    if not args.time:
        raise argparse.ArgumentTypeError('Time is required')
    if args.priority == 'Low':
        pass
    elif args.priority == 'Medium':
        pass
    elif args.priority == 'High':
        pass
    else:
        raise argparse.ArgumentTypeError('Invalid priority')
    
    title = findNextAvailableTaskTitle()

    task_info = ' | '.join([title, args.description, args.date, args.time, args.priority])
    with open('tasks.txt', 'a') as f:
        f.write(task_info + '\n')
        print(f'Successfully added task: {title}')


def findNextAvailableTaskTitle():
    # Initialize a counter for task titles
    counter = 1

    try:
        with open('tasks.txt', 'r') as f:
            # Check existing task titles
            existing_titles = [line.split('|')[0].strip() for line in f.readlines()]

            # Find the highest task index
            existing_indices = [int(title.split()[-1]) for title in existing_titles if title.startswith('Task')]
            highest_index = max(existing_indices) if existing_indices else 1

            # Start incrementing from the highest index
            counter = highest_index + 1

    except FileNotFoundError:
        # Create the file if it doesn't exist
        with open('tasks.txt', 'w') as f:
            pass

    # Find the next available task title
    title = f'Task {counter}'
    return title


def listTask(args):
    """
    List all tasks in the task tracker.

    Args:
        args: The parsed command-line arguments.
    """
    print(f'Listing all tasks: \n')
    try: 
        with open('tasks.txt', 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print('No tasks for the day.')

def deleteTask(args):

    try:
        index_to_delete = None
        # Read tasks from the file
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()

        # Print current tasks
        print('Current tasks:')
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        for i, task in enumerate(tasks, start=1):
            if args.title in task:
                index_to_delete = i
                break
        if index_to_delete is None:
            print(f'Task {args.title} not found.')

        # Validate the index
        if index_to_delete is not None:
            # Remove the selected task
            deleted_task = tasks.pop(index_to_delete - 1)

            # Update the tasks file
            with open('tasks.txt', 'w') as f:
                f.writelines(tasks)

            print(f'Successfully deleted task: {deleted_task.strip()}')
        else:
            print(f'No task with title "{args.title}" found. No task deleted.')

    except FileNotFoundError:
        print('No tasks for the day.')
        

def deleteAllTask(args):
    try: 
        os.remove('tasks.txt')
    except FileNotFoundError:
        print('No tasks for the day.')


def notifyUpcomingTasks():
    """
    Notify the user of upcoming tasks.
    """
    try: 
        # Read tasks from the file
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()
        
        timeNow = datetime.now()

        for task in tasks:

            # Parse the due date and time from the task
            _, _, due_date, due_time, _ = task.split('|')
            due_datetime = datetime.strptime(f'{due_date.strip()} {due_time.strip()}', '%Y-%m-%d %H:%M')

            # Calculate the time difference
            time_difference = due_datetime - timeNow

            # Notify if the task is due within the next 1 hour
            if 0 <= time_difference.total_seconds() <= 1 * 3600:
                notification_title = 'Upcoming Task'
                notification_message = f'Task "{task}" is due soon!'
                print(f'{notification_title}: {notification_message}')

    except FileNotFoundError:
        pass


def main():
    parser = argparse.ArgumentParser(prog='Task Tracker with Command-Line', description='Command-line Task Tracker')
    subparser = parser.add_subparsers(dest='command', help='Command to perform')

    # subparser to perform 'Add task'
    add_parser = subparser.add_parser('add', help='Add a task')
    add_parser.set_defaults(func=addTask)
    add_parser.add_argument('-d', '--description', type=str, help='Description of the task')
    add_parser.add_argument('--date', type=str, help='Due date of the task (format: YYYY-MM-DD)', default=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))
    add_parser.add_argument('--time', type=str, help='Due time of the task (format: HH:MM)')
    add_parser.add_argument('-p','--priority', type=str, help='Priority of the task (default: Low)', default='Low')

    # subparser to perform 'List all the task'
    list_parser = subparser.add_parser('list', help='List all tasks')
    list_parser.set_defaults(func=listTask)

    # subparser to perform 'Delete or remove a task'
    delete_parser = subparser.add_parser('delete', help='Delete or remove a task')
    delete_parser.set_defaults(func=deleteTask)
    delete_parser.add_argument('title', type=str, help='Title of the task')
    
    # subparser to 'Delete the file or Delete all the tasks'
    delete_all_parser = subparser.add_parser('delete-all', help='Delete the file or Delete all the tasks')
    delete_all_parser.set_defaults(func=deleteAllTask)


    args = parser.parse_args()


    if hasattr(args, 'func'):
        args.func(args)
        if args.command == 'list' or args.command == 'add':
            notifyUpcomingTasks() # notify after listing or adding tasks
    else:
        print('Invalid command. Use "add" or "list".')


if __name__ == '__main__':
    main()