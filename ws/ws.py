
#! -*- coding: utf-8 -*-

##    Authors:       Marc Serret i Garcia (marcserret@live.com)
##
##    Copyright 2018 Marc Serret i Garcia

import os
import sys
import shutil
import tempfile
import json
import re
import cherrypy
import datetime as time
from pathlib import Path
# from cherrypy.lib.static import serve_file
import mysql.connector
import database


class AppIndex(object):
    @cherrypy.expose
    def index(self):
        return open('./templates/index.html')

@cherrypy.expose
class GetAllGames(object):
    def GET(self, name = "", planet = ""):
        result = database.getAllGames()
        return str(result).replace("datetime.date(", "").replace(")", "").replace("Decimal(", "")


if __name__ == '__main__':
    conf = {
         '/getGames': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')]
        },
        '/': {
            'tools.sessions.on': False,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public',
        },
        'global' : {
            'server.socket_host' : '0.0.0.0',
            'server.socket_port' : 8081,
            'server.thread_pool' : 8,
        }
    }

    webapp = AppIndex()
    webapp.getGames = GetAllGames()
    cherrypy.quickstart(webapp, '/', conf)