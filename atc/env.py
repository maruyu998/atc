import os
ENVPATH = f'{os.path.dirname(__file__)}/env'

def _parse_env()->dict:
    envs = {}
    with open(ENVPATH) as f:
        for line in f:
            _name, _value = line.rstrip().split('=')
            envs[_name] = _value
    return envs

def _write_env(env:dict)->None:
    with open(ENVPATH, 'w') as f:
        for _name, _value in env.items():
            f.write(f'{_name}={_value}\n')

def _confirm_set(envs:dict, name:str, value:str)->None:
    import sys
    if name not in envs: 
        inp = input(f'set env "{name}" \033[92m{value}\033[0m, is it ok? [Y/n] ').strip()
        if inp not in ["Y",""]: sys.exit()
    elif envs[name] == value:
        print(f'env "{name}" is already {value}. exit.')
        sys.exit()
    else:
        inp = input(f'set env "{name}" from \033[93m{envs[name]}\033[0m to \033[92m{value}\033[0m, is it ok? [Y/n] ').strip()
        if inp not in ["Y",""]: sys.exit()

def _confirm_delete(envs:dict, name:str)->None:
    import sys
    if name not in envs:
        print(f'env "{name}" is not set')
        sys.exit()
    else:
        inp = input(f'env "{name}" is to deleted, is it ok? [Y/n] ').strip()
        if inp not in ["Y",""]: sys.exit()

def show_env(name:str=None):
    print_env = lambda n,v: print(f'{n} = {v}')
    envs = _parse_env()
    if name == None:
        for n,v in envs.items(): print_env(n,v)
        exit(0)
    name = name.upper()
    if name not in envs:
        print(f'env "{name}" is not set')
    else:
        print_env(name, envs[name])

def set_env(name:str, value:str):
    name = name.upper()
    envs = _parse_env()
    _confirm_set(envs, name, value)
    envs[name] = value
    _write_env(envs)

def delete_env(name:str):
    name = name.upper()
    envs = _parse_env()
    _confirm_delete(envs, name)
    del envs[name]
    _write_env(envs)