# ClusterFach

_cluster_, noun: A group of similar things or people positioned or occurring
closely together.

_fach_, noun: German. Compartment or category.

ClusterFach uses maths ([Singular value
decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition)) to
provide an easy to use suggestion engine.

Use cases might include movie recommendations for a user based on movies they
like, or suggesting roles to opera singers based on role's they've previously
sung.

Adapted from <https://github.com/katiahayati/clusterfach>, originally for
<http://fachme.com>. Thanks to Katia for finding this algorithm, and putting
the pieces together.

## Installation

1. Clone this repo
2. `pip install -r requirements.txt`

## Usage

    # find_movies.py
    import clusterfach

    # A list of people. Each represented by a list of ids of movies they like.
    people = [
        [283, 120, 2792, 83],
        [294, 1942, 2831, 29832, 23],
        [3274, 29, 93, 291, 293],
        # ...
    ]

    # Crunch the data, this bit might take some time
    clusterfach.generate_archetypes(people, cache_file='cache.npz')

    # Movies I like
    me = [232, 3943, 394] 

    movie_suggestions = cluterfach.fach_me(me, cache_file='cache.npz')

    # Movies I might like
    print movie_suggestions
    # => [249, 2848, 2084, 283, 292]

## TODO

1. Find a good relatable example data-set
2. Create example app
3. Add tests
4. Upload to pypi
5. Setup Travis.ci


