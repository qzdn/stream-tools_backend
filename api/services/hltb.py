import urllib.parse
from howlongtobeatpy import HowLongToBeat


def get_hltb_data(gamename):
    gamename = urllib.parse.unquote_plus(gamename)

    # Если год указан (doom**1993)
    if "**" in gamename:
        game, year = gamename.split("**")
        return _get_game_info_by_year(game, int(year))

    # Без года
    return _get_game_info(gamename)


def _get_game_info(gamename):
    search_list = HowLongToBeat().search(gamename, similarity_case_sensitive=False)
    if not search_list:
        return {"message": f"Игра {gamename} не найдена"}

    match = max(search_list, key=lambda element: element.similarity)
    return _format_game_info(match)


def _get_game_info_by_year(game, year):
    search_list = HowLongToBeat().search(game, similarity_case_sensitive=False)
    if not search_list:
        return {"message": f"Игра {game} {year} не найдена"}

    for data in search_list:
        if data.release_world == year:
            return _format_game_info(data)

    return {"message": f"Игра {game} {year} не найдена"}


def _format_game_info(data):
    return {
        "game_name": data.game_name,
        "release_world": data.release_world,
        "main_story": data.main_story,
        "main_extra": data.main_extra,
        "completionist": data.completionist,
        "url": f"https://howlongtobeat.com/game/{data.game_id}",
    }
