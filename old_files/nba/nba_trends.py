def fileHandling(someFile):
    with open(someFile) as f:
        lines = f.read().splitlines()
        return lines


def updateDictionaryWinners(streak):
    dictionaryWinners['W' + streak] += 1


def updateDictionaryLosers(streak):
    dictionaryLosers['L' + streak] += 1


def getStreaksWinners(data):
    for strings in data:
        streak = 0
        for char in strings:
            if char == 'W':
                streak += 1
            else:
                if streak > 0:
                    updateDictionaryWinners(str(streak))
                    streak = 0


def getStreaksLosers(data):
    for strings in data:
        streak = 0
        for char in strings:
            if char == 'L':
                streak += 1
            else:
                if streak > 0:
                    updateDictionaryLosers(str(streak))
                    streak = 0


def startLosers():
    file = 'nba_moneyline.txt'
    file = fileHandling(file)
    getStreaksLosers(file)


def startWinners():
    file = 'nba_moneyline.txt'
    file = fileHandling(file)
    getStreaksWinners(file)


dictionaryWinners = dict.fromkeys(
    ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10', 'W11'])
dictionaryWinners = dict.fromkeys(dictionaryWinners, 0)

dictionaryLosers = dict.fromkeys(
    ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11'])
dictionaryLosers = dict.fromkeys(dictionaryLosers, 0)


startWinners()
startLosers()

for i in sorted(dictionaryWinners.keys()):
    print(i)

print(dictionaryWinners.values())
print(dictionaryLosers.values())


print(dict(sorted(dictionaryWinners.items())))
