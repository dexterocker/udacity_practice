from flask import render_template
from flask.views import MethodView

from models.ascii_tables import BlogTable


class BlogMainHandler(MethodView):

    def get(self):
        blogs = BlogTable.query.order_by(BlogTable.date_created.desc()).all()
        return render_template("blog_mainpage.html", blogs=blogs)