# from gevent import monkey
# monkey.patch_time()
# monkey.patch_thread()

# Not needed for now but might be put in in the future
# monkey.patch_subprocess()

# from gevent.server import _tcp_listener
# from gevent.pywsgi import WSGIServer

from app import app


if __name__ == '__main__':
    app.run()

# try:
#     listener = _tcp_listener(('127.0.0.1', 3500))
#     WSGIServer(
#         listener,
#         app,
#         # log=app.logger,
#         # keyfile=kesala_paths.NGINX_SSL_KEY_LOCATION,
#         # certfile=kesala_paths.NGINX_SSL_CRT_LOCATION
#     ).serve_forever()
# except (KeyboardInterrupt, SystemExit):
#     raise
# except Exception as e:
#     print(f'Failed: {e}')
# finally:
#     print(f'Stopped')