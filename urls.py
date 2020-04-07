# add routes to handlers
from handlers.rot13 import Rot13Handler
from handlers.userSignup import SignupHandler, ProfileHandler
from handlers.blog import BlogHandler
from main import app

app.add_url_rule('/rot13', view_func=Rot13Handler.as_view('rot13'))
app.add_url_rule('/signup', view_func=SignupHandler.as_view('signup'))
app.add_url_rule('/profile', view_func=ProfileHandler.as_view('profile'))
app.add_url_rule('/blog', view_func=BlogHandler.as_view('blog'))
