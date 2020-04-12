from flask import render_template
from flask.views import MethodView

from models.ascii_tables import BlogTable


class PermalinkHandler(MethodView):
    def get(self, id):
        blog = BlogTable.query.filter_by(id=id).first()
        if not blog:
            return "No such blog exists", 404
        return render_template("blog_permalink.html", blog=blog)
