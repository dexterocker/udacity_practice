import re
from flask.views import MethodView
from flask import render_template, request, redirect


class ProfileHandler(MethodView):
    def get(self):
        return request.args.get('username')


class SignupHandler(MethodView):
    def get(self):
        return render_template("userSignup.html")

    @staticmethod
    def valid_username(username):
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return username and USER_RE.match(username)

    @staticmethod
    def valid_password(password):
        USER_RE = re.compile(r"^.{3,20}$")
        return password and USER_RE.match(password)

    @staticmethod
    def valid_email(email):
        USER_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        return not email or USER_RE.match(email)

    def post(self):
        have_error = False
        username = request.form.get("username")
        password = request.form.get("password")
        verify_pass = request.form.get("verifyPassword")
        email = request.form.get("email")

        params = {
            "username": username,
            "email": email,
        }
        if not SignupHandler.valid_username(username):
            params['username_error'] = "not a valid username"
            have_error = True
        if not SignupHandler.valid_password(password):
            params['password_error'] = "not a valid password"
            have_error = True
        elif password != verify_pass:
            params['verify_error'] = "password does not match"
            have_error = True
        if not SignupHandler.valid_email(email):
            params['email_error'] = "email not correct"
            have_error = True
        if have_error:
            return render_template('userSignup.html', **params)
        return redirect('/profile?username={}'.format(username))
