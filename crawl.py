from urllib.request import urlopen
import helpers

class StatCrawler:

    # Retrieves the stats of specified player
    def getStats(self, player):
        
        # Get URL from player's name
        player_url = helpers.getPlayerUrl(player)

        # Download webpage
        page = urlopen(player_url)

        # Read into html
        html = page.read()

        # Scrape page into an array and return it
        self.playerStats = helpers.getPlayerStatsArray(html)

    # Returns a reddit-formatted string of the player's stats
    def prettify(self):

        if not self.playerStats:
            return

        return helpers.getRedditString(self.playerStats)

