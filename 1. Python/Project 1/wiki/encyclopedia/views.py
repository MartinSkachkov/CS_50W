from django.shortcuts import render
from markdown2 import Markdown
from . import util

def convert_md_to_html(title):
    content = util.get_entry(title) # loads the content of the page by the given title
    if content == None:
        return None
    else:
        markdowner = Markdown()
        return markdowner.convert(content) # converts the content to html

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        '''
        In Django, when you use the render function to render a template, 
        you only need to specify the path relative to the TEMPLATES directory
        that you have configured in your settings. Django automatically knows
        where to look for the templates based on your settings.
        '''
        return render(request, "encyclopedia/error.html", {"err_msg": "This entry does not exist!"})
    else:
        return render(request, "encyclopedia/entry.html", {"title": title, "content": html_content})
    
def recommendation(entry_search):
    available = util.list_entries()
    recommended = []
    
    for entry in available:
        if entry_search.lower() in entry.lower():
            recommended.append(entry)
    return recommended

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {"title": entry_search, "content": html_content})
        else:
            recommended = recommendation(entry_search)
            return render(request, "encyclopedia/recommended.html", {"recommended": recommended})
