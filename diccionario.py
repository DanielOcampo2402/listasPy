persona ={
    'nombre' : 'Daniel',
    'edad' : 20,
    'estatura':1.72,
    'LeGustaFutbol':True
}

print(persona)
print(persona['nombre'])
print(persona.get('edad'))

persona['carrera'] = 'Ingeniero'
print(persona)