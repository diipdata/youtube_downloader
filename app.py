import streamlit as st
import yt_dlp
import os

# Configuração inicial da página
st.set_page_config(
    page_title="YouTube Downloader 🎥",
    page_icon="🎧",
    layout="centered"
)

st.title("🎬 YouTube Downloader")
st.markdown("Baixe vídeos ou áudios do YouTube com apenas um clique.")

# Campo para o link do vídeo
url_video = st.text_input("🔗 Cole o link do vídeo do YouTube:", placeholder="Cole o link do youtube aqui")

# Opção para escolher o tipo de download
tipo_download = st.radio("O que você quer baixar?", ["🎧 Áudio (MP3)", "🎥 Vídeo (MP4)"])

# Botão principal
if st.button("Baixar"):
    if not url_video.strip():
        st.warning("⚠️ Por favor, insira um link válido do YouTube.")
    else:
        destino = os.path.join(os.getcwd(), "downloads")
        os.makedirs(destino, exist_ok=True)

        st.info("⏳ Iniciando o download... Isso pode levar alguns segundos.")

        try:
            # Configuração para áudio ou vídeo
            if tipo_download == "🎧 Áudio (MP3)":
                ydl_opts = {
                    "format": "bestaudio/best",
                    "outtmpl": f"{destino}/%(title)s.%(ext)s",
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }],
                }
            else:
                ydl_opts = {
                    "format": "18",  # MP4 360p
                    "outtmpl": f"{destino}/%(title)s.%(ext)s",
                }

            # Executa o download
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url_video, download=True)
                nome_arquivo = ydl.prepare_filename(info)
                if tipo_download == "🎧 Áudio (MP3)":
                    nome_arquivo = os.path.splitext(nome_arquivo)[0] + ".mp3"

            st.success("✅ Download concluído com sucesso!")

            # Exibir botão para baixar o arquivo
            with open(nome_arquivo, "rb") as f:
                st.download_button(
                    label="⬇️ Clique para salvar o arquivo",
                    data=f,
                    file_name=os.path.basename(nome_arquivo),
                    mime="audio/mpeg" if tipo_download == "🎧 Áudio (MP3)" else "video/mp4"
                )

        except Exception as e:
            st.error(f"❌ Ocorreu um erro: {e}")
