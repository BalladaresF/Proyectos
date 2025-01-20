from pytubefix import YouTube
import os

print("Ingrese el enlace del video por descargar:")
link = input()
yt = YouTube(link)

#print("\nTítulo: ", yt.title)
#print("Visitas: ",yt.views)
#print("Longitud: ",yt.length," seconds")
#print("Description: ",yt.description)
#print("Ratings: ",yt.rating)

print("\nDesea descargar el video o el audio?\n1. Video.\n2. Audio.")
Respuesta=input()
YouTube.use_po_token=True

match Respuesta:
    case "1":
         print("\nDescargando video. . .")
         ys = yt.streams.get_highest_resolution()
         ys.download(r'D:\Visual Studio code\Python projects\Videos descargados\Videos')
         print("El video ha sido descargado.\n")
    case "2":
         print("\nDescargando audio. . .")
         video = yt.streams.filter(only_audio=True).first()
         out_file = video.download(r'D:\Visual Studio code\Python projects\Videos descargados\Audios')
         base, ext = os.path.splitext(out_file)
         new_file = base + '.mp3'
         os.rename(out_file, new_file)
         print("El audio ha sido descargado.\n")
    case _:
        print("Respuesta no válida.")
