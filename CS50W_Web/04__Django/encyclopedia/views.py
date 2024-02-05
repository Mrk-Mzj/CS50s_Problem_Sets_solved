from random import randrange

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import util


class EditEntry(forms.Form):
    # object transporing content data
    # from and to form in new_edit.html
    content = forms.CharField(widget=forms.Textarea())


class NewEntry(forms.Form):
    # object transporing content and title data
    # from and to form in new_edit.html
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea())


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def edit(request):

    # save eddited entry (POST)
    if request.method == "POST":
        filled = EditEntry(request.POST)

        # if form is ok
        if filled.is_valid():
            # user sent correctly filled form - saving entry file
            # title = filled.cleaned_data["title"]
            title = request.POST["title"]
            content = filled.cleaned_data["content"]
            util.save_entry(title, content)
            # send user to the entry page
            return util.render_entry(request, title)
        else:
            # user sent incorrect filled form - showing him form again
            return render(
                request,
                "encyclopedia/edit.html",
                {
                    "form": filled,
                    "error": "Error: incorrect data",
                },
            )

    # edit entry (GET)
    title = request.GET["title"]
    return render(
        request,
        "encyclopedia/edit.html",
        {"title": title, "form": EditEntry(initial={"content": util.get_entry(title)})},
    )


def entry(request, title):
    # show entry page
    if util.get_entry(title):
        return util.render_entry(request, title)

    # or show 404
    else:
        return render(
            request,
            "encyclopedia/entry.html",
            {"title": "404 - no entry", "content": "404 - no entry found"},
        )


def new(request):

    # save new entry (POST)
    if request.method == "POST":
        filled = NewEntry(request.POST)

        # if form is ok and not trying to overwrite an existing entry
        if (
            filled.is_valid()
            and filled.cleaned_data["title"] not in util.list_entries()
        ):
            # user sent correctly filled form - saving entry file
            title = filled.cleaned_data["title"]
            content = filled.cleaned_data["content"]
            util.save_entry(title, content)
        else:
            # user sent incorrect filled form - showing him form again
            return render(
                request,
                "encyclopedia/new.html",
                {
                    "form": filled,
                    "error": "Error: incorrect data or entry already exists",
                },
            )

    # write a new entry (GET)
    return render(
        request,
        "encyclopedia/new.html",
        {"title": "Create new entry", "form": NewEntry()},
    )


def random(request):
    # show random entry
    no = randrange(0, len(util.list_entries()))
    title = util.list_entries()[no]
    return util.render_entry(request, title)


def search(request):
    # show entry page searched by user
    searched = request.POST["q"].strip()

    # show entry if searched matches
    if util.get_entry(searched):
        return util.render_entry(request, searched)

    # look for similar entries
    else:
        results = []
        for _ in util.list_entries():
            if searched.lower() in _.lower():
                results.append(_)

        return render(request, "encyclopedia/search.html", {"results": results})
