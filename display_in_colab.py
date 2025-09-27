from IPython.core.display import display, HTML
html_code = open("index.html", "r").read()
css_code = "<style>" + open("style.css", "r").read() + "</style>"
js_code = "<script>" + open("script.js", "r").read() + "</script>"
display(HTML(css_code + html_code + js_code))
