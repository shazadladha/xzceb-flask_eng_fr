from flask import Flask, render_template, request
from translator import english_to_french, french_to_english
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Index(Resource):
    def get(self):
        return render_template('index.html')


class FrenchToEnglish(Resource):
    def post(self):
        input_text = request.form['text']
        output_text = french_to_english(input_text)
        return output_text


class EnglishToFrench(Resource):
    def post(self):
        input_text = request.form['text']
        output_text = english_to_french(input_text)
        return output_text


api.add_resource(Index, '/')
api.add_resource(FrenchToEnglish, '/french_to_english')
api.add_resource(EnglishToFrench, '/english_to_french')

if __name__ == '__main__':
    app.run(debug=True)

