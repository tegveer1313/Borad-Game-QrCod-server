from flask import Flask, render_template, abort
import pandas as pd

app = Flask(__name__)

# Excel file
excel_file = "TestQuetions.xlsx"

# Read Excel
df = pd.read_excel(excel_file)

# Remove spaces from column names
df.columns = df.columns.str.strip()

# Create card answer dictionary
cards = {}

for _, row in df.iterrows():

    card_id = str(row["ID"]).strip().upper()
    answer = str(row["Correct Answer"]).strip().upper()

    cards[card_id] = answer


@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Card Answer System</title>
    </head>

    <body style="font-family: Arial; text-align: center; padding: 50px;">

        <h1>Card Answer System</h1>

        <p>Scan a QR code to check an answer.</p>

        <p>Server is running successfully.</p>

    </body>
    </html>
    """


@app.route("/card/<card_id>")
def card_answer(card_id):

    card_id = card_id.strip().upper()

    # Check whether card exists
    if card_id not in cards:
        abort(404)

    answer = cards[card_id]

    return render_template(
        "answer.html",
        card_id=card_id,
        answer=answer
    )


if __name__ == "__main__":

    print("====================================")
    print(" CARD ANSWER SYSTEM")
    print("====================================")
    print(f"Cards loaded: {len(cards)}")
    print("Server starting...")
    print("")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )