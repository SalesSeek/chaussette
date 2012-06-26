from meinheld import server
from meinheld import patch
patch.patch_all()


class Server(object):
    def __init__(self, listener, application=None, backlog=2048):
        server.set_backlog(backlog)
        host, port = listener
        if host.startswith('fd://'):
            fd = int(host.split('://')[1])
            server.set_listen_socket(fd)
        else:
            server.listen(listener)

        self.application = application

    def serve_forever(self):
        server.run(self.application)
