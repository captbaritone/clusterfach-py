from clusterfach import fach_me

suggested_character_ids = fach_me(['502'])

for character in suggested_character_ids[:10]:
    print "Character: %s (%s)" % (character['id'], character['score'])
