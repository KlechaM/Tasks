import re


def damage(spell):
    if len(re.findall("fe", spell)) == 0 or len(re.findall("fe", spell)) > 1:
        return 0
    regex = re.compile("fe(.*)ai")
    match = re.findall(regex, spell)[0]
    subspells_values = {"dai": 5, "jee": 3, "je": 2, "fe": 1, "aine": 4, "ain": 3, "ai": 2, "ne": 2}
    subspells = ["dai", "jee", "je", "fe", "aine", "ain", "ai", "ne"]
    dmg = 3
    for subspell in subspells:
        value = subspells_values[subspell]
        found_subspells = re.findall(subspell, match)
        regex = re.compile(subspell)
        match = regex.sub("", match)
        dmg += len(found_subspells) * value
    dmg = dmg - len(match)
    if dmg < 0:
        return 0
    return dmg
