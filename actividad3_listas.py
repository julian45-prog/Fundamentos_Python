# Actividad 3 : Gestion de Lista de Reproduccion Musical

canciones = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Imagine", "Smells Like Teen Spirit"]
append_cancion = "Sweet Child O' Mine"
canciones.append(append_cancion)
canciones.insert(2, "Hey Jude")
canciones.extend(["Bonus Track 1", "Bonus Track 2"])

canciones.remove("Imagine")
canciones.pop(3)

sorted_canciones = sorted(canciones)
reverse_canciones = sorted(canciones, reverse=True)

#¿cuantas canciones tiene la playlist
numero_canciones = len(canciones)
print(f"La playlist tiene {numero_canciones} canciones.")
# en que posicion se encuentra la primera cancion que agregue?
posicion_append = canciones.index(append_cancion)
print(f"La canción '{append_cancion}' se encuentra en la posición {posicion_append} de la playlist.")
#cuantas veces aparece el string bonuus track 1
veces_bonus_track_1 = canciones.count("Bonus Track 1")
print(f"La canción 'Bonus Track 1' aparece {veces_bonus_track_1} veces en la playlist.")