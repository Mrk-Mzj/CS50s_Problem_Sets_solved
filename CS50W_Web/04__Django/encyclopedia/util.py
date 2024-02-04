import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render
import markdown2


def list_entries():
    """
    Returns a sorted list of all names of encyclopedia entries without their extensions.
    Lambda function assures that list is not separated to uppercase sorted first and lowercase sorted later - but mix them together.
    """
    _, filenames = default_storage.listdir("entries")
    return list(
        sorted(
            (
                re.sub(r"\.md$", "", filename)
                for filename in filenames
                if filename.endswith(".md")
            ),
            key=lambda v: v.upper(),
        )
    )


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content.encode("utf-8")))


def get_entry(title):
    """
    Retrieves an encyclopedia entry from file by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def render_entry(request, title):
    """
    Renders entry page for the browser.
    """
    return render(
        request,
        "encyclopedia/entry.html",
        {
            "title": title,
            "content": markdown2.markdown(get_entry(title)),
        },
    )
