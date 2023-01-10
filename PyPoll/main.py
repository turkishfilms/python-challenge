import csv



def main():
    totalVotes = 0
    candidates = []
    uniqueCand = []
    winner = ""
    csvPath = r"G:\CODE\Data Analytics Bootcamp\Data_Analytics\Class_Folder\M3_Python\chllenge\python-challenge\PyPoll\Resources\election_data.csv"
    with open(csvPath) as eCSV:
        electionCSV = csv.reader(eCSV, delimiter=',')
        curCandidate = ""
        # bID,COunty,Cand
        for row in electionCSV:
            if(row[0] == "Ballot ID"):
                continue
            totalVotes += 1
            if(curCandidate == row[2]):
                candidates[-1]["votes"] += 1
            else:
                candidates.append({"name": row[2], "votes":1})
                curCandidate = row[2]    
        # i mistakenly thought this data was ordered by candidate, it is not. the next step gets unique candidates 
        uniqueCand = [candidates[0]]
        candidates.pop(0)
        for cand in candidates:
            for uC in uniqueCand:
                if(cand["name"] == uC["name"]):
                    uC["votes"] += cand["votes"]
                    continue
                else:
                    matchh = 0
                    for uC2 in uniqueCand:
                        if(uC2["name"] == cand["name"]):
                            matchh = 1
                    if(matchh == 0):
                        uniqueCand.append(cand)
                        continue
        # lord forgive  me for my sins
        # calcPercents
        maxPercent = 0
        for u in uniqueCand:
            u["percent"] = u["votes"] / totalVotes * 100
            if(u["percent"] > maxPercent): 
                maxPercent = u["percent"] 
                    # winner
                winner = u["name"]
        
        
        
    
        
    analysisPath =r"G:\CODE\Data Analytics Bootcamp\Data_Analytics\Class_Folder\M3_Python\chllenge\python-challenge\PyPoll\analysis\finalAnalysis.txt"
    with open(analysisPath, "w") as newText:
        candstr = ""
        for u in uniqueCand:
            candstr += f'{u["name"]}: {round(u["percent"],2)}% {u["votes"]} \n \t' 
        electionAnalysis = f"""
  Election Results
  -------------------------
  Total Votes: {totalVotes}
  -------------------------
  Candidates:
  {candstr}
  -------------------------
  Winner: {winner}
  -------------------------
  """
        print(electionAnalysis)
        newText.write(electionAnalysis)

main() 