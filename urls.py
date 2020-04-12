# add routes to handlers
from handlers.rot13 import Rot13Handler
from handlers.userSignup import SignupHandler, ProfileHandler
from handlers.blog import BlogHandler
from handlers.asciiArt import AsciiArtHandeler
from handlers.showcase import Showcase_handler
from handlers.blog_form import BlogFormHandler
from handlers.permalink import PermalinkHandler
from handlers.blog_mainpage import BlogMainHandler
from wsgi import app

app.add_url_rule('/rot13', view_func=Rot13Handler.as_view('rot13'))
app.add_url_rule('/signup', view_func=SignupHandler.as_view('signup'))
app.add_url_rule('/profile', view_func=ProfileHandler.as_view('profile'))
app.add_url_rule('/blog', view_func=BlogHandler.as_view('blog'))
app.add_url_rule('/asciiArt', view_func=AsciiArtHandeler.as_view('asciiArt'))
app.add_url_rule('/showcase', view_func=Showcase_handler.as_view('showcase'))
app.add_url_rule('/blog/newpost', view_func=BlogFormHandler.as_view('newpost'))
app.add_url_rule('/blog/<id>', view_func=PermalinkHandler.as_view("permalink"))
app.add_url_rule('/blog/mainpage', view_func=BlogMainHandler.as_view("mainpage"))

