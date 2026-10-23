
from flask import Flask, render_template, request
import socket

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    ip = None
    domain = ""
    error = None

    if request.method == "POST":  #if user has submitted the form
        domain = request.form.get("domain", "").strip() #.strip() is used to remove extra spaces from the starting and ending of our input

        if not domain:  #if user has not entered any domain name
            error = "Please enter a domain name."
        else:
            try:
                results = socket.getaddrinfo(
                    domain, None, socket.AF_INET  #none=>user has not selected specific service or port
                ) #socket.AF_INET=>asks for IPv4 address info(for IPv6=>INET6)

                ips = sorted(set(
                    item[4][0] for item in results #item[4]=>part of a tuple containing add info
                    # example : item[4] = ('142.251.150.119', 443)
                    #item[4][0] only IP & item[4][1] only port number(443)
                ))

                if ips:
                    ip = ips[0]
                else:
                    error = "No IPv4 address found."

            except socket.gaierror:
                error = "Domain not found or DNS unavailable."

    return render_template(
        "index.html", ip=ip, domain=domain, error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
#app.run=>flask dev starts web server
#debug=true=>reload if code is changed
