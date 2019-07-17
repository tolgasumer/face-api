from flask import Flask, send_file
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from face_recognition_knn import predict, show_prediction_labels_on_image
from io import BytesIO
from PIL import Image
import werkzeug
import os

app = Flask(__name__)
CORS(app)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument(
    'file', type=werkzeug.datastructures.FileStorage, location='files')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

## util for serving a PIL image object
def serve_pil_image(pil_img):
    cached_img = BytesIO() # caching the file
    pil_img.save(cached_img, 'JPEG', quality=70)
    cached_img.seek(0)
    return send_file(cached_img, mimetype='image/jpeg')

# util that takes a normal FileStorage image file and resizes it
def resize_image(img_file):
    pil_img = Image.open(img_file) # turn the image file into a pil image
    pil_img.thumbnail((1000,1000),Image.ANTIALIAS) # resize the image while keeping the aspect ratio, max=1000,1000
    cached_img = BytesIO() # caching the file
    pil_img.save(cached_img, 'JPEG', quality=70) # saving the pil image into an imagefile
    return cached_img


class PhotoUpload(Resource):

    def post(self):
        data = parser.parse_args()
        if data['file'] == "":
            return {
                'data': '',
                'message': 'No file found',
                'status': 'error'
            }
        photo = data['file']

        if photo:
            print(photo)
            resized_photo = resize_image(photo) # resize photo
            predictions = predict(resized_photo, model_path="trained_knn_model.clf") # use the trained model to get predictions
            result_img = show_prediction_labels_on_image(resized_photo, predictions) # draw prediction labels on the image
            return serve_pil_image(result_img) # use the serve_pil_image middleware to serve the image without saving it
        return {
            'data': '',
            'message': 'Something went wrong',
            'status': 'error'
        }


api.add_resource(HelloWorld, '/')
api.add_resource(PhotoUpload, '/upload')

if __name__ == '__main__':
    app.run(debug=True)
