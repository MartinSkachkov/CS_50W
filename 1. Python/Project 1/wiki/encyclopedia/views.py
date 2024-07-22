from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import Markdown
from . import util
import random

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

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        if util.get_entry(title.lower()) is not None: #this page already exists
           return render(request, "encyclopedia/error.html", {"err_msg": "This entry already exists!"})
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {"title": title, "content": html_content})
        
def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        md_content = util.get_entry(title)

        return render(request, "encyclopedia/edit.html", {"title": title, "content": md_content})
    else:
        return render(request, "encyclopedia/error.html", {"err_msg": "Error during the edit page process!"})
    
def save_edit(request):
    if request.method == "POST":
        title = request.POST['new_title']
        content = request.POST['new_content']

        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {"title": title, "content": html_content})
    
def random_page(request):
    random_title = random.choice(util.list_entries())
    random_html_content = convert_md_to_html(random_title)
    return render(request, "encyclopedia/entry.html", {"title": random_title, "content": random_html_content})