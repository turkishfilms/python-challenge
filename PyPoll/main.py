import csv



def main():
    total_votes = 0
    candidates = []
    unique_candidates = []
    winner = ""
    csv_path = r"G:\CODE\Data Analytics Bootcamp\Data_Analytics\Class_Folder\M3_Python\chllenge\python-challenge\PyPoll\Resources\election_data.csv"
    with open(csv_path) as e_CSV:
        election_CSV = csv.reader(e_CSV, delimiter=',')
        cur_candidate = ""
        # bID,COunty,Cand
        for row in election_CSV:
            if(row[0] == "Ballot ID"):
                continue
            total_votes += 1
            if(cur_candidate == row[2]):
                candidates[-1]["votes"] += 1
            else:
                candidates.append({"name": row[2], "votes":1})
                cur_candidate = row[2]    
        # i mistakenly thought this data was ordered by candidate, it is not. the next step gets unique candidates 
        unique_candidates = [candidates[0]]
        candidates.pop(0)
        for candidate in candidates:
            for unique_candidate in unique_candidates:
                if(candidate["name"] == unique_candidate["name"]):
                    unique_candidate["votes"] += candidate["votes"]
                    continue
                else:
                    match = 0
                    for unique_candidate_2 in unique_candidates:
                        if(unique_candidate_2["name"] == candidate["name"]):
                            match = 1
                    if(match == 0):
                        unique_candidates.append(candidate)
                        continue
        # lord forgive  me for my sins
        # calcPercents
        max_percent = 0
        for unique_candidate in unique_candidates:
            unique_candidate["percent"] = unique_candidate["votes"] / total_votes * 100
            if(unique_candidate["percent"] > max_percent): 
                max_percent = unique_candidate["percent"] 
                    # winner
                winner = unique_candidate["name"]
        
        
        
    
        
    analysis_path =r"G:\CODE\Data Analytics Bootcamp\Data_Analytics\Class_Folder\M3_Python\chllenge\python-challenge\PyPoll\analysis\finalAnalysis.txt"
    with open(analysis_path, "w") as new_text:
        candidates_str = ""
        for unique_candidate in unique_candidates:
            candidates_str += f'{unique_candidate["name"]}: {round(unique_candidate["percent"],2)}% {unique_candidate["votes"]} \n \t' 
        election_analysis = f"""
  Election Results
  -------------------------
  Total Votes: {total_votes}
  -------------------------
  Candidates:
  {candidates_str}
  -------------------------
  Winner: {winner}
  -------------------------
  """
        print(election_analysis)
        new_text.write(election_analysis)

main() 