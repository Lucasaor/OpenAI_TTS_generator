from openai import OpenAI
from datamodels import ConfigFile
import json
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CONFIG_FILE_PATH = os.getenv("CONFIG_FILE_PATH")

class TTS:
    def __init__(self):
        self.openai = OpenAI()
        with open(CONFIG_FILE_PATH, "r") as fp:
            config = json.load(fp)
        
        self.config = ConfigFile(**config)
        
    async def generate_audio(self, text:str,voice:str=None, speed: float = 1.0,destination_file:str=None)->None:
        assert isinstance(text, str), "Text must be a string"

        if voice is None:
            voice = self.config.voice

        if destination_file is None:
            destination_file = text[:30]+"."+ self.config.response_format

        folder_path = os.path.dirname(destination_file)
        if not os.path.exists(self.config.default_output_folder + folder_path):
            os.makedirs(folder_path)

        if not destination_file.endswith(self.config.response_format):
            destination_file = f"{destination_file}.{self.config.response_format}"
        

        response = self.openai.audio.speech.create(
            model = self.config.model,
            voice = self.config.voice,
            speed = speed,
            response_format=self.config.response_format,
            input = text
        )
        
        response.write_to_file(self.config.default_output_folder + destination_file)