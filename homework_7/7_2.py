from os.path import split


def correct_sentence(text):
    new_sentence = text.split(" ")
    new_sentence[0] = new_sentence[0].capitalize()
    new_sentence = " ".join(new_sentence)
    if new_sentence[-1] !=".":
        return new_sentence+"."
    else:
        return new_sentence

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
