import csv



def main():
    csvPath = r"G:\CODE\Data Analytics Bootcamp\Data_Analytics\Class_Folder\M3_Python\chllenge\python-challenge\PyPoll\Resources\election_data.csv"
    with open(csvPath) as electionCSV:
        totalVotes = 0
        candidates = []
        winner = ""
        # bID,COunty,Cand
        for bid in electionCSV:
            if(bid[0] == "Ballot ID"):
                continue
            totalVotes += 1
            
            for c in candidates:
                print(c)
                if(bid[2] == c.name):
                    c.votes += bid[1]
                else:
                    print(bid)
                    candidates.push({"name":bid[3], "votes":bid[1]})
                    
            # candidates
            # if knwon cnadidate , update nVPC
            # else add to cand list, update nVPC
        print(candidates)            
        # calcPercents
        # winner
        
    analysisPath =r"G:\CODE\Data Analytics Bootcamp\Data_Analytics\Class_Folder\M3_Python\chllenge\python-challenge\PyPoll\analysis\finalAnalysis.txt"
    with open(analysisPath, "w") as newText:
        electionAnalysis = f"""
  Election Results
  -------------------------
  Total Votes: {totalVotes}
  -------------------------
  candidates[0]: percentages[0]% (numVotesPerCandidates[0])
  
  -------------------------
  Winner: {winner}
  -------------------------
  """
  
    print(electionAnalysis)
    newText.write(electionAnalysis)
    pass


main() 