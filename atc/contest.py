def _save_contest_name(contest_name:str=None):
    inp = input("saving contest name in .contest_name, is it ok? [Y/n] ").strip()
    if inp not in ["Y",""]: return
    with open('.contest_name','w') as f:
        f.write(contest_name)

def _guess_contest_name():
    import os, re
    for direc in reversed(os.getcwd().split('/')):
        m = re.findall(r'([a-z]{3}|[A-Z]{3}|[A-Z][a-z]{2})[^0-9]*([0-9]{3,4})', direc)
        for mm in m:
            contest_name = f'{mm[0].lower()}{mm[1]}'
            inp = input(f'guessed contest name is {contest_name}, is this right? [Y/n] ').strip()
            if inp not in ["Y",""]: continue
            return contest_name
    contest_name = input("input context name following format [a-z]{3}[0-9]{3,4} > ").strip()
    return contest_name

def _read_contest_name():
    import os
    if not os.path.exists('.contest_name'): return None
    with open('.contest_name') as f:
        contest_name = f.readline().strip()
    return contest_name

def get_contest_name(contest_name:str=None):
    if contest_name == None:
        contest_name = _read_contest_name()
    if contest_name == None:
        contest_name = _guess_contest_name()
        _save_contest_name(contest_name)
    return contest_name

def fetch_html(url:str):
    import requests
    print(f'fetching from {url}')
    page = requests.get(url)
    if page.status_code != 200:
        print(f'failed to get {url}, status {page.status_code}')
        post = url.replace('https://atcoder.jp/contests/','')
        post = '_'.join(post.split('/')[1:])
        with open(f'fail_{post}.log', 'w') as f:
            for k,v in page.__dict__.items():
                print(k, file=f)
                print(v, file=f)
                print('='*20, file=f)
        exit(0)
    return page.text

def _parse_levels(html):
    import re
    section = re.findall(r'<h3>配点</h3>[\s\t\r\n]*<section>(.*?)</section>', html, flags=re.DOTALL)
    if len(section)==0:
        print('could not find score section')
        exit(0)
    tbody = re.findall(r'<tbody>[\s\t\r\n]*(.*?)[\s\t\r\n]*</tbody>', section[0], flags=re.DOTALL)
    if len(tbody)==0:
        print('could not find score tbody')
        exit(0)
    levels = re.findall(r'<tr>[\s\t\r\n]*<td.*?>(.*?)</td>[\s\t\r\n]*<td.*?>.*?</td>[\s\t\r\n]*</tr>', tbody[0], flags=re.DOTALL)
    return levels

def _read_levels():
    import os
    if not os.path.exists('.contest_levels'): return None
    with open('.contest_levels') as f:
        levels = f.readline().strip().split(',')
    return levels

def _save_levels(levels):
    inp = input(f"saving levels info {','.join(levels)} into .contest_levels, is it ok? [Y/n] ").strip()
    if inp not in ["Y",""]: return
    with open('.contest_levels','w') as f:
        f.write(','.join(levels))

def get_levels(contest_name=None):
    levels = _read_levels()
    if levels == None:
        contest_name = get_contest_name(contest_name)
        levels = _parse_levels(fetch_html(f'https://atcoder.jp/contests/{contest_name}'))
        _save_levels(levels)
    return levels