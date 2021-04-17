import sys, os

def _store_inputs():
    while True:
        line = input()
        if line == "": break
        inputs.append(line)
    return inputs

def _write_inputs(file_path:str, inputs:[str]):
    with open(file_path, 'w') as f:
        for ex in inputs:
            f.write(ex)
            f.write("\n")

def case(level:str, case:str):
    directory = f'testcases/{level}'
    os.makedirs(directory, exist_ok=True)
    print(f"input sample case input {case} >>>")
    inputs = _store_inputs()
    print(f"input sample case output {case} >>>")
    outputs = _store_inputs()

    _write_inputs(f'{directory}/ex{case}.txt', inputs)
    _write_inputs(f'{directory}/out{case}.txt', outputs)
    print(f"ex{case}.txt and out{case}.txt have been written")