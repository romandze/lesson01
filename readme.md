### Popular verbs counter.

Search and count verbs in your project.

#### example usage

```python

import os, collections
from verbscounter import get_top_verbs_in_path

words = []
projects = [
    'django',
    'flask',
    'pyramid',
    'reddit',
    'requests',
    'sqlalchemy',
    '..'
]

for project in projects:
    path = os.path.join('.', project)
    words += get_top_verbs_in_path(path)

top_size = 200
print('total %s words, %s unique' % (len(words), len(set(words))))
for word, occurence in collections.Counter(words).most_common(top_size):
    print(word, occurence)

```

### Licence MIT
