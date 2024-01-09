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
    # Implement logic to detect the image extension, e.g., check the first file in the directory
    # For simplicity, assuming all files in the directory have the same extension
    files = os.listdir(directory)
    if files:
        first_file = files[0]
        _, extension = os.path.splitext(first_file)
        return extension[1:]  # Remove the leading dot from the extension

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
