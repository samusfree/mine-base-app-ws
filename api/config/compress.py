from flask import Flask
from flask_compress import Compress


def compress_config(app: Flask):
    app.config["COMPRESS_REGISTER"] = True
    app.config["COMPRESS_ALGORITHM"] = "gzip"
    compress = Compress()
    compress.init_app(app)
