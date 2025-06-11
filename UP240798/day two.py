
first_name = 'Fernando'
last_name = 'Gutierrez'
full_name = first_name + ' ' + last_name
country = 'México'
city = 'aguascalientes'
age = 19
year = 2005
is_married = False
is_true = True
is_light_on = True

# Múltiples variables en una línea
x, y, z = 1, 2, 3



# Comprobando el tipo de datos
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Longitud del nombre
print('Longitud del primer nombre:', len(first_name))

# Comparación de longitudes
print('¿El primer nombre es más largo que el apellido?', len(first_name) > len(last_name))

# Operaciones matemáticas
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print('Suma:', total)
print('Resta:', diff)
print('Producto:', product)
print('División:', division)
print('Residuo:', remainder)
print('Potencia:', exp)
print('División entera:', floor_division)

# Círculo
radius = 30
pi = 3.1416
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print('Área del círculo:', area_of_circle)
print('Circunferencia del círculo:', circum_of_circle)

# Entrada del usuario para calcular área
user_radius = float(input('Ingresa el radio del círculo: '))
user_area = pi * user_radius ** 2
print('Área con radio ingresado:', user_area)

# Entradas del usuario
first_name_input = input('Ingresa tu primer nombre: ')
last_name_input = input('Ingresa tu apellido: ')
country_input = input('Ingresa tu país: ')
age_input = input('Ingresa tu edad: ')

print('Nombre completo:', first_name_input + ' ' + last_name_input)
print('País:', country_input)
print('Edad:', age_input)

# Palabras reservadas de Python
help('keywords')  # Este se usa preferentemente desde la consola interactiva
