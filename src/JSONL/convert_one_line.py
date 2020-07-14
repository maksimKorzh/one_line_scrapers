# get rid of indentations in JSONL files
import json; [open('Sold_Houses_no_indent_2020-07-14-14-23.jsonl', 'a').write(json.dumps((json.loads('{' + item + '}'))) + '\n') for item in open('Sold_Houses_2020-07-14-14-23.jsonl').read()[1:-2].split('}\n{')]
