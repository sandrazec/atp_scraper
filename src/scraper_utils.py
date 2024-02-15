# src/scraper_utils.py

def construct_url(rank_range, date_week):
    base_url = "https://www.atptour.com/en/rankings/singles?RankRange={rank_range}&Region=all&DateWeek={date_week}"
    return base_url.format(rank_range=rank_range, date_week=date_week)

def parse_player_data(soup):
    # Implement parsing logic here
    # Return a list of dictionaries, each representing a player's data
    pass

