import urllib.parse
from howlongtobeatpy import HowLongToBeat


def search_with_gamename(results_list, format):
    match = max(results_list, key=lambda element: element.similarity)
    if format == "txt":
        return f"{match.game_name} ({match.release_world}) :: Main story - {match.main_story} ч., Main+Extras - {match.main_extra} ч., Completionist - {match.completionist} ч. :: https://howlongtobeat.com/game/{match.game_id}"
    elif format == "json":
        return {
            "game": {
                "game_name": match.game_name,
                "release_world": match.release_world,
                "main_story": match.main_story,
                "main_extra": match.main_extra,
                "completionist": match.completionist,
                "url": f"https://howlongtobeat.com/game/{match.game_id}",
            }
        }


def search_with_specified_year(game_name, year, format, results_list):
    for result in results_list:
        if result.release_world == year:
            if format == "txt":
                return f"{result.game_name} ({result.release_world}) :: Main story - {result.main_story} ч., Main+Extras - {result.main_extra} ч., Completionist - {result.completionist} ч. :: https://howlongtobeat.com/game/{result.game_id}"
            elif format == "json":
                return {
                    "game": {
                        "game_name": result.game_name,
                        "release_world": result.release_world,
                        "main_story": result.main_story,
                        "main_extra": result.main_extra,
                        "completionist": result.completionist,
                        "url": f"https://howlongtobeat.com/game/{result.game_id}",
                    }
                }
    else:
        if format == "txt":
            return f"Игра {game_name} {year} не найдена"
        elif format == "json":
            return {"message": f"Игра {game_name} {year} не найдена"}


def request_to_hltb(game_name, year, format):
    # vercel workaround
    game_name = urllib.parse.unquote_plus(game_name)

    results_list = HowLongToBeat().search(game_name, similarity_case_sensitive=False)
    if results_list is None or len(results_list) == 0:
        if format == "txt":
            return f"Игра {game_name} не найдена"
        elif format == "json":
            return {"message": f"Игра {game_name} не найдена"}

    if year:
        return search_with_specified_year(game_name, year, format, results_list)

    return search_with_gamename(results_list, format)
