#!/usr/bin/python

import gi
gi.require_version('Libosinfo', '1.0')
from gi.repository import Libosinfo as osinfo
import sys


loader = osinfo.Loader()
loader.process_default_path()
db = loader.get_db()

oses = db.get_os_list()

for i in range(oses.get_length()):
    os = oses.get_nth(i)

    osID = os.get_id()
    osShortID = os.get_short_id()
    osName = os.get_name()
    osVersion = os.get_version()
    if not osVersion:
        osVersion = ""
    osFamily = os.get_family()
    osVendor = os.get_vendor()
    osReleaseDate = os.get_release_date_string()
    if not osReleaseDate:
        osReleaseDate = ""
    osEOLDate = os.get_eol_date_string()
    if not osEOLDate:
        osEOLDate = ""
    osCodename = os.get_codename()
    if not osCodename:
        osCodename = ""

    print("%s | %s | %s | %s | %s | %s | %s | %s | %s" %
          (osID, osShortID, osName, osVersion, osFamily, osVendor, osReleaseDate,
           osEOLDate, osCodename))
