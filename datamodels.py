from pydantic import BaseModel, field_validator

class ConfigFile(BaseModel):
    model: str
    voice: str
    response_format: str = "mp3"
    default_output_folder: str = "generated_audios"

    @field_validator("model")
    def check_model(cls, value):
        if value not in ["tts-1", "tts-1-hd"]:
            raise ValueError("Invalid model")
        return value
    
    @field_validator("voice")
    def check_voice(cls, value):
        if value not in ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]:
            raise ValueError("Invalid voice")
        return value
    
    @field_validator("response_format")
    def check_response_format(cls, value):
        if value not in ["mp3", "wav", "ogg"]:
            raise ValueError("Invalid response format")
        return value