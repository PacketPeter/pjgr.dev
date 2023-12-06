import flask
import os
import discord
import dotenv

app = flask.Flask(__name__)
dotenv.load_dotenv()
webhook_url = os.getenv("WEBHOOK_URL")

@app.route("/", methods=["GET"])
def index():
    return flask.render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
    return flask.render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if flask.request.method == "GET":
        return flask.render_template("contact.html")

    if flask.request.method == "POST":
        try:
            name = flask.request.form["user_name"]
            email = flask.request.form["user_email"]
            message = flask.request.form["message"]

            webhook = discord.SyncWebhook.from_url(webhook_url)

            embed = discord.Embed(
                title="New Message",
                description=f"**Name:** ` {name} `\n**Email:** ` {email} `\n**Message:** ` {message} `",
                color=discord.Color.og_blurple()
            )
            webhook.send(embed=embed)

            return flask.render_template("contact.html", success=True)
        except:
            return flask.render_template("contact.html", error=True)