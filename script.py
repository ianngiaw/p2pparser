# -*- coding: utf-8 -*-
import xbmc,urllib

all_modules = ['https://github.com/ianngiaw/p2pparser/raw/master/livesports247/livesports247.tar.gz', 'https://github.com/ianngiaw/p2pparser/raw/master/livesportscf/livesportscf.tar.gz']

for parser in all_modules:
    xbmc.executebuiltin('XBMC.RunPlugin("plugin://plugin.video.p2p-streams/?mode=405&name=p2p&url=' + urllib.quote(parser) + '")')
    xbmc.sleep(1000)

xbmc.executebuiltin("Notification(%s,%s,%i,%s)" % ('P2P-Streams', "All parsers imported",1,''))
