from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey123"

# Fake users and transactions
users = {"admin": "password123"}
transactions = []

# Random fake winners
fake_names = ["John", "Sarah", "Mike", "Anna", "David", "Emily", "Tom", "Sophia"]

def generate_fake_transaction():
    name = random.choice(fake_names)
    amount = random.choice([100, 200, 500])
    return f"{name} sent ${amount} and received ${amount*2}"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html", error=None)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    # Add random fake transaction for realism
    if random.random() < 0.5:
        transactions.append(generate_fake_transaction())
    return render_template("dashboard.html", transactions=transactions)

@app.route("/payment", methods=["GET", "POST"])
def payment():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        recipient = request.form.get("recipient")
        amount = request.form.get("amount")
        transactions.append(f"{session['user']} sent ${amount} to {recipient} (FAKE)")
        return redirect(url_for("dashboard"))
    return render_template("payment.html")

@app.route("/winners")
def winners():
    # Show last 10 fake winners
    recent_winners = transactions[-10:]
    return render_template("winners.html", winners=recent_winners)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
