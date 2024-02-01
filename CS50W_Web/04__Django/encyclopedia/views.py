from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import util
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, title):
    # show entry page requested by user
    if util.get_entry(title):
        return render(
            request,
            "encyclopedia/entry.html",
            {
                "title": title,
                "content": markdown2.markdown(util.get_entry(title)),
            },
        )
    else:
        return render(
            request,
            "encyclopedia/entry.html",
            {"title": "404 - no entry", "content": "404 - no entry found"},
        )


def search(request):
    # show entry page searched by user
    # TODO: consider joining entry (GET) and search (POST)
    searched = request.POST["q"].strip()

    # show entry if searched matches
    if util.get_entry(searched):
        return render(
            request,
            "encyclopedia/entry.html",
            {
                "title": searched,
                "content": markdown2.markdown(util.get_entry(searched)),
            },
        )
    # look for similar entries
    else:
        results = []
        for _ in util.list_entries():
            if searched.lower() in _.lower():
                results.append(_)

        # results = util.list_entries().filter(searched)
        return render(request, "encyclopedia/search.html", {"results": results})
