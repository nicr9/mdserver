from flask import Flask, Response
from os.path import isfile, basename, splitext
from os.path import join as path_join
from glob import glob

import subprocess

app = Flask(__name__)
app.config.from_object(__name__)

ROOT = "/opt/"

@app.route("/")
def homepage():
    """
    Displays a list of note sets that are available.
    """
    md_wildcard = path_join(ROOT, "notes/", "*.md")
    md_files = glob(md_wildcard)

    notes = [basename(path).split(".md")[0] for path in md_files]
    lines = ["* [{}](/notes/{})\n".format(path, path) \
            for path in notes]
    lines.insert(0, "# Markdown notes\n\n")

    md_path = path_join(ROOT, "list.md")
    html_path = path_join(ROOT, "list.html")

    with open(md_path, 'w') as outp:
        outp.writelines(lines)

    subprocess.call(["pandoc", "-c", "http://localhost:4000/style/github-pandoc.css", "-f", "markdown_github", "-o", html_path, md_path])

    # Return HTML
    with open(html_path, 'r') as html:
        return html.read()

@app.route("/notes/<note_name>")
def note_page(note_name):
    """
    Converts a markdown file to HTML and returns it fully rendered.
    """
    note_path = path_join(ROOT, "notes/", note_name + '.md')
    html_path = path_join(ROOT, "notes/", note_name + '.html')

    if isfile(note_path):
        subprocess.call(["pandoc", "-c", "http://localhost:4000/style/github-pandoc.css", "-f", "markdown_github", "-o", html_path, note_path])

        # Return HTML
        with open(html_path, 'r') as html:
            return html.read()

    return "Whoopsie, can't find that note...", 404

@app.route("/style/<stylesheet>")
def style(stylesheet):
    stylesheet_path = path_join(ROOT, stylesheet)
    if isfile(stylesheet_path):
        # Return CSS
        with open(stylesheet, 'r') as style:
            return Response(style.read(), mimetype="text/css")

    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
