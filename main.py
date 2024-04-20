import streamlit as st
from datamodels import ConfigFile
from TTS import TTS
from dotenv import load_dotenv
import json
import os
import asyncio

load_dotenv()

CONFIG_FILE_PATH = os.getenv("CONFIG_FILE_PATH")

async def main():
    with open(CONFIG_FILE_PATH, "r") as fp:
        config = json.load(fp)

    config = ConfigFile(**config)
    st.set_page_config(page_title="Black Violet TTS App")
    st.image("img/logo7.png", width=100, use_column_width=True)
    st.title("Gerador de dicas com IA 🎤🎶")
    st.write("Este é um gerador de dicas para playbacks de músicas. Digite o texto e clique em 'Gerar dica' para gerar o áudio.")

    text = st.text_input("Texto da dica (zoeira é sempre incentivada 😁):","")
    speed = st.slider("Velocidade", min_value=0.5, max_value=1.5, value=1.0, step=0.1)
    voice = st.radio("Selecione a Voz", ["alloy🤵🏼", "echo 👨🏻‍💼", "fable 🧑🏽‍💼", "onyx 🧑🏽", "nova 👩🏻‍💼", "shimmer 👩🏼‍💼"], index=4)
    destination_file = st.text_input("Noe do arquivo de saida:", value="audio.mp3")

    if st.button("Gerar Dica! 🚀"):
        if text and destination_file:
            tts = TTS()
            await tts.generate_audio(text,voice,speed, destination_file)
            st.write("Dica gerada com sucesso! 🎉 Preview abaixo:")
            st.audio(config.default_output_folder + destination_file, format='audio/mp3')

if __name__ == "__main__":
    asyncio.run(main())