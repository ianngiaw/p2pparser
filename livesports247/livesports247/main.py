# -*- coding: utf-8 -*-

""" 
This plugin is 3rd party and not part of p2p-streams addon

livesport247

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

def module_tree(name,url,iconimage,mode,parser,parserfunction):
    if not parserfunction: livesport_main()

def livesport_main():
    try:
        source = clean(get_page_source(base_url))
    except:
        source = ""
    if source:
        match = list(filter(lambda x: '.html' in x, re.compile('<a href="(.+?)"').findall(source)))
        for link in match:
            new_source = clean(get_page_source(base_url + link))
            new_match = re.compile('<iframe scrolling="no" frameborder="0" src="(.+?)"').findall(new_source)
            name = link[1:][0:-5]
            for iframelink in new_match:
                true_source = get_page_source(iframelink)
                player = re.compile('this.loadPlayer\("(.+?)"').findall(true_source)
                for acehash in player:
                    addDir(name, "acestream://"+acehash,1,"http://www.masterlin.ru/wp-content/uploads/2014/02/Ace-Stream-Logo.jpeg",1,False)
    return
