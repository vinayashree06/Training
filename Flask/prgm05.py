# prgm05.py

def register_routes(app):

    @app.route('/admin')
    def hello_admin():
        return 'Hello Admin'

    @app.route('/guest/<guest>')
    def hello_guest(guest):
        return 'Hello %s as Guest' % guest
