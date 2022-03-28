import random
import json
from time import sleep, time
from datetime import datetime as date
from threading import Thread
import pymysql
import vk_api
from tokenn import main_token
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token = main_token)
longpoll = VkLongPoll(vk_session)

class user:
    def __init__(self, id, rub, stone, pol, level, mode, name, diamond):
        self.id = id
        self.mode = mode
        self.rub = rub
        self.stone = stone
        self.pol = pol
        self.level = level
        self.name = name
        self.diamond = diamond

def get_keyboard(buts):
    nb = []
    for i in range(len(buts)):
        nb.append([])
        for k in range(len(buts[i])):
            nb[i].append(None)
    for i in range(len(buts)):
        for k in range(len(buts[i])):
            text = buts[i][k][0]
            color = {'зеленый' : 'positive', 'красный' : 'negative', 'синий' : 'primary'}[buts[i][k][1]]
            nb[i][k] = {"action": {"type": "text", "payload": "{\"button\": \"" + "1" + "\"}", "label": f"{text}"}, "color": f"{color}"}
    first_keyboard = {'one_time': False, 'buttons': nb, 'inline' : False}
    first_keyboard = json.dumps(first_keyboard, ensure_ascii=False).encode('utf-8')
    first_keyboard = str(first_keyboard.decode('utf-8'))
    return first_keyboard

menu_key = get_keyboard([
    [('💳Обменник', 'зеленый'), ('💼Работа', 'зеленый')],
    [('👤Профиль', 'красный'), ('🏠Дом', 'красный')],
    [('🎲Игры', 'синий')]
])

game_key = get_keyboard([
    [('⛏копать', 'зеленый')],
    [('Назад', 'красный'), ('Кирка', 'синий')]
])

pick_key = get_keyboard([
    [('Назад', 'красный'), ('Улучшить', 'зеленый')]
])

pick1_key = get_keyboard([
    [('Назад', 'красный'), ('Улучшить кирку1', 'зеленый')]
])

pick2_key = get_keyboard([
    [('Назад', 'красный'), ('Улучшить кирку2', 'зеленый')]
])


shop_key = get_keyboard([
    [('💎Алмазы на рубли💸', 'зеленый'), ('⛰Камни на рубли💸', 'зеленый')],
    [('🐟рыба на рубли💸', 'синий'), ('🌊секретная рыба на рубли💸', 'синий')],
    [('Назад', 'красный')]
])

stone_key = get_keyboard([
    [('⛰10', 'зеленый'), ('⛰100', 'синий'), ('⛰1000', 'красный')],
    [('Назад', 'красный')]
])

diamond_key = get_keyboard([
    [('💎1', 'зеленый'), ('💎10', 'синий'), ('💎100', 'красный')],
    [('Назад', 'красный')]
])

shopfish_key = get_keyboard([
    [('🌊1', 'зеленый'), ('🌊10', 'синий'), ('🌊100', 'красный')],
    [('Назад', 'красный')]
])

shopfish1_key = get_keyboard([
    [('🐟10', 'зеленый'), ('🐟100', 'синий'), ('🐟1000', 'красный')],
    [('Назад', 'красный')]
])

bedh3_key = get_keyboard([
    [('Назад', 'красный'), ('Спать', 'синий'), ('Улучшить дом', 'зеленый')]
])

bed_key = get_keyboard([
    [('Назад', 'красный'), ('Спать', 'синий'), ('Улучшить дом до 2 уровня', 'зеленый')]
])

levelhh_key = get_keyboard([
    [('Назад', 'красный'), ('Улучшить дом1', 'зеленый')]
])

bedh2_key = get_keyboard([
    [('Назад', 'красный'), ('Спать', 'синий'), ('Улучшить дом до 3 уровня', 'зеленый')]
])

levelhh2_key = get_keyboard([
    [('Назад', 'красный'), ('Улучшить дом2', 'зеленый')]
])

bed1_key = get_keyboard([
    [('Спать 1 минуту', 'красный'), ('Спать 25 минут', 'синий'), ('Спать 50 минут', 'зеленый')],
    [('Назад', 'красный')]
])

bed2_key = get_keyboard([
    [('Спать 1 минуту', 'красный'), ('Спать 15 минут', 'синий'), ('Спать 30 минут', 'зеленый')],
    [('Назад', 'красный')]
])

bed3_key = get_keyboard([
    [('Спать 1 минуту', 'красный'), ('Спать 10 минут', 'синий'), ('Спать 20 минут', 'зеленый')],
    [('Назад', 'красный')]
])

job_key = get_keyboard([
    [('⛏Шахта', 'зеленый'), ('🐠Рыбалка', 'зеленый')],
    [('Назад', 'красный'), ('📄Раздача листовок', 'красный')]
])

fish_key = get_keyboard([
    [('🎣Ловить', 'зеленый')],
    [('Назад', 'красный'), ('Удочка', 'синий')]
])

