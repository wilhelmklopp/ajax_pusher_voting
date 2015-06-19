from django.shortcuts import render
import json
from django.http import HttpResponse  # For JSON output
from voting.models import Voting
from pusher import Pusher
import os  # for environment variables


def index(request):
    row = Voting.objects.get(pk=1)
    score = row.score
    context = {"score": score}
    return render(request, "voting/index.html", context)


def receive_votes(request):
    pusher = Pusher(
        app_id=os.environ.get('PUSHER_APP', ''),
        key="ca2bcf928a3d000ae5e4",
        secret=os.environ.get('PUSHER_SECRET', '')
        )
    json_response = {"success": False}
    row = Voting.objects.get(pk=1)
    try:
        if request.method == "GET":
            data = request.GET
            if data["vote"] == "up":
                row.score = row.score + 1
                row.total_votes = row.total_votes + 1
                row.save()
                pusher.trigger(
                    "voting_channel",
                    "new_vote",
                    {"score": row.score}
                    )
                # success
                json_response = {"success": True}
                return HttpResponse(
                    json.dumps(json_response),
                    content_type="application/json"
                    )
            elif data["vote"] == "down":
                row.score = row.score - 1
                row.total_votes = row.total_votes + 1
                row.save()
                pusher.trigger(
                    "voting_channel",
                    "new_vote",
                    {"score": row.score}
                    )
                # success
                json_response = {"success": True}
                return HttpResponse(
                    json.dumps(json_response),
                    content_type="application/json"
                    )
            else:
                return HttpResponse(
                    json.dumps(json_response),
                    content_type="application/json"
                    )

        else:
            return HttpResponse(
                json.dumps(json_response),
                content_type="application/json"
                )
    except Exception as e:
        json_response = {"success": False, "error": str(e)}
        return HttpResponse(
            json.dumps(json_response),
            content_type="application/json"
            )


def new_counter(request):
    row_add = Voting(total_votes=0, score=0)
    row_add.save()
    return render(request, "voting/done.html")
