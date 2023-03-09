# import pdfkit

# options = {'quiet': ''}

# config = pdfkit.configuration(wkhtmltopdf=r'/usr/local/bin/wkhtmltopdf')

# pdfkit.from_url('https://www.daleseo.com/python-venv/', './wehago.pdf', options=options, configuration=config)


# https://pypi.org/project/pyhtml2pdf/
from pyhtml2pdf import converter

converter.convert('https://www.wehago.com/#/main', 'naver.pdf', timeout=2)


# import os
# from pyhtml2pdf import converter

# path = os.path.abspath('NAVER.html')
# converter.convert(f'file:///{path}', 'naver2.pdf', timeout=2)


# import os
# from flask import Flask, request, jsonify
# from pyhtml2pdf import converter
# from flask_cors import CORS;

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})

# @app.route('/convert/html2pdf', methods = ['POST'])
# def html2pdf():
#     data = request.get_json()

#     if 'image' not in data:
#         return "", 400
    
#     path = os.path.abspath('NAVER.html')
#     converter.convert(f'file:///{path}', '{filename}.pdf', timeout=2)

#     return "file", 200