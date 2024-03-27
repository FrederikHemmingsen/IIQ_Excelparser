# IIQ No Bullshit Parser Installation Guide

This guide provides step-by-step instructions on how to set up and run the IIQ No Bullshit Parser.


## what is this? 
This is a quick program to extract Exif data from IIQ phaseone format. 
I found it hard to find the information i neeeded in the exif data as there was so many options.

![billede](https://github.com/FrederikHemmingsen/IIQ_No_Bullshit_Parser/assets/131653152/28677619-9d98-4ba3-aede-200ea5722c82)



## Edit filter 
You can edit the list you want to have filtered in the code

```bash
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
```

## Prerequisites
Before you begin, ensure you have the following installed on your system:

- Python (version more than than 3.12.2)
- exiftool (Make sure to add it to your system's PATH)
- GIT

## Installation

Follow these steps to install and run the IIQ No Bullshit Parser:

### 1. Clone the Repository

First, clone the repository using GIT:

```bash
git clone https://github.com/FrederikHemmingsen/IIQ_No_Bullshit_Parser.git
```

### 2. Navigate to the Project Directory

Change your directory to the cloned repository:

```bash
cd IIQ_No_Bullshit_Parser
```

### 3. Install Poetry

If you do not have Poetry installed on your system, install it using pip:

```bash
pip install poetry
```

### 4. Install Dependencies

From the project directory, install the required dependencies using Poetry:

```bash
poetry install
```

## Running the Program

With all dependencies installed, you can now run the program:

```bash
poetry run python main.py
```

This command will execute the `main.py` script using Poetry, which handles dependencies and virtual environments.
