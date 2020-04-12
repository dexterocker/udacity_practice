from flask import render_template, request, redirect
from flask.views import MethodView

from models.ascii_tables import AsciiTable


class AsciiArtHandeler(MethodView):

    def render_ascii_showcase(self):
        arts = AsciiTable.query.order_by(AsciiTable.date_created).all()
        return render_template("ascii_art_showcase.html",arts = arts)

    def get(self):
        return render_template("asciiArt.html")

    # def showcase(self):

    def post(self):
        # avoid cyclic dependency
        from wsgi import db

        title = request.form.get("title")
        art = request.form.get("Art")

        if title and art:
            art = AsciiTable(title=title, art=art)
            db.session.add(art)
            db.session.commit()
            return redirect('/showcase')
        else:
            error = "add both title and art"
            return render_template("asciiArt.html", error=error)
