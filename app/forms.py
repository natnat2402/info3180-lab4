from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import imghdr

'''
def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')
'''
class UploadForm(FlaskForm): 
    file = FileField('File', validators = [DataRequired()])
   
