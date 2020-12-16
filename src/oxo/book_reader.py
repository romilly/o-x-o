import os
import itertools
import re
from typing import List

import nbformat

notebook_dir = '../../menace'

WORDS = re.compile(r'[a-z]+')


def listify(source):
    return source if isinstance(source, list) else [source]


def notebook_contents(notebook_file):
    with open(notebook_file) as book:
        nb = nbformat.read(book, as_version=4)
        return [listify(cell.source) for cell in nb.cells if cell.cell_type == 'code']


def all_contents(dir: str):
    result = {}
    for nb_file in sorted(os.listdir(dir)):
        nb_path = os.path.join(dir, nb_file)
        if os.path.isfile(nb_path) and nb_file.endswith('.ipynb'):
            result[nb_file] = list(itertools.chain.from_iterable(notebook_contents(nb_path)))
    return result


def names_in(value: str) -> List[str]:
    return WORDS.findall(value)


def analyze(lines: List[str]):
    fndefs = {}
    vardefs = {}
    for line in lines:
        code = line.split('⍝')[0]
        splitter = code.index('←')
        name = code[:splitter].strip()
        value = code[splitter+1:].strip()
        if name[0] in '+⊢⍴÷':
            name = name[1:].strip()
        defs = fndefs if value.endswith('}') else vardefs
        defs[name] = names_in(value)
    return fndefs, vardefs


def code_in(dir: str):
    result = []
    contents = all_contents(dir)
    for key in contents.keys():
        items = contents[key]
        for item in items:
            if len(item) > 0:
                for line in item.split('\n'):
                    if '←' in line and not line.startswith('⎕io'):
                        result.append(line)
    return result


def analyze_code_in(dir: str):
    return analyze(code_in(dir))


def fn_dot(dicts, dotfile):
    fndefs, vardefs = dicts
    with open(dotfile,'w') as dot:
        print('digraph defs {', file=dot)
        for fn_name in fndefs.keys():
            print('%s [shape=box]' % fn_name, file=dot )
        show_defs(fndefs, dot)
        show_defs(vardefs, dot)
        print('}', file=dot)


def show_defs(fndefs, dot):
    for name in fndefs.keys():
        for ref in fndefs[name]:
            print('%s -> %s;' % (ref, name), file=dot)


fn_dot(analyze_code_in(notebook_dir), '../../data/calls.dot')


# TODO: Use sets to avoid multiple links