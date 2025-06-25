
# 1. Declarar variables
age = 19                   # integer
height = 1.80              # float
complex_num = 3 + 4j       # complex number

# 2. Área de un triángulo con base y altura del usuario
base = float(input("Enter base: "))
height_triangle = float(input("Enter height: "))
area_triangle = 0.5 * base * height_triangle
print("The area of the triangle is", area_triangle)

# 3. Perímetro del triángulo con lados del usuario
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter_triangle = a + b + c
print("The perimeter of the triangle is", perimeter_triangle)

# 4. Área y perímetro de un rectángulo
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("Area of rectangle:", area_rectangle)
print("Perimeter of rectangle:", perimeter_rectangle)

# 5. Área y circunferencia de un círculo
radius = float(input("Enter radius: "))
pi = 3.14
area_circle = pi * radius ** 2
circumference = 2 * pi * radius
print("Area of the circle:", area_circle)
print("Circumference of the circle:", circumference)

# 6. Pendiente (slope), intersecciones de y = 2x - 2
slope = 2
x_intercept = 2 / 2  # y = 0 => 2x - 2 = 0 => x = 1
y_intercept = -2
print("Slope:", slope)
print("X-intercept:", 1)
print("Y-intercept:", y_intercept)

# 7. Slope y distancia euclidiana entre (2, 2) y (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Slope between points:", slope_points)
print("Euclidean distance:", distance)

# 8. Comparar pendientes
print("Is slope from y=2x-2 equal to slope between points?", slope == slope_points)

# 9. Evaluar y = x^2 + 6x + 9 para diferentes x
x_vals = [-3, 0, 1, 2, -6]
for x in x_vals:
    y = x**2 + 6*x + 9
    print(f"y({x}) = {y}")

# 10. Longitud de 'python' y 'dragon'
print(len('python') != len('dragon'))  # Falsy comparison

# 11. Operador and con 'on' en 'python' y 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 12. Usar 'in' con 'jargon'
print('jargon' in 'I hope this course is not full of jargon.')

# 13. 'on' no está en ambos
print('on' not in 'dragon' and 'on' not in 'python')

# 14. Convertir longitud de 'python' a float y string
length_python = len('python')
print(float(length_python))
print(str(length_python))

# 15. ¿Número par?
num = int(input("Enter a number to check if it's even: "))
print("Is even?", num % 2 == 0)

# 16. División entera de 7 // 3 vs int(2.7)
print(7 // 3 == int(2.7))

# 17. ¿type de '10' es igual a 10?
print(type('10') == type(10))

# 18. int('9.8') vs 10
try:
    print(int('9.8') == 10)
except ValueError:
    print("Cannot convert '9.8' to int")

# 19. Script para calcular pago semanal
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning is", weekly_earning)

# 20. Años vividos a segundos
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

# 21. Mostrar tabla
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125") 



