import codecs

from flask.views import MethodView
from flask import render_template, request


class BlogHandler(MethodView):
    def get(self):
        return render_template("blog.html")

    # def post(self):
    #     text1 = request.form.get("text")
    #     print(text1)
    #     rot13 = ""
    #     if text1:
    #         rot13 = codecs.encode(text1, 'rot_13')
    #     return render_template("rot13.html", text=rot13)
    #     # return text1
