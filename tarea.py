datos = {
    "nombre":"cesar",
    "edad":26,
    "pais":"colombia"
}
dato = input("Que dato quieres conocer:")
if dato in datos:
    print(datos[dato])
else:
    print("No tenemos ese dato!")
