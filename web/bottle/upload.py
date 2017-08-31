from bottle import *
import cherrypy

@get('/upload') # or @route('/upload')
def upload():
    return '''
        <form action="/upload" method="post" enctype="multipart/form-data">
              Category:      <input type="text" name="category" />
              Select a file: <input type="file" accept="image/png,image/gif,image/jpg,image/jpeg, application/msword, application/vnd.ms-powerpoint, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/pdf, application/vnd.ms-powerpoint" name="upload" />
              <input type="submit" value="Start upload" />
        </form>
    '''
#    <input id="fileId2" type="file" multiple="multiple" name="file" />
#    multiple：是否可以选择多个文件，多个文件时其value值为第一个文件的虚拟路径。

@post('/upload') # or @route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

#    save_path = get_save_path_for_category(category)
    if category == '':
        save_path = upload.filename
    else:
        save_path = category + '/' + upload.filename
    upload.save(save_path) # appends upload.filename automatically
    return 'OK'

run(host='localhost', port=8080, server='paste')
