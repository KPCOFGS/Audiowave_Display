# Audiowave_Display

A simple script that will display audiowave for an audio/video file at a custom frames per second

## Download

You can download the script using `git`
```bash
git clone https://github.com/KPCOFGS/Audiowave_Display.git
cd Audiowave_Display
```
You can install the dependencies using pip:
```bash
pip install -r requirements.txt
```

## Parameters

`--input-path INPUT_PATH` Required. Path to your audio/video file

`--output-path OUTPUT_PATH` Optional. Output path, default to the current working directory

`--fps FPS` Optional. Custom frames per second, default to 16

## Usage
To use the script, you need to specify the parameters. For example:
```bash
python script.py --input-path YOUR_FILE
```

## Note
- For a video file, this script will replace the original video display to audiowave display
- This script will use ffmpeg, make sure you have that installed
- The script may use lots of CPU power

## License
This repository is licensed under the [Unlicense](LICENSE)
