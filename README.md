# atc
atcoder auto example fetching and code evaluation

## install
`pip install -U git+https://github.com/maruyu998/atc`

or 

```
git clone https://github.com/maruyu998/atc
cd atc
pip install -e .
```

## usage
```
> atc
usage: atc [-h] {start,create,wait,fetch,case,eval,run,env,where} ...

atcoder auto example fetching and code evaluation

positional arguments:
  {start,create,wait,fetch,case,eval,run,env,where}
    start               create base files and wait for start time and then fetch sample cases
    create              create base files which contain utility files
    wait                countdown to start contest
    fetch               fetch sample cases
    case                input sample cases and answers
    eval                evaluate your code
    run                 run the code
    env                 set environments
    where               find some files

optional arguments:
  -h, --help            show this help message and exit
```

```
> atc start
```

### adaptation
```
> atc where base
/home/yukimaru/.pyenv/versions/3.9.4/lib/python3.9/site-packages/atc/_base.py
> vim /home/yukimaru/.pyenv/versions/3.9.4/lib/python3.9/site-packages/atc/_base.py
# and then you can modify basefile that will be copied to your contest directory as {A,B,C,...}.py.

> atc where utils
/home/yukimaru/.pyenv/versions/3.9.4/lib/python3.9/site-packages/atc/utils
> vim /home/yukimaru/.pyenv/versions/3.9.4/lib/python3.9/site-packages/atc/utils/useful_functions.py
# and then you can add any files that will be copied to your contest directory.
```

### evaluation
```
# when you want check problem B for all sample cases
> atc eval B
++======== level B testcase 1 >> run ========++
pypy3 ./B.py < testcases/B/ex1.txt
*****NOT EXACT SAME***** 79ms
executed result  >> No
case's answer    >> Yes

++======== level B testcase 2 >> run ========++
pypy3 ./B.py < testcases/B/ex2.txt
******EXACTLY SAME****** 85ms
executed result  >> Yes
case's answer    >> Yes

++======== level B testcase 3 >> run ========++
pypy3 ./B.py < testcases/B/ex3.txt
******EXACTLY SAME****** 107ms
executed result  >> No
case's answer    >> No
```
```
# when you want check problem B for specific cases like 2
> atc eval B 2
++======== level B testcase 2 >> run ========++
pypy3 ./B.py < testcases/B/ex2.txt
******EXACTLY SAME****** 87ms
executed result  >> Yes
case's answer    >> Yes
```

### run
`atc eval` command waits for whole execution, so if there is infinite loop, `atc eval` command doesn't end and output nothing.

`atc run` command is just run the command and output result into stdout directory.

```
> atc run B
123000 # this is input
No # output

4627ms # runtime
```