fishing_key = get_keyboard([
    [('Назад', 'красный'), ('Улучшить удочку', 'зеленый')]
])

fishing1_key = get_keyboard([
    [('Назад', 'красный'), ('Улучшить удочку1', 'зеленый')]
])

fishing2_key = get_keyboard([
    [('Назад', 'красный'), ('Улучшить удочку2', 'зеленый')]
])

leaflet_key = get_keyboard([
    [('Назад', 'красный'), ('📄Дать листовку', 'зеленый')]
])

play_key = get_keyboard([
    [('📀Монетка', 'зеленый'), ('🎰Рулетка', 'зеленый')],
    [('Назад', 'красный')]
])

monetka_key = get_keyboard([
    [('1руб', 'зеленый'), ('5руб', 'зеленый'), ('10руб', 'зеленый')],
    [('Назад', 'красный')]
])

orel_key = get_keyboard([
    [('Орел', 'синий'), ('Решка', 'зеленый')],
    [('Назад', 'красный')]
])

orel1_key = get_keyboard([
    [('Орел1', 'синий'), ('Решка1', 'зеленый')],
    [('Назад', 'красный')]
])

orel2_key = get_keyboard([
    [('Орел2', 'синий'), ('Решка2', 'зеленый')],
    [('Назад', 'красный')]
])

ruletka_key = get_keyboard([
    [('1 руб', 'синий'), ('5 руб', 'синий'), ('10 руб', 'синий')],
    [('Назад', 'красный')]
])

rulx_key = get_keyboard([
    [('2x', 'красный'), ('5x', 'синий'), ('10x', 'зеленый')],
    [('Назад', 'красный')]
])

rull_key = get_keyboard([
[('Назад', 'красный'), ('Играть на 2x', 'зеленый')]
])

rull1_key = get_keyboard([
[('Назад', 'красный'), ('Играть на 5x', 'зеленый')]
])

rull2_key = get_keyboard([
[('Назад', 'красный'), ('Играть на 10x', 'зеленый')]
])

rulx1_key = get_keyboard([
    [('2x.', 'красный'), ('5x.', 'синий'), ('10x.', 'зеленый')],
    [('Назад', 'красный')]
])

rulx2_key = get_keyboard([
    [('2x..', 'красный'), ('5x..', 'синий'), ('10x..', 'зеленый')],
    [('Назад', 'красный')]
])

back_key = get_keyboard([
    [('Назад', 'красный')]
])

clear_key = get_keyboard([])

def sender(id, text, key):
      vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': key})

def chat_sender(id, text):
      vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})

users = []

