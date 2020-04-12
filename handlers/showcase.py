from flask import render_template
from flask.views import MethodView

from models.ascii_tables import AsciiTable


class Showcase_handler(MethodView):

    def get(self):
        arts = AsciiTable.query.order_by(AsciiTable.date_created.desc()).all()
        return render_template("ascii_art_showcase.html", arts=arts)