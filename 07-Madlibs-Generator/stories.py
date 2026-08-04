import random

stories = [

    """
{name} visited {place} carrying a {adjective} backpack.
Suddenly, a giant {animal} appeared!
Instead of running away, {name} started dancing.
The {animal} joined in, and everyone cheered.
It became the most unforgettable day in {place}.
""",

    """
One morning, {name} woke up and found a {adjective} {animal}
waiting outside the house.
Together they traveled to {place},
where they discovered a hidden treasure.
""",

    """
During a trip to {place},
{name} accidentally challenged a {animal}
to a dance competition.
The crowd couldn't stop laughing because everything looked so {adjective}!
"""
]

def get_story():
    return random.choice(stories)