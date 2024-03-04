import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# 获取 downloads 目录下的文件

def get_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

# 渲染主界面
@app.route('/')
def index():
    files = get_all_files('downloads')
    return render_template('index.html', files=files)

# 点击链接下载
@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory('downloads', filename, as_attachment=True)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
