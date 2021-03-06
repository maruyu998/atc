from .contest import get_contest_name, fetch_html, get_session
from .contest import _parse_levels, _save_levels, _read_levels
from datetime import timedelta

def parse_start_time(html):    
    import re
    start_time = re.findall(r'var startTime = moment\(\"(.*?)\"\);', html)
    if len(start_time)==0: 
        print('could not find start time') 
        exit(0)
    else:
        from dateutil.parser import parse
        start_time = parse(start_time[0])
    return start_time

def wait(contest_name:str=None, require_session:bool=False):
    contest_name = get_contest_name(contest_name)
    url = f'https://atcoder.jp/contests/{contest_name}'
    html = fetch_html(url)
    start_time = parse_start_time(html)
    if _read_levels() == None:
        _save_levels(_parse_levels(html))
    from datetime import datetime, timezone, timedelta
    now = datetime.now(timezone(timedelta(hours=+9), 'JST'))
    import time
    session = None
    while now < start_time:
        now = datetime.now(timezone(timedelta(hours=+9), 'JST'))
        print(f"{int((start_time - now).total_seconds())} seconds left        ", end="\r")
        if session == None and now > start_time - timedelta(minutes=3):
            session = get_session()
        time.sleep(1)
    return session