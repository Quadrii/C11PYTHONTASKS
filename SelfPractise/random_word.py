import random
noun = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
random_word = random.choice(noun)
random_word1 = random.choice(noun)
random_word2 = random.choice(noun)
verb = ["kicks", "jingles", "bounces", "slurps", "mweos", "explodes", "curdles"]
random_verb = random.choice(verb)
random_verb1 = random.choice(verb)
random_verb2 = random.choice(verb)
adjectives = ["furry", "balding", "incredulous", "fragrant", "exubernet", "glistening"]
random_adjective = random.choice(adjectives)
random_adjective1 = random.choice(adjectives)
random_adjective2 = random.choice(adjectives)
preposition = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
random_preposition = random.choice(preposition)
random_preposition1 = random.choice(preposition)
adverb = ["curiously", "extravagant", "tantalizing", "furiously", "sensuosly"]
random_adverb = random.choice(adverb)
print(f'{random_adjective} {random_word} \n {random_adjective} {random_word} {random_verb} {random_preposition} the {random_adjective1} {random_word1} {random_adverb} , the {random_word} {random_verb1} the {random_word1} {random_verb2} {random_preposition1} a {random_adjective2} {random_word2}')