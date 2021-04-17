#!/usr/bin/env python
def main():
    import argparse
    parser = argparse.ArgumentParser(description="atcoder auto example fetching and code evaluation")
    subparsers = parser.add_subparsers(dest='action')

    start_parser = subparsers.add_parser('start', help='create base files and wait for start time and then fetch sample cases')
    start_parser.add_argument('contest_name', help='contest name ex) arc114', nargs='?')
    
    create_parser = subparsers.add_parser('create', help='create base files which contain utility files')
    create_parser.add_argument('contest_name', help='contest name ex) arc114', nargs='?')

    wait_parser = subparsers.add_parser('wait', help='countdown to start contest')
    wait_parser.add_argument('contest_name', help='contest name ex) arc114', nargs='?')

    fetch_parser = subparsers.add_parser('fetch', help='fetch sample cases')
    fetch_parser.add_argument('contest_name', help='contest name ex) arc114', nargs='?')

    case_parser = subparsers.add_parser('case', help='input sample cases and answers')
    case_parser.add_argument('level', help='level character')
    case_parser.add_argument('case', help='case character')

    eval_parser = subparsers.add_parser('eval', help='evaluate your code')
    eval_parser.add_argument('level', help='level character to evaluate')
    eval_parser.add_argument('case', help='case character', nargs='?')

    run_parser = subparsers.add_parser('run', help='run the code')
    run_parser.add_argument('level', help='level character to evaluate')

    env_parser = subparsers.add_parser('env', help='set environments')
    env_subparser = env_parser.add_subparsers(dest='env_action')
    show_env_parser = env_subparser.add_parser('show')
    show_env_parser.add_argument('name', nargs='?')
    set_env_parser = env_subparser.add_parser('set')
    set_env_parser.add_argument('name')
    set_env_parser.add_argument('value')
    delete_env_parser = env_subparser.add_parser('delete')
    delete_env_parser.add_argument('name')

    where_parser = subparsers.add_parser('where', help='find some files')
    where_parser.add_argument('file_type', choices=['env','base','utils'])

    args = parser.parse_args()

    if args.action == None:
        parser.print_help()
    
    elif args.action == 'start':
        from .create import create
        create(args.contest_name)
        from .wait import wait
        wait(args.contest_name)
        from .fetch import fetch
        fetch(args.contest_name)
    
    elif args.action == 'create':
        from .create import create
        create(args.contest_name)
    elif args.action == 'wait':
        from .wait import wait
        wait(args.contest_name)
    elif args.action == 'fetch':
        from .fetch import fetch
        fetch(args.contest_name)

    elif args.action == 'case':
        from .case import case
        case(args.level, args.case)

    elif args.action == 'eval':
        from .eval import eval
        eval(args.level, args.case)

    elif args.action == 'run':
        from .eval import run
        run(args.level)

    elif args.action == 'env':
        if args.env_action == None:
            env_parser.print_help()
        elif args.env_action == 'show':
            from .env import show_env
            show_env(args.name)
        elif args.env_action == 'set':
            from .env import set_env
            set_env(args.name, args.value)
        elif args.env_action == 'delete':
            from .env import delete_env
            delete_env(args.name)
        else:
            raise NotImplementedError

    elif args.action == 'where':
        if args.file_type == 'env':
            from .env import ENVPATH
            print(ENVPATH)
        elif args.file_type == 'base':
            from .create import BASEPATH
            print(BASEPATH)
        elif args.file_type == 'utils':
            from .create import UTILSPATH
            print(UTILSPATH)

    else:
        raise NotImplementedError

if __name__ == "__main__":
    main()