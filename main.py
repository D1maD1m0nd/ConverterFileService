# servefile.py
import os
from os import abort

import chardet
from flask import Flask, send_from_directory, flash, request, url_for, Response, stream_with_context, make_response, \
    send_file
from werkzeug.utils import redirect, secure_filename

from Converter import ConverterUtils

app = Flask(__name__)


@app.route('/stream_data', methods=['POST'])
def stream_data():

    # contentType = request.headers['content_type']
    # contentLength = request.headers['total_content_length']
    fileName = request.headers['Content-Disposition']
    data = request.data
    # print('total_content_length', contentLength)
    # request.get_data(parse_form_data=True)
    utils = ConverterUtils()
    utils.saveFile(fileName, data)

    outputFileName = fileName.replace(".docx", ".pdf")
    utils.onThreadStart()
    utils.convertDocToPdf(fileName, outputFileName)

    return send_file(outputFileName)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
