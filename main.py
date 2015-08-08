import numpy as np
from constants import ARCHETYPES_CACHE_FILE
from constants import character_index_lookup
from constants import character_name_lookup
from helpers import singer_vector_from_resume


archetypes = np.load(ARCHETYPES_CACHE_FILE)


# Each column represents a character
def fach_me(known_character_ids):
    input_singer_vector = singer_vector_from_resume(known_character_ids)

    singer_fach = input_singer_vector.dot(archetypes.transpose()).dot(archetypes)

    return [character_index_lookup[index] for index, score in enumerate(singer_fach) if score > 0]


suggested_character_ids = fach_me([123])

for id in suggested_character_ids:
    print character_name_lookup[id]
