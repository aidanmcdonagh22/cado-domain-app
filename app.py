from flask import Flask, request, render_template
from whois import whois
import json

app = Flask(__name__)

# filter for pretty printing
def to_pretty_json(value):
    return json.dumps(
        value, sort_keys=True, indent=2, separators=(',', ': '), default=str
    )

app.jinja_env.filters['to_pretty_json'] = to_pretty_json

@app.route("/", methods=["GET", "POST"])
def index():
    domain: str = request.args.get("domain")
    
    if domain and not isinstance(domain, str):
        return { "error", "domain must be a str" }, 400
    
    whoisData = whois(domain) if domain else None
    
    return render_template('index.html', data=whoisData)