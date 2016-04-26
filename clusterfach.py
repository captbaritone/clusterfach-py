import numpy as np
import scipy.sparse
from sparsesvd import sparsesvd

CACHE = 'cache.npz'
ARCHETYPES = 'archetypes'
ITEMS = 'items'


def recomendations_for(user_items, cache_file=CACHE):
    """
    Given a list of ids, return a list of dicts containing ids and similarity
    scores
    """

    with np.load(cache_file) as data:
        archetypes = data[ARCHETYPES]
        item_positions = data[ITEMS].item()

    user_vector = np.zeros((len(item_positions), 1))
    for item in user_items:
        position = item_positions[item]
        user_vector[position] = True

    user_vector = user_vector.transpose()

    rec_vector = user_vector.dot(archetypes.transpose()).dot(archetypes)

    recomendations = []
    for item, index in item_positions.iteritems():
        recomendations.append({'item': item, 'score': rec_vector[0, index]})

    return sorted(recomendations, key=lambda k: k['score'], reverse=True)


def generate_archetypes(users, archetype_count_k=20, cache_file=CACHE):
    """ Generate and write to disk an archetype matrix given a population """

    # Generate a unique, ordered, list of items
    items = set()  # Could optimized by using single comprehension
    for user_items in users:
        items.update(user_items)
    items = list(items)

    # Create a dict to lookup item indexes by id
    item_positions = dict()
    for i, item in enumerate(items):
        item_positions[item] = i

    # Construct an empty matrix to populate
    dimensions = len(users), len(items)
    user_matrix = scipy.sparse.lil_matrix(dimensions)

    # Populate the matrix
    for j, user_items in enumerate(users):
        for item in user_items:
            position = item_positions[item]
            user_matrix[j, position] = True

    # Convert matrix to a sparse matrix
    sparse_user_matrix = scipy.sparse.csc_matrix(user_matrix)

    # Do magic with maths
    U, s, V = sparsesvd(sparse_user_matrix, archetype_count_k)

    archetypes = V

    # Cache the data for later use
    arrays = {ITEMS: item_positions, ARCHETYPES: archetypes}
    np.savez(cache_file, **arrays)