while True:
    try:
        con = pymysql.connect(host='localhost', user='root', password='', database='base_db',
                              cursorclass=pymysql.cursors.DictCursor)
        print("connected")
        cur = con.cursor()
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    id = event.user_id
                    msg = event.text.lower()

                    if msg == 'начать':
                        if event.from_chat:
                            chat_sender(event.chat_id, 'Это беседа')
                        if event.from_user:
                            user = vk_session.method("users.get", {"user_ids": event.user_id})
                            name = user[0]['first_name']
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            result = cur.fetchone()
                            if result is None:
                                cur.execute("INSERT INTO accounts (vkid, name, rub, stone, diamond, energy) VALUES (%s, %s, %s)", (event.user_id, name, 0, 0, 0, 0))
                                con.commit()
                                sender(id, "Вы успешно зарегистрировались", menu_key)
                            else:
                                sender(id, "Вы уже зарегистрированы", menu_key)
                                for user in users:
                                    if user.id == id:
                                        sender(id, "Вы уже зарегистрированы", menu_key)

                    if msg == '💼работа':
                        sender(id, 'Удачной работы!', job_key)

                    if msg == '👤профиль':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        rub = result['rub']
                        diamond = result['diamond']
                        stone = result['stone']
                        fishh = result['fishh']
                        fish = result['fish']
                        energy = result['energy']
                        levelh = result['levelh']
                        fishing = result['fishing']
                        pick = result['pick']
                        id = result['id']
                        msgToSend = f'[id{id}|{name}], ✅Профиль:\n' \
                                    f'👤Ваш id в боте: {id}\n'  \
                                    f'💸Ваши рубли: {rub}\n' \
                                    f'💎Ваши алмазы: {diamond}\n' \
                                    f'⛰Ваши камни: {stone}\n' \
                                    f'⚡Ваша энергия: {energy}\n' \
                                    f'🏠Ваш уровень дома: {levelh}\n' \
                                    f'🎣Ваш уровень удочки: {fishing}\n' \
                                    f'⛏Ваш уровень кирки: {pick}\n' \
                                    f'🌊Ваши секретные рыбы: {fishh}\n'\
                                    f'🐟Ваши рыбы: {fish}'
                        if event.from_chat:
                            chat_sender(event.chat_id, msgToSend)
                        if event.from_user:
                            sender(event.user_id, msgToSend, menu_key)
                            user.mode = 'start'

                    if msg == '🎲игры':
                        sender(id, 'Удачной игры', play_key)

                    if msg == '📀монетка':
                        sender(id, 'Удачной игры', monetka_key)

                    if msg == '🎰рулетка':
                        sender(id, 'Выбурите ставку', ruletka_key)

                    if msg == '⛏шахта':
                        sender(id, 'Кликайте на кнопку "Копать"', game_key)
                        user.mode = 'game'

                    if msg == '📄раздача листовок':
                        sender(id, 'Удачной работы', leaflet_key)

                    if msg == 'кирка':
                        sender(id, 'Сдесь вы можете улучшить свою кирку', pick_key)

                    if msg == 'удочка':
                        sender(id, 'Сдесь вы можете улучшить свою удочку', fishing_key)

                    if msg == '💳обменник':
                        sender(id, 'Выберите, что хотите обменять:', shop_key)
                        user.mode = 'shop'

                    if msg == '🐠рыбалка':
                        sender(id, 'Удачной рыбалки', fish_key)

                    if msg == 'назад':
                        sender(id, 'Выберите действие:', menu_key)
                        user.mode = 'start'

                    if msg == '1руб':
                        sender(id, 'Орел или решка?', orel_key)

                    if msg == '5руб':
                        sender(id, 'Орел или решка?', orel1_key)

                    if msg == '10руб':
                        sender(id, 'Орел или решка?', orel2_key)

                    if msg == '1 руб':
                        sender(id, 'Выберите х?', rulx_key)

                    if msg == '5 руб':
                        sender(id, 'Выберите х', rulx1_key)

                    if msg == '10 руб':
                        sender(id, 'Выберите x', rulx2_key)

                    #игра монетка
                    r = random.randint(1, 100)
                    if msg == 'орел':
                        if r >= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 1:
                                rub += 1
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли выпал орел\nУ вас {rub} рублей',
                                       orel_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 1:
                                rub -= 1
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли выпала решка\n У вас {rub} рублей',
                                           orel_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == 'решка':
                        if r >= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 1:
                                rub += 1
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли выпала решка\nУ вас {rub} рублей',
                                       orel_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 1:
                                rub -= 1
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли выпал орел\n У вас {rub} рублей',
                                       orel_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == 'орел1':
                        if r >= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 5:
                                rub += 5
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли выпал орел\nУ вас {rub} рублей',
                                       orel1_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 5:
                                rub -= 5
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли выпала решка\n У вас {rub} рублей',
                                       orel1_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == 'решка1':
                        if r >= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 5:
                                rub += 5
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли выпала решка\nУ вас {rub} рублей',
                                       orel1_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 5:
                                rub -= 5
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли выпал орел\n У вас {rub} рублей',
                                       orel1_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == 'орел2':
                        if r >= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 10:
                                rub += 10
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли выпал орел\nУ вас {rub} рублей',
                                       orel2_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 10:
                                rub -= 10
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли выпала решка\n У вас {rub} рублей',
                                       orel2_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == 'решка2':
                        if r >= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 10:
                                rub += 10
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли выпала решка\nУ вас {rub} рублей',
                                       orel2_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 10:
                                rub -= 10
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли выпал орел\n У вас {rub} рублей',
                                       orel2_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    #Рулетка
                    r = random.randint(1, 100)
                    if msg == '2x':
                        if r >= 70:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 1:
                                rub += 1
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли\nУ вас {rub} рублей',
                                       rulx_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 69:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 1:
                                rub -= 1
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли\n У вас {rub} рублей',
                                       rulx_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == '5x':
                        if r >= 90:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 1:
                                rub += 5
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли\nУ вас {rub} рублей',
                                       rulx_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 89:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 1:
                                rub -= 1
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли\n У вас {rub} рублей',
                                       rulx_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == '10x':
                        if r >= 95:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 1:
                                rub += 10
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли\nУ вас {rub} рублей',
                                       rulx_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 94:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 1:
                                rub -= 1
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли\n У вас {rub} рублей',
                                      rulx_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == '2x.':
                        if r >= 70:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 5:
                                rub += 5
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли\nУ вас {rub} рублей',
                                       rulx1_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 69:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 5:
                                rub -= 5
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли\n У вас {rub} рублей',
                                       rulx1_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == '5x.':
                        if r >= 90:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 5:
                                rub += 25
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли\nУ вас {rub} рублей',
                                       rulx1_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 89:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 5:
                                rub -= 5
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли\n У вас {rub} рублей',
                                       rulx1_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == '10x.':
                        if r >= 95:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 5:
                                rub += 50
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли\nУ вас {rub} рублей',
                                       rulx1_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 94:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 5:
                                rub -= 5
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли\n У вас {rub} рублей',
                                       rulx1_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == '2x..':
                        if r >= 80:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 10:
                                rub += 10
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли\nУ вас {rub} рублей',
                                       rulx2_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 79:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 10:
                                rub -= 10
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли\n У вас {rub} рублей',
                                       rulx2_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == '5x..':
                        if r >= 95:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 10:
                                rub += 50
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли\nУ вас {rub} рублей',
                                       rulx2_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 94:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 10:
                                rub -= 10
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли\n У вас {rub} рублей',
                                       rulx2_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == '10x..':
                        if r >= 99:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 10:
                                rub += 100
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'🎉Вы выйграли\nУ вас {rub} рублей',
                                       rulx2_key)
                            else:
                                sender(id, 'Недостаточно средств', menu_key)

                        elif r <= 98:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            if rub >= 10:
                                rub -= 10
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'😥Увы вы проиграли\n У вас {rub} рублей',
                                       rulx2_key)
                            else:
                                sender(id, 'Недодасточно средств', menu_key)

                    if msg == 'улучшить':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        pick = result['pick']
                        if pick == 1:
                            sender(id, f'Стоимость улучшения на 2 уровень 5 рублей', pick1_key)

                    if msg == 'улучшить кирку1':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        pick = result['pick']
                        rub = result['rub']
                        if pick == 1:
                            if rub >= 5:
                                rub -= 5
                                pick += 1
                                cur.execute("UPDATE accounts set pick=%s WHERE vkid=%s", (pick, id))
                                con.commit()
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'Вы успешно улучшили кирку до 2 уровня', menu_key)
                            else:
                                sender(id, 'У вас недостаточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == '⛏копать':
                        if r >= 99:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            diamond = result['diamond']
                            energy = result['energy']
                            pick = result['pick']
                            if pick == 1:
                                if energy >= 1:
                                    energy -= 1
                                    diamond += 1
                                    cur.execute("UPDATE accounts set diamond=%s WHERE vkid=%s", (diamond, id))
                                    con.commit()
                                    cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                                    con.commit()
                                    sender(id, f'Вы откопали алмаз💎\nУ вас {diamond} алмазов',
                                           game_key)
                                else:
                                    sender(id, 'У вас не осталось эенергии⚡', menu_key)

                        elif r <= 98:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            stone = result['stone']
                            energy = result['energy']
                            pick = result['pick']
                            if pick == 1:
                                if energy >= 1:
                                    energy -= 1
                                    stone += 1
                                    cur.execute("UPDATE accounts set stone=%s WHERE vkid=%s", (stone, id))
                                    con.commit()
                                    cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                                    con.commit()
                                    sender(id, f'Вы откопали камень⛰\n У вас {stone} камней',
                                           game_key)
                                else:
                                    sender(id, 'У вас не осталось эенергии⚡', menu_key)
                                    user.mode = 'game'

                    if msg == 'улучшить':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        pick = result['pick']
                        if pick == 2:
                            sender(id, f'Стоимость улучшения на 3 уровень 10 рублей', pick2_key)

                    if msg == 'улучшить кирку2':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        pick = result['pick']
                        rub = result['rub']
                        if pick == 2:
                            if rub >= 10:
                                rub -= 10
                                pick += 1
                                cur.execute("UPDATE accounts set pick=%s WHERE vkid=%s", (pick, id))
                                con.commit()
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'Вы успешно улучшили кирку до 3 уровня', menu_key)
                            else:
                                sender(id, 'У вас недостаточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == '⛏копать':
                        if r >= 95:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            diamond = result['diamond']
                            energy = result['energy']
                            pick = result['pick']
                            if pick == 2:
                                if energy >= 1:
                                    energy -= 1
                                    diamond += 1
                                    cur.execute("UPDATE accounts set diamond=%s WHERE vkid=%s", (diamond, id))
                                    con.commit()
                                    cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                                    con.commit()
                                    sender(id, f'Вы откопали алмаз💎\nУ вас {diamond} алмазов',
                                           game_key)
                                else:
                                    sender(id, 'У вас не осталось эенергии⚡', menu_key)

                        elif r <= 94:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            stone = result['stone']
                            energy = result['energy']
                            pick = result['pick']
                            if pick == 2:
                                if energy >= 1:
                                    energy -= 1
                                    stone += 1
                                    cur.execute("UPDATE accounts set stone=%s WHERE vkid=%s", (stone, id))
                                    con.commit()
                                    cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                                    con.commit()
                                    sender(id, f'Вы откопали камень⛰\n У вас {stone} камней',
                                           game_key)
                                else:
                                    sender(id, 'У вас не осталось эенергии⚡', menu_key)
                                    user.mode = 'game'

                    if msg == 'улучшить':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        pick = result['pick']
                        if pick == 3:
                            sender(id, f'У вас максимальный уровень кирки', menu_key)

                    r = random.randint(1, 100)
                    if msg == '⛏копать':
                        if r >= 90:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            diamond = result['diamond']
                            energy = result['energy']
                            pick = result['pick']
                            if pick == 3:
                                if energy >= 1:
                                    energy -= 1
                                    diamond += 1
                                    cur.execute("UPDATE accounts set diamond=%s WHERE vkid=%s", (diamond, id))
                                    con.commit()
                                    cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                                    con.commit()
                                    sender(id, f'Вы откопали алмаз💎\nУ вас {diamond} алмазов',
                                           game_key)
                                else:
                                    sender(id, 'У вас не осталось эенергии⚡', menu_key)

                        elif r <= 89:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            stone = result['stone']
                            energy = result['energy']
                            pick = result['pick']
                            if pick == 3:
                                if energy >= 1:
                                    energy -= 1
                                    stone += 1
                                    cur.execute("UPDATE accounts set stone=%s WHERE vkid=%s", (stone, id))
                                    con.commit()
                                    cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                                    con.commit()
                                    sender(id, f'Вы откопали камень⛰\n У вас {stone} камней',
                                           game_key)
                                else:
                                    sender(id, 'У вас не осталось эенергии⚡', menu_key)
                                    user.mode = 'game'

                    #Улучшение удочки
                    if msg == 'улучшить удочку':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fishing = result['fishing']
                        if fishing == 1:
                            sender(id, f'Стоимость улучшения на 2 уровень 5 рублей', fishing1_key)

                    if msg == 'улучшить удочку1':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fishing = result['fishing']
                        rub = result['rub']
                        if fishing == 1:
                            if rub >= 5:
                                rub -= 5
                                fishing += 1
                                cur.execute("UPDATE accounts set fishing=%s WHERE vkid=%s", (fishing, id))
                                con.commit()
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'Вы успешно улучшили удочку до 2 уровня', menu_key)
                            else:
                                sender(id, 'У вас недостаточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == '🎣ловить':
                        if r >= 99:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            fishh = result['fishh']
                            energy = result['energy']
                            fishing = result['fishing']
                            if fishing == 1:
                                if energy >= 1:
                                    energy -= 1
                                    fishh += 1
                                    cur.execute("UPDATE accounts set fishh=%s WHERE vkid=%s", (fishh, id))
                                    con.commit()
                                    cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                                    con.commit()
                                    sender(id, f'Вы поймали секретную рыбу\nУ вас {fishh} секретных рыб',
                                           fish_key)
                                else:
                                    sender(id, 'У вас не осталось эенергии⚡', menu_key)

                        elif r <= 98:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            fish = result['fish']
                            energy = result['energy']
                            fishing = result['fishing']
                            if fishing == 1:
                                if energy >= 1:
                                    energy -= 1
                                    fish += 1
                                    cur.execute("UPDATE accounts set fish=%s WHERE vkid=%s", (fish, id))
                                    con.commit()
                                    cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                                    con.commit()
                                    sender(id, f'Вы поймали рыбу\n У вас {fish} рыб',
                                           fish_key)
                                else:
                                    sender(id, 'У вас не осталось эенергии⚡', menu_key)
                                    user.mode = 'game'

                    if msg == 'улучшить удочку':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fishing = result['fishing']
                        if fishing == 2:
                            sender(id, f'Стоимость улучшения на 3 уровень 10 рублей', fishing2_key)

                    if msg == 'улучшить удочку2':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fishing = result['fishing']
                        rub = result['rub']
                        if fishing == 2:
                            if rub >= 10:
                                rub -= 10
                                fishing += 1
                                cur.execute("UPDATE accounts set fishing=%s WHERE vkid=%s", (fishing, id))
                                con.commit()
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'Вы успешно улучшили удочку до 3 уровня', menu_key)
                            else:
                                sender(id, 'У вас недостаточно средств', menu_key)

                    r = random.randint(1, 100)
                    if msg == '🎣ловить':
                        if r >= 95:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            fishh = result['fishh']
                            energy = result['energy']
                            fishing = result['fishing']
                            if fishing == 2:
                                if energy >= 1:
                                    energy -= 1
                                    fishh += 1
                                    cur.execute("UPDATE accounts set fishh=%s WHERE vkid=%s", (fishh, id))
                                    con.commit()
                                    cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                                    con.commit()
                                    sender(id, f'Вы поймали секретную рыбу\nУ вас {fishh} секретных рыб',
                                           fish_key)
                                else:
                                    sender(id, 'У вас не осталось эенергии⚡', menu_key)

                        elif r <= 94:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            fish = result['fish']
                            energy = result['energy']
                            fishing = result['fishing']
                            if fishing == 2:
                                if energy >= 1:
                                    energy -= 1
                                    fish += 1
                                    cur.execute("UPDATE accounts set fish=%s WHERE vkid=%s", (fish, id))
                                    con.commit()
                                    cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                                    con.commit()
                                    sender(id, f'Вы поймали рыбу\n У вас {fish} рыб',
                                           fish_key)
                                else:
                                    sender(id, 'У вас не осталось эенергии⚡', menu_key)
                                    user.mode = 'game'

                    if msg == 'улучшить удочку':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fishing = result['fishing']
                        if fishing == 3:
                            sender(id, f'У вас максимальный уровень удочки', menu_key)

                    r = random.randint(1, 100)
                    if msg == '🎣ловить':
                        if r >= 90:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            fishh = result['fishh']
                            energy = result['energy']
                            fishing = result['fishing']
                            if fishing == 3:
                                if energy >= 1:
                                    energy -= 1
                                    fishh += 1
                                    cur.execute("UPDATE accounts set fishh=%s WHERE vkid=%s", (fishh, id))
                                    con.commit()
                                    cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                                    con.commit()
                                    sender(id, f'Вы поймали секрутную рыбу\nУ вас {fishh} секрутных рыб',
                                           fish_key)
                                else:
                                    sender(id, 'У вас не осталось эенергии⚡', menu_key)

                        elif r <= 89:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            fish = result['fish']
                            energy = result['energy']
                            fishing = result['fishing']
                            if fishing == 3:
                                if energy >= 1:
                                    energy -= 1
                                    fish += 1
                                    cur.execute("UPDATE accounts set fish=%s WHERE vkid=%s", (fish, id))
                                    con.commit()
                                    cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                                    con.commit()
                                    sender(id, f'Вы поймали рыбу\n У вас {fish} рыб',
                                           fish_key)
                                else:
                                    sender(id, 'У вас не осталось эенергии⚡', menu_key)
                                    user.mode = 'game'

                    if msg == 'назад':
                        sender(id, 'Выберите действие:', menu_key)
                        user.mode = 'start'

                    elif msg == '💎алмазы на рубли💸':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        diamond = result['diamond']
                        sender(id,
                               f'Сколько алмазов вы хотите обменять на рубли?:\nЦена 1 рубль: 10 алмазов\nУ вас {diamond} алмазов',
                               diamond_key)
                        user.mode = 'get_wood_count'

                    elif msg == '⛰камни на рубли💸':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        stone = result['stone']
                        sender(id,
                               f'Сколько камней вы хотите обменять на рубли?:\nЦена 1 рубль: 100 камня\nУ вас {stone} камня',
                               stone_key)
                        user.mode = 'get_stone_count'

                    if msg == '💎1':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        diamond = result['diamond']
                        rub = result['rub']
                        if diamond >= 1:
                            diamond -= 1
                            rub += 0.1
                            cur.execute("UPDATE accounts set diamond=%s WHERE vkid=%s", (diamond, id))
                            con.commit()
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'вы успешно продали 1 алмаз и получили 0.1руб\nВаши алмазы: {diamond}\nВаши рубли: {rub}', diamond_key)
                        else:
                            sender(id, 'У вас недостаточно средств', menu_key)

                    if msg == '💎10':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        diamond = result['diamond']
                        rub = result['rub']
                        if diamond >= 10:
                            diamond -= 10
                            rub += 1
                            cur.execute("UPDATE accounts set diamond=%s WHERE vkid=%s", (diamond, id))
                            con.commit()
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'Вы успешно продали 10 алмазов и получили 1руб\nВаши алмазы: {diamond}\nВаши рубли: {rub}', diamond_key)
                        else:
                            sender(id, 'У вас недостаточно средств', menu_key)

                    if msg == '💎100':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        diamond = result['diamond']
                        rub = result['rub']
                        if diamond >= 100:
                            diamond -= 100
                            rub += 10
                            cur.execute("UPDATE accounts set diamond=%s WHERE vkid=%s", (diamond, id))
                            con.commit()
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'вы успешно продали 100 алмазщв и получили 10руб\nВаши алмазы: {diamond}\nВаши рубли: {rub}', diamond_key)
                        else:
                            sender(id, 'У вас недостаточно средств', menu_key)

                    elif msg == 'назад':
                        sender(id, 'Выберите действие:', menu_key)
                        user.mode = 'start'

                    if msg == '⛰10':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        stone = result['stone']
                        rub = result['rub']
                        if stone >= 10:
                            stone -= 10
                            rub += 0.1
                            cur.execute("UPDATE accounts set stone=%s WHERE vkid=%s", (stone, id))
                            con.commit()
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'вы успешно продали 10 камня и получили 0.1руб\nВаши камни: {stone}\nВаши рубли: {rub}', stone_key)
                        else:
                            sender(id, 'У вас недостаточно средств', menu_key)

                    if msg == '⛰100':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        stone = result['stone']
                        rub = result['rub']
                        if stone >= 100:
                            stone -= 100
                            rub += 1
                            cur.execute("UPDATE accounts set stone=%s WHERE vkid=%s", (stone, id))
                            con.commit()
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'вы успешно продали 100 камня и получили 1руб\nВаши камни: {stone}\nВаши рубли: {rub}', stone_key)
                        else:
                            sender(id, 'У вас недостаточно средств', menu_key)

                    if msg == '⛰1000':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        stone = result['stone']
                        rub = result['rub']
                        if stone >= 1000:
                            stone -= 1000
                            rub += 10
                            cur.execute("UPDATE accounts set stone=%s WHERE vkid=%s", (stone, id))
                            con.commit()
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'вы успешно продали 1000 камня и получили 10руб\nВаши камни: {stone}\nВаши рубли: {rub}', stone_key)
                        else:
                            sender(id, 'У вас недостаточно средств', menu_key)

                    elif msg == '🌊секретная рыба на рубли💸':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fishh = result['fishh']
                        sender(id,
                               f'Сколько секретной рыбы вы хотите обменять на рубли?:\nЦена 1 рубль: 10 секретной рыбы\nУ вас {fishh} секретной рыбы',
                               shopfish_key)
                        user.mode = 'get_wood_count'

                    elif msg == '🐟рыба на рубли💸':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fish = result['fish']
                        sender(id,
                               f'Сколько рыб вы хотите обменять на рубли?:\nЦена 1 рубль: 100 рыб\nУ вас {fish} рыб',
                               shopfish1_key)
                        user.mode = 'get_stone_count'

                    if msg == '🌊1':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fishh = result['fishh']
                        rub = result['rub']
                        if fishh >= 1:
                            fishh -= 1
                            rub += 0.1
                            cur.execute("UPDATE accounts set fishh=%s WHERE vkid=%s", (fishh, id))
                            con.commit()
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'вы успешно продали 1 секретную рыбу и получили 0.1руб\nВаши секретные рыбы: {fishh}\nВаши рубли: {rub}', shopfish_key)
                        else:
                            sender(id, 'У вас недостаточно средств', menu_key)

                    if msg == '🌊10':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fishh = result['fishh']
                        rub = result['rub']
                        if fishh >= 10:
                            fishh -= 10
                            rub += 1
                            cur.execute("UPDATE accounts set fishh=%s WHERE vkid=%s", (fishh, id))
                            con.commit()
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'Вы успешно продали 10 секетных рыб и получили 1руб\nВаши секретные рыбы: {fishh}\nВаши рубли: {rub}', shopfish_key)
                        else:
                            sender(id, 'У вас недостаточно средств', menu_key)

                    if msg == '🌊100':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fishh = result['fishh']
                        rub = result['rub']
                        if fishh >= 100:
                            fishh -= 100
                            rub += 10
                            cur.execute("UPDATE accounts set fishh=%s WHERE vkid=%s", (fishh, id))
                            con.commit()
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'вы успешно продали 100 секретной рыбы и получили 10руб\nВаши секретные рыбы: {fishh}\nВаши рубли: {rub}', shopfish_key)
                        else:
                            sender(id, 'У вас недостаточно средств', menu_key)

                    elif msg == 'назад':
                        sender(id, 'Выберите действие:', menu_key)
                        user.mode = 'start'

                    if msg == '🐟10':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fish = result['fish']
                        rub = result['rub']
                        if fish >= 10:
                            fish -= 10
                            rub += 0.1
                            cur.execute("UPDATE accounts set fish=%s WHERE vkid=%s", (fish, id))
                            con.commit()
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'вы успешно продали 10 рыб и получили 0.1руб\nВаши рыбы: {fish}\nВаши рубли: {rub}', shopfish1_key)
                        else:
                            sender(id, 'У вас недостаточно средств', menu_key)

                    if msg == '🐟100':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fish = result['fish']
                        rub = result['rub']
                        if fish >= 100:
                            fish -= 100
                            rub += 1
                            cur.execute("UPDATE accounts set fish=%s WHERE vkid=%s", (fish, id))
                            con.commit()
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'вы успешно продали 100 рыб и получили 1руб\nВаши рыбы: {fish}\nВаши рубли: {rub}', shopfish1_key)
                        else:
                            sender(id, 'У вас недостаточно средств', menu_key)

                    if msg == '🐟1000':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        fish = result['fish']
                        rub = result['rub']
                        if fish >= 1000:
                            fish -= 1000
                            rub += 10
                            cur.execute("UPDATE accounts set fish=%s WHERE vkid=%s", (fish, id))
                            con.commit()
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'вы успешно продали 1000 рыб и получили 10руб\nВаши рыбы: {fish}\nВаши рубли: {rub}', shopfish1_key)
                        else:
                            sender(id, 'У вас недостаточно средств', menu_key)

                    #работа листовок
                    r = random.randint(1, 100)
                    if msg == '📄дать листовку':
                        if r >= 50:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'Прохожий не взял листовку\nУ вас {rub} рублей',
                                   leaflet_key)

                        elif r <= 49:
                            cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                            con.commit()
                            result = cur.fetchone()
                            rub = result['rub']
                            rub += 0.01
                            cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                            con.commit()
                            sender(id, f'Прохожий взял листовку вы получили 0.01\n У вас {rub} рублей',
                                   leaflet_key)

                    if msg == '🏠дом':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        if levelh == 1:
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            sender(id, f'Добро пожаловать в свой дом',
                                   bed_key)

                    if msg == 'улучшить дом до 2 уровня':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        if levelh == 1:
                            sender(id, f'Стоимость дома 10 рублей', levelhh_key)

                    if msg == 'улучшить дом1':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        rub = result['rub']
                        if levelh == 1:
                            if rub >= 10:
                                rub -= 10
                                levelh += 1
                                cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                                con.commit()
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'Вы успешно улучшили дом до 2 уровня', menu_key)
                            else:
                                sender(id, 'У вас недостаточно средств', menu_key)

                    if msg == 'спать':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        if levelh == 1:
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            sender(id, f'Выберите сколько времени вы хотите спать 1 минута +2 энергии:',
                                   bed1_key)

                    if msg == 'спать 1 минуту':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        energy = result['energy']
                        if levelh == 1:
                            sleep(60)
                            energy += 2
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                            con.commit()
                            sender(id, f'Вы успешно поспали и получули 2 энергии\nУ вас {energy} энергии', menu_key)

                    if msg == 'спать 25 минут':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        energy = result['energy']
                        if levelh == 1:
                            sleep(1500)
                            energy += 50
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                            con.commit()
                            sender(id, f'Вы успешно поспали и получули 50 энергии\nУ вас {energy} энергии', menu_key)

                    if msg == 'спать 50 минут':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        energy = result['energy']
                        if levelh == 1:
                            sleep(3000)
                            energy += 100
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                            con.commit()
                            sender(id, f'Вы успешно поспали и получули 100 энергии\nУ вас {energy} энергии', menu_key)

                    if msg == '🏠дом':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        if levelh == 2:
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            sender(id, f'Добро пожаловать в свой дом 2 уровня',
                                   bedh2_key)

                    if msg == 'улучшить дом до 3 уровня':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        if levelh == 2:
                            sender(id, f'Стоимость дома 50 рублей', levelhh2_key)

                    if msg == 'улучшить дом2':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        rub = result['rub']
                        if levelh == 2:
                            if rub >= 50:
                                rub -= 50
                                levelh += 1
                                cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                                con.commit()
                                cur.execute("UPDATE accounts set rub=%s WHERE vkid=%s", (rub, id))
                                con.commit()
                                sender(id, f'Вы успешно улучшили дом до 3 уровня', menu_key)
                            else:
                                sender(id, 'У вас недостаточно средств', menu_key)

                    if msg == 'спать':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        if levelh == 2:
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            sender(id, f'Выберите сколько времени вы хотите спать 1 минута +3 энергии:',
                                   bed2_key)

                    if msg == 'спать 1 минуту':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        energy = result['energy']
                        if levelh == 2:
                            sleep(60)
                            energy += 3
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                            con.commit()
                            sender(id, f'Вы успешно поспали и получули 3 энергии\nУ вас {energy} энергии', menu_key)

                    if msg == 'спать 15 минут':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        energy = result['energy']
                        if levelh == 2:
                            sleep(900)
                            energy += 50
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                            con.commit()
                            sender(id, f'Вы успешно поспали и получули 50 энергии\nУ вас {energy} энергии', menu_key)

                    if msg == 'спать 30 минут':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        energy = result['energy']
                        if levelh == 2:
                            sleep(1800)
                            energy += 100
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                            con.commit()
                            sender(id, f'Вы успешно поспали и получули 100 энергии\nУ вас {energy} энергии', menu_key)

                    if msg == '🏠дом':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        if levelh == 3:
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            sender(id, f'Добро пожаловать в свой дом 3 уровня',
                                   bedh3_key)

                    if msg == 'улучшить дом':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        if levelh == 3:
                            sender(id, f'У вас максимальный уровень дома', menu_key)

                    if msg == 'спать':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        if levelh == 3:
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            sender(id, f'Выберите сколько времени вы хотите спать 1 минута +5 энергии:',
                                   bed3_key)

                    if msg == 'спать 1 минуту':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        energy = result['energy']
                        if levelh == 3:
                            sleep(60)
                            energy += 5
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                            con.commit()
                            sender(id, f'Вы успешно поспали и получули 5 энергии\nУ вас {energy} энергии', menu_key)

                    if msg == 'спать 10 минут':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        energy = result['energy']
                        if levelh == 3:
                            sleep(600)
                            energy += 50
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                            con.commit()
                            sender(id, f'Вы успешно поспали и получули 50 энергии\nУ вас {energy} энергии', menu_key)

                    if msg == 'спать 20 минут':
                        cur.execute("SELECT * FROM accounts WHERE vkid=%s", (event.user_id,))
                        con.commit()
                        result = cur.fetchone()
                        levelh = result['levelh']
                        energy = result['energy']
                        if levelh == 3:
                            sleep(1200)
                            energy += 100
                            cur.execute("UPDATE accounts set levelh=%s WHERE vkid=%s", (levelh, id))
                            con.commit()
                            cur.execute("UPDATE accounts set energy=%s WHERE vkid=%s", (energy, id))
                            con.commit()
                            sender(id, f'Вы успешно поспали и получули 100 энергии\nУ вас {energy} энергии', menu_key)


    except Exception as ex:
        print(ex)