class Election:
    def __init__(self, candidates):
        # Initialize the dictionary with candidates' names as keys and their votes as values (initially 0)
        self.votes = {candidate: 0 for candidate in candidates}

    def vote(self, name):
        # If the candidate exists, increment their vote count and return True
        if name in self.votes:
            self.votes[name] += 1
            return True
        # If the candidate does not exist, return False
        else:
            return False

    def print_winner(self):
        # Find the maximum number of votes received
        max_votes = max(self.votes.values())
        # Get the list of candidates who received the maximum number of votes
        winners = [name for name, vote_count in self.votes.items() if vote_count == max_votes]
        # Print each winner's name on a new line
        for winner in winners:
            print(winner)

    def get_votes(self):
        # Return the sorted dictionary based on the number of votes (in descending order)
        return dict(sorted(self.votes.items(), key=lambda item: item[1], reverse=True))


# Example usage:
candidates = ["Alice", "Bob", "Charlie"]
election = Election(candidates)

# Cast some votes
election.vote("Alice")
election.vote("Bob")
election.vote("Alice")
election.vote("Charlie")
election.vote("Charlie")
election.vote("Charlie")
election.vote("Dave")  # This should return False

# Print the votes dictionary
print(election.get_votes())

# Print the winner(s)
election.print_winner()
