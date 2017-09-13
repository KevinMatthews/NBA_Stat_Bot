import re

class CommentParser:

    # Constructor which takes the filename of the players list and initializes it into an array
    def __init__(self, filename):

        # Read player list into an array and store as uppercase 
        with open(filename) as f:
            self.players = f.readlines()
        self.players = [x.strip() for x in self.players]
        self.players = [x.lower() for x in self.players]

    # Returns the name of the mentioned NBA player, if one exists
    # in the comment, and returns None otherwise
    def getPlayerName(self, comment):

        # There was a matching pattern of "first last's stats", so see if name exists in database
        if re.search("\[[a-zA-Z_.'-]+\s[a-zA-Z_.'-]+\sstats\]", comment, re.IGNORECASE):

            # Get the matching pattern
            match = re.search("\[[a-zA-Z_.'-]+\s[a-zA-Z_.'-]+\sstats\]", comment, re.IGNORECASE).group(0)

            # Parse the name from the matching pattern
            name = match[1:-7].lower()

            # Check to see if name exists in players list
            if name in self.players:
                return name
            else:
                return None

        # No matching pattern of "first last's stats", so return None
        else:
            return None

