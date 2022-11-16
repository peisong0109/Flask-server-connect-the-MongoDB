# @Time     : 10/26/2022 08:33 
# @Author   : Peisong Li
# @FileName : Server.py

from flask import request, Flask
import os
import time
from werkzeug.utils import secure_filename
import pymongo
import base64

os.environ['TZ'] = 'Asia/Shanghai'
time.tzset()
app = Flask(__name__)

client = pymongo.MongoClient(host='mongodb://47.243.109.255', port=27017)

db = client.test

collection = db.information


@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


@app.route("/image", methods=['POST', 'GET'])
def get_frame():
    if request.method == 'POST':
        # 
        # img = base64.b64decode(str(request.form['file1']))
        # img=str(request.form['file1'])
        file = request.files['file']
        name = file.filename
        file.save(name)
        datatime = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime())
        image_info = {'name': name, 'data': datatime}
        collection.insert_one(image_info)
        return {'Image received': name}


@app.route('/audio', methods=['POST', 'GET'])
def uploadid():
    if request.method == 'POST':
        # 通过file标签获取文件
        f = request.files['file']
        pro = request.form['pro']
        id = request.form['id']
        datatime = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime())
        # 当前文件所在路径
        basepath = os.path.dirname(__file__)
        # 一定要先创建该文件夹，不然会提示没有该路径
        upload_path = os.path.join(basepath, 'Audio', pro+'-'+datatime+'-'+id+'-'+secure_filename(f.filename))
        # 保存文件
        f.save(upload_path)
        audio_info = {'name': upload_path, 'data': datatime}
        collection.insert_one(audio_info)
        return 'Success.'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
