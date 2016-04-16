from collections import defaultdict

from clusterfach import generate_archetypes


def get_singer_resumes():
    singer_resumes_dict = defaultdict(set)

    with open("singer_pairs.txt", "r") as pairs:
        for line in pairs.readlines():
            singer, character = tuple(line[0:-1].split(", "))
            singer_resumes_dict[singer].add(character)

    # Convert dict of sets to list of lists
    return [list(resume) for singer_id, resume in singer_resumes_dict.iteritems()]

generate_archetypes(get_singer_resumes(), 20)
