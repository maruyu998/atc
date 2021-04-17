import os, subprocess, time

def _exist_check(path:str)->str:
    if not os.path.exists(path):
        print(f"create {path} first, use atc case or atc fetch")
        exit(0)
    return path

def _get_answer(level:str, case:str):
    path = _exist_check(f"testcases/{level}/out{case}.txt")
    with open(path) as f:
        answer = [line.strip() for line in f.readlines()]
    return answer

def _exact_same(results:[str], answer:[str]):
    if len(results) != len(answer): return False
    for r,a in zip(results, answer):
        if r!=a: return False
    return True

def _run_command(command, *, stdin, stdout):
    start = time.perf_counter()
    ret = subprocess.run(command,
        stdin=stdin,
        encoding='utf-8',
        stdout=stdout,
        stderr=subprocess.PIPE
    )
    end = time.perf_counter()
    return ret, end-start

def _get_command(level:str):
    from dotenv import load_dotenv
    load_dotenv(f'{os.path.dirname(__file__)}/env')
    runner = os.environ.get("RUNNER")
    if runner == "": 
        print('env "RUNNNER" is not set. please use atc env set runnner {your runner}')
        exit(0)
    command = [runner, f"./{level}.py"]
    return command

def _run_case(level:str, case:str):
    command = _get_command(level)
    print("run ========++")
    case_path = f'testcases/{level}/ex{case}.txt'
    print(' '.join(command + ['<', case_path]))
    path = _exist_check(case_path)
    with open(path) as f:
        ret, runtime = _run_command(command, stdin=f, stdout=subprocess.PIPE)
    if ret.stderr: print('\033[93m',end="");print(ret.stderr);print('\033[0m',end="")
    result = ret.stdout.strip().split('\n')
    return result, runtime

def _print_output(output:[str]):
    if len(output) == 0: print()
    elif len(output) == 1: print(output[0])
    else:
        print("\n>> ",end="")
        print("\n>> ".join(output))

def eval(level:str, case:str=None):
    if case == None:
        directory = f'testcases/{level}/'
        cases = sorted(list(set([
            fn.replace("ex","").replace("out","").replace(".txt","") 
            for fn in os.listdir(directory)
        ])))
    else:
        cases = [case]

    print("\033[45m"+' '*47+"\033[0m")
    for case in cases:
        print(f"++======== level {level} testcase {case} >> ", end="")
        result, runtime = _run_case(level, case)
        answer = _get_answer(level, case)

        if _exact_same(result, answer): 
            print("******\033[92mEXACTLY SAME\033[0m******", f'{runtime*1000:.0f}ms')
        else: 
            print("*****\033[91mNOT EXACT SAME\033[0m*****", f'{runtime*1000:.0f}ms')

        print("executed result  >> ", end="")
        _print_output(result)
        print("case's answer    >> ", end="")
        _print_output(answer)
        print()

def run(level:str):
    import sys
    command = _get_command(level)
    result, runtime = _run_command(command, stdin=sys.stdin, stdout=sys.stdout)
    print("\033[45m"+' '*47+"\033[0m")
    print(f'{runtime*1000:.0f}ms')