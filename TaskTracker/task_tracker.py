import argparse

def addTask(args):
    """
    Add a task to the task tracker.

    Args:
        args: The parsed command-line arguments.

    Raises:
        argparse.ArgumentTypeError: If required arguments are not provided.
    """
    if not args.title:
        raise argparse.ArgumentTypeError('Title is required')
    if not args.description:
        raise argparse.ArgumentTypeError('Description is required')
    if not args.due:
        # Due date will be set to None if not provided
        pass
    if args.priority == 'Low':
        pass
    elif args.priority == 'Medium':
        pass
    elif args.priority == 'High':
        pass
    else:
        raise argparse.ArgumentTypeError('Invalid priority')
    
    with open('tasks.txt', 'a') as f:
        f.write(f'{args.title}: {args.description} ------------ {args.due} \n')
        print(f'Successfully added task: {args.title}')

def listTask(args):
    """
    List all tasks in the task tracker.

    Args:
        args: The parsed command-line arguments.
    """
    print(f'Listing all tasks: \n')
    with open('tasks.txt', 'r') as f:
        content = f.read()
        print(content)

def main():
    parser = argparse.ArgumentParser(description='Command-line Task Tracker')
    subparser = parser.add_subparsers(dest='command', help='Command to perform')

    # subparser to perform 'Add task'
    add_parser = subparser.add_parser('add', help='Add a task')
    add_parser.set_defaults(func=addTask)
    add_parser.add_argument('-t', 'title', type=str, help='Title of the task', required=True)
    add_parser.add_argument('-d', '--description', type=str, help='Description of the task', required=True)
    add_parser.add_argument('--due', type=str, help='Due date of the task (default: None)', default=None)
    add_parser.add_argument('p','--priority', type=str, help='Priority of the task (default: Low)', default='Low')

    # subparser to perform 'List all the task'
    list_parser = subparser.add_parser('list', help='List all tasks')
    list_parser.set_defaults(func=listTask)

    args = parser.parse_args()


    if hasattr(args, 'func'):
        args.func(args)
    else:
        print('Invalid command. Use "add" or "list".')


if __name__ == '__main__':
    main()