def main():
    # Sample election data (modify as per actual data)
    constituencies = [
        {
            'name': 'Constituency A',
            'parties': [
                {'party': 'BJP', 'candidate': 'Rahul Sharma', 'votes': 45000},
                {'party': 'INC', 'candidate': 'Priya Singh', 'votes': 42000},
                {'party': 'AAP', 'candidate': 'Arjun Patel', 'votes': 38000}
            ]
        },
        {
            'name': 'Constituency B',
            'parties': [
                {'party': 'BJP', 'candidate': 'Neha Gupta', 'votes': 55000},
                {'party': 'INC', 'candidate': 'Vikram Joshi', 'votes': 53000},
                {'party': 'TMC', 'candidate': 'Sneha Roy', 'votes': 49000}
            ]
        },
        {
            'name': 'Constituency C',
            'parties': [
                {'party': 'INC', 'candidate': 'Amit Kumar', 'votes': 32000},
                {'party': 'BJP', 'candidate': 'Suresh Reddy', 'votes': 31500},
                {'party': 'JD(U)', 'candidate': 'Rajesh Das', 'votes': 29000}
            ]
        }
    ]

    # 1. Calculate total votes per party
    party_totals = {}
    for constituency in constituencies:
        for party_data in constituency['parties']:
            party = party_data['party']
            votes = party_data['votes']
            party_totals[party] = party_totals.get(party, 0) + votes

    # 2. Find constituency winners
    constituency_winners = []
    for constituency in constituencies:
        max_votes = 0
        winner = {}
        for party_data in constituency['parties']:
            if party_data['votes'] > max_votes:
                max_votes = party_data['votes']
                winner = {
                    'constituency': constituency['name'],
                    'party': party_data['party'],
                    'candidate': party_data['candidate'],
                    'votes': party_data['votes']
                }
        constituency_winners.append(winner)

    # 3. Determine overall election winner
    overall_winner = max(party_totals.items(), key=lambda x: x[1])

    # 4. Calculate vote share percentages and close contests
    close_margin_constituencies = []
    for constituency in constituencies:
        total_votes = sum(party['votes'] for party in constituency['parties'])
        sorted_parties = sorted(constituency['parties'], key=lambda x: x['votes'], reverse=True)
        
        # Calculate percentages
        for party in constituency['parties']:
            party['vote_share'] = (party['votes'] / total_votes) * 100
        
        # Check for close contests
        if len(sorted_parties) > 1:
            margin = sorted_parties[0]['vote_share'] - sorted_parties[1]['vote_share']
            if margin < 12:
                close_margin_constituencies.append({
                    'constituency': constituency['name'],
                    'winner': sorted_parties[0]['party'],
                    'runner_up': sorted_parties[1]['party'],
                    'margin': round(margin, 2)
                })

    # Display results
    print("==== Election Results Analysis ====\n")
    
    print("-- Total Votes per Party --")
    for party, votes in party_totals.items():
        print(f"{party}: {votes} votes")
    
    print("\n-- Constituency Winners --")
    for winner in constituency_winners:
        print(f"{winner['constituency']}: {winner['candidate']} ({winner['party']}) - {winner['votes']} votes")
    
    print("\n-- Overall Election Winner --")
    print(f"{overall_winner[0]} with {overall_winner[1]} total votes")
    
    print("\n-- Close Contests (Margin < 12%) --")
    if close_margin_constituencies:
        for contest in close_margin_constituencies:
            print(f"{contest['constituency']}: {contest['winner']} vs {contest['runner_up']} (Margin: {contest['margin']}%)")
    else:
        print("No constituencies with close margins")

if __name__ == "__main__":
    main()