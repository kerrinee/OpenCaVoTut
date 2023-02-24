import flask
from flask import request, jsonify

import cv2
import face_recognition

from PIL import Image

app = flask.Flask(__name__)
app.config["DEBUG"] == True

# img1 = Image.open(r'C:\Users\Kerrine\Documents\codysp23\iden\Choidentify.jpg')
# img2 = Image.open(r'C:\Users\Kerrine\Documents\codysp23\pictures\Cho.jpg')

# img1cv = cv2.imread(img1)
# img2cv = cv2.imread(img2)

img1cv = face_recognition.load_image_file(r'C:\Users\Kerrine\Documents\codysp23\iden\Choidentify.jpg')
img2cv = face_recognition.load_image_file(r'C:\Users\Kerrine\Documents\codysp23\pictures\Cho.jpg')

img1cv = face_recognition.face_encodings(img1cv)[0]
img2cv = face_recognition.face_encodings(img2cv)[0]
@app.route('/', methods=['GET'])
def home():
    return "<h1>API</h1>"

@app.route('/imagefile', methods=['GET'])
def image():
    # file = request.files['image']
    
    # img2 = Image.open(file.stream)
    result = face_recognition.compare_faces([img1cv], img2cv)
    return str(result)




app.run()
# Create some test data for our catalog in the form of a list of dictionaries.
# books = [
#     {'id': 0,
#      'title': 'A Fire Upon the Deep',
#      'author': 'Vernor Vinge',
#      'first_sentence': 'The coldsleep itself was dreamless.',
#      'year_published': '1992'},
#     {'id': 1,
#      'title': 'The Ones Who Walk Away From Omelas',
#      'author': 'Ursula K. Le Guin',
#      'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
#      'published': '1973'},
#     {'id': 2,
#      'title': 'Dhalgren',
#      'author': 'Samuel R. Delany',
#      'first_sentence': 'to wound the autumnal city.',
#      'published': '1975'}
# ]

# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>API</h1>"

# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     return jsonify(books)

# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_id():
#     # Check if an ID was provided as part of the URL.
#     # If ID is provided, assign it to a variable.
#     # If no ID is provided, display an error in the browser.
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: No id field provided. Please specify"

#     #create empty list for results
#     results=[]

#     #loop through data and match 
#     for book in books:
#         if book['id'] == id:
#             results.append(book)
    
#     return jsonify(results)

# @app.route('/api/post', methods=['POST'])
# def add_book():
#     book_data = request.get_json()
    

#     return "DONE WHE"

