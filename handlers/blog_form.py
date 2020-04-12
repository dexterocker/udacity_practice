from flask import render_template, request, redirect
from flask.views import MethodView

from models.ascii_tables import BlogTable


class BlogFormHandler(MethodView):

    def get(self):
        return render_template("blog_form.html")

    def post(self):

        from wsgi import db
        subject = request.form.get("Subject")
        blog = request.form.get("Blog")

        if subject and blog:
            blog_obj = BlogTable(subject=subject,blog=blog)
            db.session.add(blog_obj)
            db.session.commit()
            return redirect('/blog/' + str(blog_obj.id))
        else:
            return render_template("blog_form.html",errors = "add both the feild plz")
            # return redirect()