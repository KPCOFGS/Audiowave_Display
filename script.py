import librosa
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2
import argparse
import subprocess
import os
def generate_audio_frames(audio_file, fps, duration=None, sr=44100):
    # Load the audio file
    y, sr = librosa.load(audio_file, sr=sr)

    # Calculate the number of frames
    num_frames = int(len(y) / sr * fps)

    # Calculate the frame duration
    frame_duration = 1 / fps

    # Generate frames
    fig, ax = plt.subplots()
    ax.set_xlim(0, frame_duration)
    ax.set_ylim(-1, 1)  # Assuming the audio is normalized
    ax.axis('off')  # Turn off both x and y axes
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        start_idx = int(frame * sr / fps)
        end_idx = int((frame + 1) * sr / fps)
        t = np.linspace(0, frame_duration, end_idx - start_idx)
        y_frame = y[start_idx:end_idx]
        line.set_data(t, y_frame)
        return line,

    ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True)

    return ani


def save_audio_video(audio_file, output_file, fps, duration=None):
    ani = generate_audio_frames(audio_file, fps, duration)
    writer = animation.FFMpegWriter(fps=fps)
    ani.save(output_file, writer=writer)
parser = argparse.ArgumentParser(description='Generate audio visualization video.')
parser.add_argument('--input-path', type=str, required=True, help='Path to the input audio file')
parser.add_argument('--output-path', type=str, default='output.mp4', help='Path to the output video file')
parser.add_argument('--fps', type=int, default=16, help='Frames per second for the output video')
# Path to your audio file
args = parser.parse_args()

audio_file = args.input_path
output_file = "temp.mp4"
fps = args.fps

# Save audio video
save_audio_video(audio_file, output_file, fps)

# Combine audio and video using ffmpeg
cmd = f'ffmpeg -y -i {audio_file} -i {output_file} -c:v copy -c:a aac -strict experimental {args.output_path}'
subprocess.call(cmd, shell=True)
os.remove(output_file)
print('Audio and video combined successfully!')
