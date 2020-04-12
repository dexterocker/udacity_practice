from datetime import datetime

from sqlalchemy.dialects.mysql import LONGTEXT

from wsgi import db


class AsciiTable(db.Model):
    __tablename__ = 'ascii_table'

    title = db.Column(db.String(512), primary_key=True)
    art = db.Column(LONGTEXT)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


class BlogTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(512))
    blog = db.Column(LONGTEXT)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
