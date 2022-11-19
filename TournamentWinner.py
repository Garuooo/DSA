# time complexity = O(N) , space complexity = O(K)
# Where N is the number of competitions and k is number of teams
def tournamentWinner(competitions, results):
    scores={}
    match_number=0
    tour_winner=""
    winner_score=0
    for match in competitions:
        result=results[match_number]
        if result ==1:
            winner=match[0]
        else:
            winner=match[1]
        if scores.get(winner)==None:
            scores[winner]=3
        else:
            scores[winner]=scores[winner]+3
        match_number+=1

    for team in scores:
        if scores[team] > winner_score:
            tour_winner=team
            winner_score=scores[team] 
    return tour_winner
print(tournamentWinner([
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
],[0, 0, 1]))