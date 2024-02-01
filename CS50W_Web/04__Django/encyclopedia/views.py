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
