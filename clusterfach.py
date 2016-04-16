import numpy as np
import scipy.sparse
from sparsesvd import sparsesvd

CACHE= 'cache.npz'
ARCHETYPES = 'archetypes'
CHARACTERS = 'characters'


def fach_me(singer_resume, cache_file=CACHE):
    """ Given a list of ids, return dictionary ids with similarity scores """

    with np.load(cache_file) as data:
        archetypes = data[ARCHETYPES]
        character_positions = data[CHARACTERS].item()

    input_singer_vector = np.zeros((len(character_positions), 1))
    for character_id in singer_resume:
        position = character_positions[character_id]
        input_singer_vector[position] = True

    input_singer_vector = input_singer_vector.transpose()

    singer_fach = input_singer_vector.dot(archetypes.transpose()).dot(archetypes)

    suggested_roles = []
    for character, index in character_positions.iteritems():
        suggested_roles.append({'id': character, 'score': singer_fach[0, index]})

    return sorted(suggested_roles, key=lambda k: k['score'], reverse=True)


def generate_archetypes(singer_resumes, archetype_count_k=20, cache_file=CACHE):
    """ Generate and write to disk an archetype matrix given a population """

    # Generate a unique, ordered, list of characters
    characters = set()  # Could optimized by using single comprehension
    for singer_resume in singer_resumes:
        characters.update(singer_resume)
    characters = list(characters)

    # Create a dict to lookup character index by id
    character_positions = dict()
    for i, character in enumerate(characters):
        character_positions[character] = i

    # Construct an empty matrix to populate
    dimensions = len(singer_resumes), len(characters)
    singer_matrix = scipy.sparse.lil_matrix(dimensions)

    # Populate the matrix
    for j, singer_resume in enumerate(singer_resumes):
        for character in singer_resume:
            position = character_positions[character]
            singer_matrix[j, position] = True

    # Convert matrix to a sparse matrix
    sparse_singer_matrix = scipy.sparse.csc_matrix(singer_matrix)

    # Do magic with maths
    U, s, V = sparsesvd(sparse_singer_matrix, archetype_count_k)

    archetypes = V

    # Cache the data for later use
    arrays = {CHARACTERS: character_positions, ARCHETYPES: archetypes}
    np.savez(cache_file, **arrays)
