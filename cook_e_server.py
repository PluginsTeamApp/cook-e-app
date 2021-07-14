# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

'''
1. post function - json args - parse site'''

@app.route('/getRecipes', methods=['POST'])
def add_message():
    content = request.get_json()
    print("Content ", content)
    return jsonify({"uuid": 'uuid'})

def main():
    app.run(debug=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
