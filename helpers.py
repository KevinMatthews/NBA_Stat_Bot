# Script contains helper methods for the web crawler
import bs4

# Takes the player's name as a string of the form: "First Last"
# Returns the basketball-reference URL of the player's stats page
def getPlayerUrl(name):

    # Get first and last names 
    names = name.split()
    first = names[0].lower()
    last = names[1].lower()

    # Select first 2 letters of first name
    first = first[:2]

    # Select first 5 letters of last name
    if len(last) > 5:
        last = last[:5]

    # Get first letter of last name
    letter = last[:1].lower()

    # Return URL string from player's name
    return "https://www.basketball-reference.com/players/" + letter + "/" + last + first + "01.html"

# Takes the webpage of player's stats as a string
# Returns their stats in an array, with each array element
#   containing one year of their stats, and the last element
#   contains their overall career stats
def getPlayerStatsArray(html):

    # Create BeautifulSoup object
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # Create array of all table rows containing per game stats
    years = soup.findAll('tr', id=lambda x: x and x.startswith('per_game.'))

    # Array to store all the stats 
    yearsArray = []

    # For each table row element (a year of stats each), parse it into an array of tuples of stat name and stat number
    for tr in years:

        # Create BeautifulSoup object out of this table row
        soup = bs4.BeautifulSoup(str(tr), 'html.parser')

        # Array to store each stat for this year
        statsArray = []

        # Get the table header element 
        header = soup.findAll('th')[0]

        obj = {}

        obj['type'] = header['data-stat']

        obj['value'] = header.string

        # Add the year to the stats array
        statsArray.append(obj)

        # Get all table data elements (stats) for this year
        stats = soup.findAll('td')

        # For each of the stats, parse it into a tuple and add it to array
        for stat in stats:

            obj = {}

            obj['type'] = stat['data-stat']

            obj['value'] = stat.string

            statsArray.append(obj)

        # Add this year of stats to the final array
        yearsArray.append(statsArray)

    return yearsArray

# Takes a player stats array and turns it into a reddit-formatted table
def getRedditString(playerStats):
    
    numStats = len(playerStats[0])

    printString = "Season | Age | Tm | Lg | Pos | G | GS | MP | FG | FGA | FG% | 3P | 3PA | 3P% | 2P | 2PA | 2P% | eFG% | FT | FTA | FT% | ORB | DRB | TRB | AST | STL | BLK | TOV | PF | PTS\n"

    headersArray = []

    for i in range(numStats):
        headersArray.append(":--------:")

    headerString = " | ".join(headersArray)

    printString = printString + headerString + "\n"

    for year in playerStats:

        stats = []

        for obj in year:

            stats.append(obj['value'])

        yearString = " | ".join(map(str, stats))

        printString = printString + yearString + "\n"

    return printString

