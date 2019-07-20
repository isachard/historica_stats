class Records:
    def __init__(self):
        self.teams = []
        self.records = []
        self.file = open('mlb_results_2017.txt', 'r')
        self.file = self.file.readlines()
        self.parse()
        self.wins = dict()


    def parse(self):
        for i in range(61):
            if i % 2 :
                self.teams.append(self.file[i])
            else:
                self.records.append(self.file[i])
    
    def howManyWins(self):
        count = 0
        for r in self.records:
            for i in r:
                if (i == 'W'):
                    count += 1
                else:
                    if (count > 0 ):
                        self.enterWin(count)
                        count = 0 
    
    def enterWin(self, c):
        if c in self.wins:
            self.wins[c] += 1
        else:
            self.wins[c] = 1

    def printWins(self):
        print(dict(sorted(self.wins.items())))


a = Records()
a.howManyWins()
a.printWins()
