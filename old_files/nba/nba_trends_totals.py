def fileHandling(someFile):
    with open(someFile) as f:
        lines = f.read().splitlines()
        return lines


def updateDictionaryOvers(streak):
    dictionaryOvers['O' + streak] += 1


def updateDictionaryUnders(streak):
    dictionaryUnders['U' + streak] += 1


def getStreaksOvers(data):
    for strings in data:
        streak = 0
        for char in strings:
            if char == 'O':
                streak += 1
            else:
                if streak > 0:
                    updateDictionaryOvers(str(streak))
                    streak = 0


def getStreaksUnders(data):
    for i in range(1, len(data), 2):
        streak = 0
        for char in data[i]:
            if char == 'U':
                streak += 1
            else:
                if streak > 0:
                    updateDictionaryUnders(str(streak))
                    streak = 0


def startOvers():
    file = 'nba_totals.txt'
    file = fileHandling(file)
    getStreaksOvers(file)


def startUnders():
    file = 'nba_totals.txt'
    file = fileHandling(file)
    getStreaksUnders(file)


dictionaryOvers = dict.fromkeys(
    ['O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10', 'O11'])
dictionaryOvers = dict.fromkeys(dictionaryOvers, 0)

dictionaryUnders = dict.fromkeys(
    ['U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8', 'U9', 'U10', 'U11'])
dictionaryUnders = dict.fromkeys(dictionaryUnders, 0)


startOvers()
startUnders()

print(dictionaryOvers)
print(dictionaryUnders)
