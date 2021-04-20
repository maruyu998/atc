from .contest import get_contest_name, fetch_html, get_levels, get_session

def fetch_case(contest_name:str, level:str, session=None):
    url = f'https://atcoder.jp/contests/{contest_name}/tasks/{contest_name}_{level}'
    html = fetch_html(url, session)
    import re
    inputs = re.findall(r'<h3>入力例 ([0-9])</h3><pre>(.*?)</pre>', html, flags=re.DOTALL)
    outputs = re.findall(r'<h3>出力例 ([0-9])</h3><pre>(.*?)</pre>', html, flags=re.DOTALL)
    input_dic = {int(k): v.replace("\r\n","\n").rstrip() for k,v in inputs}
    output_dic = {int(k): v.replace("\r\n","\n").rstrip() for k,v in outputs}
    if input_dic.keys() != output_dic.keys(): 
        raise Exception("key error", input_dic, output_dic)
    return input_dic, output_dic

def make_case_file(level:str, inputs:dict, outputs:dict):
    import os
    directory = f"{os.getcwd()}/testcases/{level.upper()}"
    import os
    os.makedirs(directory, exist_ok=True)
    for i in inputs.keys():
        with open(f'{directory}/ex{i}.txt','w') as f: f.write(inputs[i])
        with open(f'{directory}/out{i}.txt','w') as f: f.write(outputs[i])
        print(f"[\033[92msample {i}\033[0m]",inputs[i],f'[output {i}]',outputs[i], sep='\n')

def fetch(contest_name:str=None, session=None):
    import time
    contest_name = get_contest_name(contest_name)
    if session==None:
        session = get_session()
    for level in get_levels():
        input_dic, output_dic = fetch_case(contest_name, level, session)
        make_case_file(level, input_dic, output_dic)
        time.sleep(1)