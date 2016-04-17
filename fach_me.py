import sys
import re
from clusterfach import fach_me

character_names = {}

p = re.compile("(\d+): (.*)")
for line in open("characters.txt", "rb"):
    matches = p.search(line)
    character_names[matches.group(1)] = matches.group(2)

me = sys.argv[1:] or ['731', '1862', '153', '562']

print "----- Given that you sing -----"
print '\n'.join(character_names[id] for id in me)

print "----- You should also sing -----"

suggested_character_ids = fach_me(me)

for character in suggested_character_ids[:20]:
    id = character['id']
    name = character_names[id]
    print "%s: %s (%s)" % (id, name, character['score'])
