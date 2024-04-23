def show_personal_info():
    nimi = "Matti Meikäläinen"
    kunta = "Sodankylä"
    ammatti = "Ohjelmistosuunnittelija"
    print(nimi)
    print(kunta)
    print(ammatti)

def count_seconds(hours, minutes, seconds):
    sekunnit = hours*3600 + minutes*60 + seconds
    return sekunnit

def magazine_serial_check(serial):
    serial = serial.replace("-", "") 
    if len(serial) != 8 or not serial.isdigit():
        return False

    check_sum = 0
    for i, digit in enumerate(serial):
        weight = 8 - i
        check_sum += int(digit) * weight

    return check_sum % 11 == 0

def show_numbered_list(title, data):
    lista = data.split(",")
    lista = [x.strip() for x in lista]
    title = "Lista Hämähäkkimiehen vihollisista: "
    print(title)

    for i, item in enumerate(lista, start=1):
        title = "Lista Hämähäkkimiehen vihollisista: "
        
        print(i, item)
    
    for i, item in enumerate(lista, start=1):
        print(i, item)

def box_volume(width, height, depth):
    return width * height * depth
def ball_volume(radius):
    # PALAUTE: kannattaa käyttää math.pita
    pyoristys = round(4/3 * 3.14 * radius**3, 2)
    return pyoristys
def pipe_volume(radius, height):
    return 3.14 * radius**2 * height

def lotto():
    import random
    lottonumerot = random.sample(range(1, 40), 7)
    return lottonumerot

