class Simulation:
    def __init__(self):
        self.teams = []
        self.games = []
        self.file = open('nba_results.txt', 'r')
        self.file = self.file.readlines()
        self.parse()
        self.win = dict()
        self.lost = dict()
        self.sendWin = 0
        self.sendLost = 0

    def parse(self):
        for i in range(60):
            if i % 2:
                self.teams.append(self.file[i])

            else:
                self.games.append(self.file[i])

    def enterWin(self, c):
        if c in self.win:
            self.win[c] += 1
        else:
            self.win[c] = 1

    def enterLost(self, c):
        if c in self.lost:
            self.lost[c] += 1
        else:
            self.lost[c] = 1

    def totals_win_dict(self):
        print(dict(sorted(self.win.items())))

    def percentage_distribution_win(self):
        counter = 0
        for keys in self.win.keys():
            counter += 1
            if counter > 9:
                break
            value = int(self.win[keys])
            formula = float((100*value)/self.total_games_win())
            formula = round(formula, 2)
            print(str(counter) + " -> " + str(formula) + "%")

    def percentage_distribution_lost(self):
        counter = 0
        for keys in self.lost.keys():
            counter += 1
            if counter > 9:
                break

            value = int(self.lost[keys])
            formula = float((100*value)/self.total_games_lost())
            formula = round(formula, 2)
            print(str(counter) + " -> " + str(formula) + "%")

    def totals_win(self):
        return self.win

    def _win(self):
        return self.win.values()

    def _lost(self):
        return self.lost.values()

    def totals_lost_dict(self):
        print(dict(sorted(self.lost.items())))

    def _win_dict(self):
        for key in self.win.items():
            print(key, end='')

    def totals_lost(self):
        return self.lost

    def win_format(self):
        count = 0
        first = True
        for t in self.games:
            for i in t:
                self.sendWin += 1
                if (i == 'W'):
                    count += 1
                else:
                    if (count > 0):
                        self.enterWin(count)
                        count = 0

    def lose_format(self):
        count = 0
        send = 0
        first = True
        for t in self.games:
            for i in t:
                self.sendLost += 1
                if (i == 'L'):
                    count += 1
                else:
                    if (count > 0):
                        self.enterLost(count)
                        count = 0

    def total_games_lost(self):
        return(self.sendLost/4)

    def total_games_win(self):
        return(self.sendWin/4)


a = Simulation()
a.win_format()
a.lose_format()
print("\nWinners-Spread Trends for NBA :")
a.totals_win_dict()
c = a.percentage_distribution_win()

# a._win_dict()

print("\nLosers-Spread Trends for NBA :")

a.totals_lost_dict()

b = a.totals_win()

c = a.percentage_distribution_lost()

print(c)


print("\nHow many games in 2017 regular season:?\n")
a.total_games_win()


a.totals_win()


# print(a._win())
# print(a._lost())
