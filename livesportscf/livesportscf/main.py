# -*- coding: utf-8 -*-

""" 
This plugin is 3rd party and not part of p2p-streams addon

livesportscf

"""
import sys,os,requests
current_dir = os.path.dirname(os.path.realpath(__file__))
basename = os.path.basename(current_dir)
core_dir =  current_dir.replace(basename,'').replace('parsers','')
sys.path.append(core_dir)
from peertopeerutils.webutils import *
from peertopeerutils.pluginxbmc import *
from peertopeerutils.directoryhandle import *

base_url = 'http://live-sports.cf/'

def module_tree(name,url,iconimage,mode,parser,parserfunction):
    if not parserfunction: live_sports_main()
    elif parserfunction == "live_sports_links": live_sports_links(url)
    elif parserfunction == "ttvnet_acestream": ttvnet_acestream(url)

def live_sports_main():
    try:
        source = clean(get_page_source(base_url))
    except:
        source = ""
    if source:
        start = source.find('<p><b>TORRENT STREAM</b></p>')
        end = source.find('<p><b>IFRAME</b></p>')
        source = source[start:end]
        stream_links = re.compile('<a title="(.+?)" href="(.+?)" target="_blank">').findall(source)
        for stream_name, stream_url in stream_links:
            addDir(stream_name,stream_url,401,os.path.join(current_dir,"icon.png"),1,True,parser="livesportscf",parserfunction="live_sports_links")
    return

def live_sports_links(url):
    try:
        source = clean(get_page_source(url))
    except:
        source = ""
    if source:
        match = re.compile("<iframe width='630' height='400' src='(.+?)'").findall(source)
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
