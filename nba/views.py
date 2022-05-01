import json
from django.http import HttpResponse, JsonResponse
from nba_api.stats.static.players import get_players
from nba_api.stats.endpoints import playercareerstats

# Create your views here.


def index(request):
    return HttpResponse("Elite NBA Api")


def players(request):
    all_players = get_players()
    return JsonResponse({"players": all_players}, status=200)


def get_player(request, id):
    stats = playercareerstats.PlayerCareerStats(
        player_id=id).get_data_frames()[0]
    result = json.dumps(json.loads(stats.to_json(orient="records")), indent=4)
    print(result)
    return HttpResponse(result, content_type="application/json")
