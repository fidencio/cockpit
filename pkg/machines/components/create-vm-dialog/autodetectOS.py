#!/usr/bin/python

import gi
gi.require_version('Libosinfo', '1.0')
from gi.repository import Libosinfo as osinfo
import sys


loader = osinfo.Loader()
loader.process_default_path()
db = loader.get_db()

url_type_media = sys.argv[1].endswith(".iso")

os = None
if url_type_media:
    media = osinfo.Media().create_from_location(sys.argv[1])
    db.identify_media(media)
    os = media.get_os()
else:
    tree = osinfo.Tree().create_from_location(sys.argv[1])
    os, _ = db.guess_os_from_tree(tree)

if os:
    print(os.get_id())
