import subprocess
import ffmpeg

class VideoConverter:
    
    def convert_webm_mp4_subprocess(self, input_file, output_file):
        try:
            command = f'ffmpeg -i {input_file} {output_file}'
            subprocess.run(command)
        except Exception as e:
            print(e)
            print("Some error occurred")

    def convert_webm_mp4_module(self, input_file, output_file):
        try:
            stream = ffmpeg.input(input_file)
            stream = ffmpeg.output(stream, output_file)
            ffmpeg.run(stream)
        except Exception as e:
            print(e)
            print("Some error occurred")

converter = VideoConverter()

webm_file_path   = r"C:\Users\sayan\OneDrive\Documents\Chemical Engineering\CRE Lab\screen-recorder-wed-feb-02-2022-13-48-08.webm"
output_file_path = r"C:\Users\sayan\OneDrive\Documents\Chemical Engineering\CRE Lab\screen-recorder-wed-feb-02-2022-13-48-08.mp4"
converter.convert_webm_mp4_module(webm_file_path, output_file_path)
