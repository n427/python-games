adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
day1 = input("Time of day: ")
verb1 = input("Present tense verb: ")
adj3 = input("Cute Adjective: ")
pet = input("Typical household pet: ")
verb2 = input("Past tense verb: ")
noun1 = input("Plural, part of an animal: ")
noun2 = input("Plural, part of an animal: ")
animal = input("Big animal: ")
verb3 = input("Past tense verb: ")

madlib = f"It was a {adj1} and {adj2} {day1}. You were {verb1} down the street when \
suddenly you heard a noise. You turned around, anticipating the worst. Turns out, \
it was just a {adj3} {pet}. As you {verb2} closer, you realized that this was \
no ordinary {pet}. It had {noun1} and {noun2} the size of a {animal}. \
You backed away slowly in fear, then {verb3} away as fast as you could. \
The end."

print(madlib)