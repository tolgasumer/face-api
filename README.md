<h1 align="center">Combining the famous [face_recognition](https://github.com/ageitgey/face_recognition) library with a simple flask backend that can receive images and respond with the labeled ones, without saving them locally</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/kefranabg/readme-md-generator#readme">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/kefranabg/readme-md-generator/graphs/commit-activity">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" target="_blank" />
  </a>
  <a href="https://github.com/kefranabg/readme-md-generator/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
</p>

> Simple Flask backend to serve face_recognition.py functions via REST

### 🏠 [Homepage](https://github.com/kefranabg/readme-md-generator#readme)

## Install

```sh
pip3 install -r requirements.txt
```

## Usage

To run the server with the sample model
```sh
python3 api.py
```

To train your own KNN classifier with your dataset, place your images according to the structure below:
```sh
images/train/
        ├── <person1_name>/
        │   ├── <someimage1>.jpeg
        │   ├── <someimage2>.jpeg
        │   ├── ...
        ├── <person2_name>/
        │   ├── <someimage1>.jpeg
        │   └── <someimage2>.jpeg
        └── ...
```
```sh
python3 train.py
```

The trained model will be placed in the root folder, named as "trained_knn_model.clf"

## Run tests

```sh
npm run test
```

## Author

👤 **Tolga Sümer**

* Github: [@tolgasumer](https://github.com/tolgasumer)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/kefranabg/readme-md-generator/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [Tolga Sümer](https://github.com/tolgasumer).<br />
This project is [MIT](https://github.com/kefranabg/readme-md-generator/blob/master/LICENSE) licensed.

***