def generate(f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14):
    print("It was a %s, cold November day. I woke up to the %s smell of %s roasting in the %s downstairs. I %s down the stairs to see if I could help %s the dinner. My mom said, \"See if %s needs a fresh %s.\" So I carried a tray of glasses full of %s into the %s room. When I got there, I couldn't believe my %s! There were %s %s on the %s!" % (f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14))

print("MadLib Generator")

adj1 = input("Gimme an adjective: ")
adj2 = input("Gimme another adjective: ")
bird = input("Gimme a type of bird: ")
room = input("Gimme a room in a house: ")
verb1 = input("Gimme a verb (past tense): ")
verb2 = input("Gimme a verb: ")
name = input("Gimme a relative's name: ")
noun1 = input("Gimme a noun: ")
liquid = input("Gimme a liquid: ")
verb3 = input("Gimme a verb ending in -ing: ")
body = input("Gimme a part of the body (plural): ")
noun2 = input("Gimme a plural noun: ")
verb4 = input("Gimme a verb ending in -ing: ")
noun3 = input("Gimme a noun: ")

generate(adj1, adj2, bird, room, verb1, verb2, name, noun1, liquid, verb3, body, noun2, verb4, noun3)
