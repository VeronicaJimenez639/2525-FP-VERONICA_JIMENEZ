# Se creó una matriz 3D para almacenar datos de temperaturas
# 1ra dimensión: Ciudades (3 ciudades: Quito, Guayaquil y Cuenca)
# 2da dimensión: Días de la semana (7 días)
# 3ra dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 5},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 10}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 9}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 37}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 20}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana.

ciudades = ["Quito", "Guayaquil", "Cuenca"]
for ciudad_idx, ciudad in enumerate(temperaturas):    # Recorremos la lista de temperaturas ciudad por ciudad. Con "in enumerate" se ve el índice y el contenido.
    for semana_idx, semana in enumerate(ciudad):      # Recorremos cada semana de esa ciudad.
        suma_temperaturas = sum([dia["temp"] for dia in semana]) # Dentro de cada semana, toma todos los días y suma sus temperaturas.
        promedio = suma_temperaturas / len(semana)     # Se divide entre 7 días para obtener el promedio semanal.
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.0f} grados") #Imprimir el resultado con el nombre de la ciudad y la semana.
