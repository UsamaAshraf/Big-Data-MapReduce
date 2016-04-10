import re
import csv
import collections
import StringIO


with open('forum_node.tsv', 'r') as _file:
     content = _file.read()

reader = csv.reader(StringIO.StringIO(content), delimiter='\t')

#words = re.split('; |, |. |: |! |? |" |< |> |( |) |[ |] |# |$ |= |- |/', content)

_dict = collections.defaultdict(list)

for _line in reader:
    words = re.split('\W+', _line[4])
    for word in words:
        _dict[word.lower()].append(_line[0])	    

print _dict['fantastically']

