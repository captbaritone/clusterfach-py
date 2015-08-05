from numpy.linalg import svd
from numpy import array

CLUSTERS = 2

character_index_lookup = {
    0: "Papageno",
    1: "Figaro",
    2: "Mimi",
    3: "Rudolfo",
    4: "Susanna"
}


def v_clustered():
    # Get list of singer resumes
    singer_matrix = array([
        (1, 1, 0, 0, 0),
        (1, 1, 0, 0, 0),
        (0, 0, 1, 0, 1),
        (0, 0, 0, 1, 0),
    ])

    U, s, V = svd(singer_matrix)

    return V[:CLUSTERS]

# Cache
clusters = v_clustered()

input_singer_vector = array([1, 0, 0, 0, 0])
singer_fach = input_singer_vector.dot(clusters.transpose()).dot(clusters)

for index, score in enumerate(singer_fach):
    if score > 0:
        print character_index_lookup[index]
