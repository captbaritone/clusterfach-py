import numpy as np

from constants import ARCHETYPES_CACHE_FILE
from constants import singer_resumes
from constants import ARCHETYPE_COUNT_K


def generate_archetypes(list_of_singers_resumes):
    singer_matrix = _singer_matrix_from_resumes(list_of_singers_resumes)

    # Do magic with maths
    U, s, V = np.linalg.svd(singer_matrix)

    archetypes = V[:ARCHETYPE_COUNT_K]

    f = open(ARCHETYPES_CACHE_FILE, 'w')
    np.save(f, archetypes)


def _singer_matrix_from_resumes(list_of_singer_resumes):
    characters = set()
    for singer_resume in list_of_singer_resumes:
        for character in singer_resume:
            characters.add(character)

    ordered_characters = list(characters)

    singer_matrix = []
    for singer_resume in list_of_singer_resumes:
        singer_vector = []
        for character in ordered_characters:
            singer_vector.append(character in singer_resume)
        singer_matrix.append(singer_vector)

    # Rows represent signers, columns represent characters
    return np.array(singer_matrix)

generate_archetypes(singer_resumes)
