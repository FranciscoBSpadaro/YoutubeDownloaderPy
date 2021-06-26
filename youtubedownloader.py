from pytube import YouTube

link = input("digite o link do video do youtube: ")
path = input("onde deseja salvar o arquivo?")
yt = YouTube(link)

# Mostra os detalhes do video #
print("Título: ", yt.title)
print("Número de views: ", yt.views)
print("Tamanho do Vídeo: ", yt.length, "Segundos")
print("Avaliação do Vídeo: ", yt.rating)

# Usa a maior resolução #
ys = yt.streams.get_highest_resolution()

# Começa o Download do vídeo #
print("Downloading...")
ys.download(path)
print("Download Completo!!")