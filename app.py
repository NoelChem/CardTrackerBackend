from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

cards_file = 'cards.json'


def read_cards():
    with open(cards_file, 'r') as file:
        return json.load(file)


def write_cards(cards):
    with open(cards_file, 'w') as file:
        json.dump(cards, file, indent=4)


@app.route('/cards', methods=['GET'])
def get_cards():
    cards = read_cards()
    return jsonify(cards)


@app.route('/cards', methods=['POST'])
def add_card():
    data = request.json
    cards = read_cards()
    new_card = {
        "id": len(cards) + 1,
        "name": data["name"],
        "card_type": data["card_type"],
        "rarity": data["rarity"],
        "version": data["version"],
        "is_foil": data["is_foil"],
        "is_full_art": data["is_full_art"]
    }
    cards.append(new_card)
    write_cards(cards)
    return jsonify(new_card), 201


if __name__ == '__main__':
    app.run(debug=True)
