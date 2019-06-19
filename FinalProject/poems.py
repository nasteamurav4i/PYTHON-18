import glob


def load_poems(poems_glob="poems/*.txt"):
    poem_files = glob.glob(poems_glob)
    poem_strings = []

    for f in poem_files:
        poem_strings += [l for l in open(f).readlines() if len(l.split(" ")) > 1]

    return poem_strings


def find_rhyme(string):
    string = "".join(c for c in string if c.isalpha())
    input_words = string.split()

    may_be_rhyme = []
    for l in load_poems():
        l = "".join([c for c in l if c.isalpha() or c == " "])
        line_words = l.split(" ")

        if line_words[-1] == input_words[-1]:
            continue

        if line_words[-1][-3:] == input_words[-1][-3:]:
            may_be_rhyme.append(line_words)

    if len(may_be_rhyme) == 0:
        return "Рифма не найдена =("

    may_be_rhyme.sort(key=lambda lw: abs(len(lw) - len(input_words)))
    return " ".join(may_be_rhyme[0])
