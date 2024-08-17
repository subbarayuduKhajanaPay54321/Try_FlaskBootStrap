from flask import Flask, send_from_directory, render_template, request
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/admin/dashBoard", methods=["GET"])
def dashBoard():
    return render_template("dashBoard.html")


@app.route("/admin/userWalletAndKycUpdate", methods=["GET"])
def userWalletKycUpdate():
    return render_template("manageUsers.html")


@app.route("/assets/<path:filename>")
def serve_assets(filename):
    return send_from_directory("assets", filename)


@app.route("/JQuerySetUp/<path:filename>")
def serve_JQuerySetUp(filename):
    return send_from_directory("JQuerySetUp", filename)


@app.route("/templates/<path:filename>")
def serve_JQuery(filename):
    return send_from_directory("templates", filename)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    # token = request.headers.get("access_token")
    url = "https://khazanapay.net/admin/login"
    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            return response.json()

    except requests.exceptions.RequestException as e:
        return {"errorMsg": "An error occurred during the request"}


@app.route("/getUsers", methods=["POST"])
def getUsers():
    data = request.get_json()
    username = data.get("username")
    token = request.headers.get("Authorization")
    url = "https://khazanapay.net/admin/getUsers"
    headers = {"Authorization": token, "Content-Type": "application/json"}
    payload = {"username": username}
    try:
        response = requests.get(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.json()

    except requests.exceptions.RequestException as e:
        return {"errorMsg": "An error occurred during the request"}


@app.route("/getWalletHistory", methods=["POST"])
def getWalletHistory():
    data = request.get_json()
    username = data.get("username")
    token = request.headers.get("Authorization")
    url = "https://khazanapay.net/admin/getWalletHistory"
    headers = {"Authorization": token, "Content-Type": "application/json"}
    payload = {"username": username}
    try:
        response = requests.get(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.json()

    except requests.exceptions.RequestException as e:
        return {"errorMsg": "An error occurred during the request"}


@app.route("/getWalletHistoryForUser", methods=["POST"])
def getWalletHistoryForUser():
    data = request.get_json()
    username = data.get("username")
    token = request.headers.get("Authorization")
    url = "https://khazanapay.net/admin/getWalletHistoryForUser"
    headers = {"Authorization": token, "Content-Type": "application/json"}
    payload = {"username": username}
    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.json()

    except requests.exceptions.RequestException as e:
        return {"errorMsg": "An error occurred during the request"}


@app.route("/updateKyc", methods=["POST"])
def updateUserStatus():
    data = request.get_json()
    username = data.get("username")
    kycStatus = data.get("KYC_Status")
    token = request.headers.get("Authorization")
    url = "https://khazanapay.net/admin/updateKyc"
    headers = {"Authorization": token, "Content-Type": "application/json"}
    payload = {"username": username, "KYC_Status": kycStatus}
    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.json()

    except requests.exceptions.RequestException as e:
        return {"errorMsg": "An error occurred during the request"}


@app.route("/UpdateWallet", methods=["POST"])
def UpdateWallet():
    data = request.get_json()
    username = data.get("username")
    amount = data.get("amount")
    function = data.get("function")
    token = request.headers.get("Authorization")
    url = "https://khazanapay.net/admin/UpdateWallet"
    headers = {"Authorization": token, "Content-Type": "application/json"}
    payload = {"username": username, "amount": amount, "function": function}
    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.json()

    except requests.exceptions.RequestException as e:
        return {"errorMsg": "An error occurred during the request"}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
