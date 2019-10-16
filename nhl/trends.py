

def test_handler():
    file = open("nhl_totals.txt")
    data = file.readlines()
    file.close()
    return data


def team_counter(team, season):
    print(team)
    over = 0
    under = 0
    push = 0
    for i in season:
        if i == 'O':
            over +=1
        if i == 'U':
            under += 1
        if i == 'P':
            push +=1

    return [team,over,under,push]

def main():
    data = test_handler()

    for i in range(0,31,2):
        print(team_counter(data[i],data[i+1]))


main()
