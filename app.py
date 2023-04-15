from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    input_string = request.form['input_string']
    morse_code_string = ''
    for char in input_string:
        if char.upper() in morse_code:
            morse_code_string += morse_code[char.upper()] + ' '
        elif char == ' ':
            morse_code_string += '  '
    return jsonify({'morse_code': morse_code_string})


if __name__ == '__main__':
    app.run(debug=True)
