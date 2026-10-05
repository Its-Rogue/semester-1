# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

music = {
    "C418": "Beta",
    "Radiohead": "In Rainbows"
}

# Pretty-print the data structure

pprint(music)

# Display details of one album recorded by a specific artist

pprint(music.get("Radiohead"))
