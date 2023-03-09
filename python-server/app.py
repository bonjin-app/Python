import os
from flask import Flask, request, make_response, send_file
from flask_cors import CORS;
from pyhtml2pdf import converter
import pdfkit
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/convert/v2/url2pdf', methods = ['POST'])
def convert_url2pdf():
    url = request.form.get('url')
    filename = request.form.get('filename', 'output')
    timeout = int(request.form.get('timeout', 2))
    
    # PDF로 변환
    converter.convert(url, 'output.pdf', timeout=timeout)
    
    path = os.path.abspath('output.pdf')
    
    # PDF 파일 읽기
    with open(path, 'rb') as f:
        pdf = f.read()
        
    # PDF 파일 삭제
    os.remove(path)
    
    # PDF 파일을 HTTP response로 반환
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
    return response
   
@app.route('/convert/v2/html2pdf', methods = ['POST'])
def convert_v2_html2pdf():
    # HTML 파일을 읽어옴
    file = request.files['file']
    file.save('input.html')
    
    # 저장한 HTML 파일을 읽어와서 PDF 파일로 변환
    os.system('wkhtmltopdf input.html output.pdf')
    
    path = os.path.abspath('output.pdf')
    
    # PDF 파일 읽기
    with open(path, 'rb') as f:
        pdf = f.read()
        
    # PDF 파일 삭제
    os.remove('input.html')
    os.remove('output.pdf')
    
    # PDF 파일을 HTTP response로 반환
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
    return response 

# html 파일을 받아서 pdfkit으로 바로 응답
@app.route('/convert/html2pdf', methods = ['POST'])
def convert_html2pdf():
    # HTML 파일을 읽어옴
    html = request.files['file'].read().decode('utf-8')
    
    # timeout 값을 받아와서 설정
    timeout = request.form.get('timeout')
    options = {'timeout': int(timeout)} if timeout else {}

    # pdfkit 모듈을 사용하여 PDF로 변환
    pdf = pdfkit.from_string(html, False, options=options)
    
    # PDF 파일을 HTTP response로 반환
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
    return response

@app.route('/')
def index():
    return "Welcome to Python server !!"

if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0', port=5001)