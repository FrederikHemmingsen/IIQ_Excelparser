from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
import exiftool
import json
from fractions import Fraction

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def custom_json_loads(s, **kwargs):
    return json.loads(s, parse_float=str, **kwargs)

def decimal_to_fraction(exposure_time):
    # Convert string to float for comparison
    exposure_time_float = float(exposure_time)

    # Define common exposure times
    common_exposures = [1/16000, 1/14000, 1/12000, 1/10000, 1/8000, 1/6000, 1/4000, 1/3200, 1/2500, 1/2000, 1/1600, 1/1250, 1/1000, 
                        1/800, 1/640, 1/500, 1/400, 1/320, 1/250, 1/200, 1/160, 
                        1/125, 1/100, 1/80, 1/60, 1/50, 1/40, 1/30, 1/25, 1/20, 
                        1/15, 1/13, 1/10, 1/8, 1/6, 1/5, 1/4, 1/3, 1/2.5, 1/2, 
                        1/1.5, 1]

    # Find the closest common exposure
    closest = min(common_exposures, key=lambda x: abs(x - exposure_time_float))

    # Convert to fraction for string formatting
    frac = Fraction(closest).limit_denominator()
    return f"{frac.numerator}/{frac.denominator}"

def apply_exposure_conversion(metadata):
    if 'EXIF:ExposureTime' in metadata:
        metadata['EXIF:ExposureTime'] = decimal_to_fraction(metadata['EXIF:ExposureTime'])
    return metadata

def extract_exif_data_list(filepath):
    desired_tags = [
        'EXIF:Model',
        'EXIF:ExposureTime',
        'EXIF:FNumber',
        'Composite:LensID',
        'EXIF:FocalLength',
        'EXIF:ISO',
        'XMP:GPSFlightAltitude',
        'XMP:GPSAltitudeAboveTakeOff',
        'XMP:RangeFinderDistance',
        'Composite:HyperfocalDistance',
        'EXIF:CreateDate',
        'Composite:GPSPosition',
        'XMP:GPSSpeed',
        'XMP:GPSSpeedRef',
        'MakerNotes:FirmwareVersions',
        'MakerNotes:SerialNumber',
    ]

    with exiftool.ExifTool() as et:
        et.set_json_loads(custom_json_loads)
        metadata = et.execute_json(*['-j', filepath] + desired_tags)

    if metadata:
        filtered_metadata = {key: metadata[0][key] for key in desired_tags if key in metadata[0]}
        filtered_metadata = apply_exposure_conversion(filtered_metadata)
        return filtered_metadata
    else:
        return {}

def extract_exif_data(filepath):
    with exiftool.ExifTool() as et:
        et.set_json_loads(custom_json_loads)
        metadata = et.execute_json('-j', filepath)

    if metadata:
        metadata = apply_exposure_conversion(metadata[0])
        return metadata
    else:
        return {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        version = request.form.get('version', 'version1')  # Default to version1

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            if version == 'version1':
                exif_data = extract_exif_data(filepath)
            else:  # If version2 or any other value
                exif_data = extract_exif_data_list(filepath)

            return jsonify(exif_data)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)