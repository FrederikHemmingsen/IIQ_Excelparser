# IIQ No Bullshit Parser Installation Guide

This guide provides step-by-step instructions on how to set up and run the IIQ No Bullshit Parser.


## what is this? 
This is a quick program to extract Exif data from IIQ Phase One format. 
I found it hard to find the information i neeeded in the exif data as there was so many options.

<img width="637" alt="image" src="https://github.com/FrederikHemmingsen/IIQ_No_Bullshit_Parser/assets/131653152/d2a50693-5972-43fc-a09b-57c0694c2bad">



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
- [exiftool](https://exiftool.org/) (Make sure to add it to your system's PATH)
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
