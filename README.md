1. Run
python -m venv myenv
or
py -m venv myenv

sudo apt install python3-venv  # for Linux
python3 -m venv myenv

for virtual environment

2. myenv\Scripts\activate

source myenv/bin/activate

3. pip install -r requirements.txt



tts.ogg will be converted to tts.wav with a sample rate of 22050 Hz, in mono format, and with 16-bit audio depth.
ffmpeg -i tts.ogg -acodec pcm_s16le -ar 22050 -ac 1 tts.wav
