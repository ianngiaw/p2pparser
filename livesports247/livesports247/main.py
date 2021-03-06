# -*- coding: utf-8 -*-

""" 
This plugin is 3rd party and not part of p2p-streams addon

livesports247

"""
import sys,os,requests
current_dir = os.path.dirname(os.path.realpath(__file__))
basename = os.path.basename(current_dir)
core_dir =  current_dir.replace(basename,'').replace('parsers','')
sys.path.append(core_dir)
from peertopeerutils.webutils import *
from peertopeerutils.pluginxbmc import *
from peertopeerutils.directoryhandle import *

base_url = 'http://pilkalive.weebly.com'
invalid_links = ['/en.html', '/sports.html', '/others.html', '/es.html', '/pl.html', '/pt.html', '/ru--ua.html', '/fr.html', '/se--dk--no.html', '/rs--hr.html', '/it.html', '/nl.html', '/cz.html', '/other.html']

def module_tree(name,url,iconimage,mode,parser,parserfunction):
    if not parserfunction: livesport_main()
    elif parserfunction == "livesports_links": livesports_links(url)
    elif parserfunction == "ttvnet_acestream": ttvnet_acestream(url)

def livesport_main():
    try:
        source = clean(get_page_source(base_url))
    except:
        source = ""
    if source:
        match = list(filter(lambda x: '.html' in x, re.compile('<a href="(.+?)"').findall(source)))
        for link in match:
            name = link[1:][0:-5]
            if link in invalid_links:
                addDir("[B][COLOR red]"+name+"[/COLOR][/B]", "",401,os.path.join(current_dir,"icon.png"),1,False)
                continue
            addDir(name,base_url+link,401,os.path.join(current_dir,"icon.png"),1,True,parser="LiveSports247",parserfunction="livesports_links")
    return

def livesports_links(url):
    try:
        source = clean(get_page_source(url))
    except:
        source = ""
    if source:
        match = re.compile('<iframe scrolling="no" frameborder="0" src="(.+?)"').findall(source)
        if not match:
            addDir("[B][COLOR red]iframe not found[/COLOR][/B]", "",401,os.path.join(current_dir,"icon.png"),1,False)
        else:
            for iframelink in match:
                ttvnet_acestream(iframelink)


def ttvnet_acestream(url):
    try:
        source = get_page_source(url)
    except:
        source = ""
    if source:
        player = re.compile('this.loadPlayer\("(.+?)"').findall(source)
        if not player:
            addDir("[B][COLOR red]loadplayer not found[/COLOR][/B]", "",401,os.path.join(current_dir,"icon.png"),1,False)
        else:
            for acehash in player:
                ace_id = "acestream://" + acehash
                addDir(ace_id, ace_id,1,"http://www.masterlin.ru/wp-content/uploads/2014/02/Ace-Stream-Logo.jpeg",1,False)
