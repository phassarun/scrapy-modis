from datetime import datetime

from arachne import Arachne
from twisted.internet import reactor
from twisted.web import http
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource

app = Arachne(__name__)

resource = WSGIResource(reactor, reactor.getThreadPool(), app)

# log files in the `logs` directory
site = Site(resource,
            logFormatter=http.combinedLogFormatter,
            logPath="logs/"+datetime.now().strftime("%Y-%m-%d.web.log"))
reactor.listenTCP(8080, site)

if __name__ == '__main__':
    reactor.run()
