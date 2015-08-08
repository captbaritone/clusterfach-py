import numpy as np
from constants import character_index_lookup


def singer_vector_from_resume(resume):
    characters = []
    for index, id in character_index_lookup.iteritems():
        singer_has_sung_character = (id in resume)
        characters.append(singer_has_sung_character)
    return np.array(characters)
