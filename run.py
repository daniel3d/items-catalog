from app import init_app, config

app = init_app()

if __name__ == '__main__':
   app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)