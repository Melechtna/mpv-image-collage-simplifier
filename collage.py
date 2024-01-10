import sys
import os

def create_mpv_command(directory, fps, audio_file=None):
    if directory.endswith('/'):
        directory = directory[:-1]

    directory = os.path.abspath(directory)
    image_extension = detect_image_extension(directory)

    if audio_file:
        command = f'mpv --mf-fps={fps} --audio-files={audio_file} "mf://{directory}/*.{image_extension}"'
    else:
        command = f'mpv --mf-fps={fps} "mf://{directory}/*.{image_extension}"'

    return command


def detect_image_extension(directory):
    # Implement logic to detect the image extension, e.g., check the first image file in the directory
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    files = os.listdir(directory)

    for file in files:
        _, extension = os.path.splitext(file)
        if extension.lower() in image_extensions:
            return extension[1:]

    raise ValueError("No image files found in the specified directory")


def main():
    if len(sys.argv) < 3:
        print("Usage: collage.py <input_directory> <fps> [optional_audio_file]")
        sys.exit(1)

    folder_name = sys.argv[1]
    fps = sys.argv[2]

    audio_file = None
    if len(sys.argv) == 4:
        audio_file = sys.argv[3]

    directory = os.path.abspath(folder_name)

    command = create_mpv_command(directory, fps, audio_file)
    print("Executing command:", command)
    os.system(command)

if __name__ == "__main__":
    main()
