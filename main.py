from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
import exiftool

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    file = request.files.get('file')
    if file:
      filename = secure_filename(file.filename)
      filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      file.save(filepath)
      exif_data = extract_exif_data(filepath)
      return jsonify(exif_data)
  return render_template('upload.html')


"""
#This works for a predefined list:
def extract_exif_data(filepath):
  # Predefined list of EXIF tags you are interested in
  desired_tags = ['EXIF:DateTimeOriginal', 'EXIF:Make', 'EXIF:Model', 'EXIF:GPSLatitude', 'EXIF:GPSLongitude']

  with exiftool.ExifTool() as et:
      # Only fetch the desired EXIF tags
      metadata = et.execute_json(*['-j', filepath] + desired_tags)

  # Filter out only the desired tags from the metadata (if any)
  if metadata:
      filtered_metadata = {key: metadata[0][key] for key in desired_tags if key in metadata[0]}
      return filtered_metadata
  else:
      return {}

"""


#this works for the whole list
def extract_exif_data(filepath):
  with exiftool.ExifTool() as et:
    # Unpack the list to separate arguments with the * operator
    metadata = et.execute_json('-j', filepath)

  return metadata[0] if metadata else {}


if __name__ == '__main__':
  app.run(debug=True)
