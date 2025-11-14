![youtube-downloader](img\youtube-downloader.png)

# 🎥 YouTube Downloader

Este projeto foi desenvolvido com o objetivo de aprofundar meus estudos em Python e Streamlit, explorando na prática o consumo de bibliotecas externas, manipulação de mídia e criação de interfaces interativas para aplicações simples. A ideia é consolidar fundamentos de desenvolvimento web com Python, além de entender melhor como fluxos de download, conversão e integração de vídeo funcionam na prática.

## 🧰 Tecnologias Utilizadas

- **Python** — Linguagem principal do projeto  
- **Streamlit** — Framework para criação rápida de interfaces web interativas  
- **yt-dlp** — Biblioteca para download de vídeos e áudios do YouTube  
- **FFmpeg** — Ferramenta de linha de comando usada para processar e converter arquivos de mídia  

## 💡 Decisões Técnicas

Durante o desenvolvimento, optei por utilizar o **yt-dlp** em vez do pytube, devido à sua maior estabilidade, suporte contínuo da comunidade e compatibilidade com as mudanças constantes na estrutura do YouTube. O yt-dlp também oferece mais controle sobre formatos e qualidade de saída, o que facilita a evolução do projeto.

O **FFmpeg** foi integrado para realizar a conversão e combinação de arquivos de áudio e vídeo, garantindo melhor qualidade final e flexibilidade de formatos — um ponto importante para aplicações que lidam com mídia de forma dinâmica.

## 🚀 Próximos Passos

- Adicionar opção de escolha de qualidade/resolução antes do download  
- Implementar barra de progresso e feedback visual durante o processo  
- Criar histórico de downloads dentro da sessão do usuário  
- Explorar deploy completo no Streamlit Cloud ou Vercel  
- Aprofundar estudos em manipulação de mídia com FFmpeg e automação com Python  

## 🛠️ Como executar localmente

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/youtube-downloader.git
cd youtube-downloader

# 2. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação
streamlit run app.py
```

## 🤝 Contribua ou experimente!

Esse projeto é **aberto para colaboração**. Se você tem ideias, encontrou um bug ou quer adicionar uma funcionalidade (tipo download em lote ou suporte a playlists), sinta-se à vontade para abrir uma *issue* ou mandar um *pull request*!

E se quiser só testar, clonar e brincar com o código — **vai fundo!** É tudo feito com carinho e vontade de aprender. Qualquer feedback é super bem-vindo. 💬

---

**Criado por [Diego](https://github.com/diipdata)**  
diegop.freitas@gmail.com | [LinkedIn](https://linkedin.com/in/diegop-freitas) | [X/Twitter](https://x.com/seu-usuario)

*Feito com ☕ e muitas linhas de código (e alguns erros pelo caminho).*