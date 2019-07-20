class Simulation:
    def __init__(self):
        self.teams = []
        self.totals = []
        self.file = open('mlb_totals_2017.txt', 'r')
        self.file = self.file.readlines()
        self.parse()
        self.over = dict()
        self.under = dict()

    def parse(self):
        for i in range(60):
            if i % 2:
                self.teams.append(self.file[i])
            else:
                self.totals.append(self.file[i])

    def enterOver(self, c):
        if c in self.over:
            self.over[c] += 1
        else:
            self.over[c] = 1

    def enterUnder(self, c):
        if c in self.under:
            self.under[c] += 1
        else:
            self.under[c] = 1

    def totals_over(self):
        print(dict(sorted(self.over.items())))

    def _over(self):
        return self.over.values()

    def _under(self):
        return self.under.values()

    def totals_under(self):
        print(dict(sorted(self.under.items())))

    def over_format(self):
        count = 0
        first = True
        for t in self.totals:
            for i in t:
                if (i == 'O'):
                    count += 1
                else:
                    if (count > 0):
                        self.enterOver(count)
                        count = 0

    def under_format(self):
        count = 0
        first = True
        for t in self.totals:
            for i in t:
                if (i == 'U'):
                    count += 1
                else:
                    if (count > 0):
                        self.enterUnder(count)
                        count = 0


a = Simulation()
a.over_format()
a.under_format()
a.totals_over()
a.totals_under()

print(a._over())
print(a._under())
