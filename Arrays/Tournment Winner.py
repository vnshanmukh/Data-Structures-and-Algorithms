def tournamentWinner(competitions, results):
	currentbestteam = ""
	scores = {currentbestteam : 0}
	for i, competition in enumerate(competitions):
		result = results[i]
		hometeam, awayteam = competition
		if result == 1:
			winingteam = hometeam
		else:
			winingteam = awayteam
		updatescore(winingteam, 3 ,scores)
		if scores[winingteam] > scores[currentbestteam]:
			currentbestteam = winingteam
	return currentbestteam
def updatescore(team,points,scores):
	if team not in scores:
		scores[team] = 0
	scores[team] += points