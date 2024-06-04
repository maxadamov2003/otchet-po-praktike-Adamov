import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600

# Цвета
white = (255, 255, 255)
green = (255, 160, 122)

# Создание экрана
screen = pygame.display.set_mode((screen_width, screen_height))
game_name = "FOOTBALL 1X1"                        # название игры

#создаем игровой экран
pygame.display.set_caption(game_name)                # заголовок окна
icon = pygame.image.load('icon.png')                 # загружаем файл с иконкой
pygame.display.set_icon(icon)                        # устанавливаем иконку в окно

# Загрузка фона
background_image = pygame.image.load('football.jpg')

# Загрузка музыки
pygame.mixer.music.load("музыка для игры.mp3")
pygame.mixer.music.set_volume(0.1)

# Функция отображения текста
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Основной цикл игры
def main_menu():
    while True:
        screen.fill(white)
        screen.blit(background_image, (0,0))

        title_font = pygame.font.Font(None, 80)
        draw_text("Игровое меню", title_font, green, screen, 200, 50)

        start_button = pygame.Rect(300, 200, 200, 50)
        pygame.draw.rect(screen, green, start_button)
        draw_text("Старт", title_font, white, screen, 320, 200)

        quit_button = pygame.Rect(300, 300, 200, 50)
        pygame.draw.rect(screen, green, quit_button)
        draw_text("Выход", title_font, white, screen, 300, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):

                    # Configuration
                    pygame.init()
                    fps = 60
                    fpsClock = pygame.time.Clock()

                    # Цвета
                    WHITE = "#FFFFFF"  # Белый
                    GREEN = "#32CD32"  # Зеленый

                    width = 1024  # ширина игрового окна
                    height = 640  # высота игрового окна
                    fps = 50  # частота кадров в секунду
                    game_name = "FOOTBALL 1X1"  # название игры

                    menu_screen = pygame.display.set_mode((width, height))
                    pygame.display.set_caption(game_name)
                    icon = pygame.image.load('icon.png')  # загружаем файл с иконкой
                    pygame.display.set_icon(icon)  # устанавливаем иконку в окно

                    # создаем игровой экран
                    screen1 = pygame.display.set_mode((width, height))  # Создаем игровой экран
                    pygame.display.set_caption(game_name)  # заголовок окна
                    icon = pygame.image.load('icon.png')  # загружаем файл с иконкой
                    pygame.display.set_icon(icon)  # устанавливаем иконку в окно

                    timer = pygame.time.Clock()  # создаем таймер pygame
                     
                    pygame.mixer.music.play(-1) # бесконечное проигрывание музыки

                    score1 = 0  # голы 1 игрока в начале
                    score2 = 0  # голы 2 игрока в начале

                    run = True  # переменная для управления циклом

                    mar = pygame.image.load('марио.png')  # Загружаем спрайт 1 игрока
                    mar_rect = mar.get_rect()  # Получаем рамку спрайта 1 игрока
                    lui = pygame.image.load('луиджи.png')  # Загружаем спрайт 2 игрока
                    lui_rect = lui.get_rect()  # Получаем рамку спрайта 2 игрока
                    ball = pygame.image.load('мяч.png')  # Загружаем спрайт мяча
                    ball_rect = ball.get_rect()  # Получаем рамку спрайта мяча
                    vorota1 = pygame.image.load('vorota1.png')  # Загружаем спрайт ворот 1 игрока
                    vorota1_rect = vorota1.get_rect()  # Получаем рамку спрайта ворот 1 игрока
                    vorota2 = pygame.image.load('vorota2.png')  # Загружаем спрайт ворот 2 игрока
                    vorota2_rect = vorota2.get_rect()  # Получаем рамку спрайта ворот 2 игрока
                    pole = pygame.image.load('pole.png')  # Загружаем спрайт поля
                    pole_rect = pole.get_rect()  # Получаем рамку спрайта поля

                    ball_rect.x = 490  # задаем координату Х мяча
                    ball_rect.y = 290  # задаем координату Y мяча
                    mar_rect.x = 100  # задаем координату Х 1 игрока
                    mar_rect.y = 290  # задаем координату Y 1 игрока
                    lui_rect.x = 924  # задаем координату Х 2 игрока
                    lui_rect.y = 290  # задаем координату Y 2 игрока
                    vorota1_rect.x = 0  # задаем координату Х ворот 1 игрока
                    vorota1_rect.y = 157  # задаем координату Y ворот 1 игрока
                    vorota2_rect.x = 1000  # задаем координату Х ворот 2 игрока
                    vorota2_rect.y = 150  # задаем координату Y ворот 2 игрока

                    while run:  # начинаем бесконечный цикл
                        timer.tick(fps)  # Контроль времени (обновление игры)
                        for event in pygame.event.get():  # Обработка ввода (события)
                            if event.type == pygame.QUIT:  # проверить закрытие окна
                                run = False  # завершаем игровой цикл

                        key = pygame.key.get_pressed()  # Считываем нажатия на клавиши
                        if key[pygame.K_a] and mar_rect.x >= 10:  # Движение влево
                            mar_rect.x -= 10
                        if key[pygame.K_d] and mar_rect.x <= 950:  # Движение вправо
                            mar_rect.x += 10
                        if key[pygame.K_w] and mar_rect.y >= 0:  # Движение вверх
                            mar_rect.y -= 10
                        if key[pygame.K_s] and mar_rect.y <= 550:  # Движение вниз
                            mar_rect.y += 10

                        key = pygame.key.get_pressed()  # Считываем нажатия на клавиши
                        if key[pygame.K_LEFT] and lui_rect.x >= 10:  # Движение влево
                            lui_rect.x -= 10
                        if key[pygame.K_RIGHT] and lui_rect.x <= 950:  # Движение вправо
                            lui_rect.x += 10
                        if key[pygame.K_UP] and lui_rect.y >= 0:  # Движение вверх
                            lui_rect.y -= 10
                        if key[pygame.K_DOWN] and lui_rect.y <= 550:  # Движение вниз
                            lui_rect.y += 10

                        def draw_text1(screen, text, size, x, y, color):
                            font_name = pygame.font.match_font('arial')  # Выбираем тип шрифта для текста
                            font = pygame.font.Font(font_name, size)  # Шрифт выбранного типа и размера
                            text_image = font.render(text, True, color)  # Превращаем текст в картинк
                            text_rect = text_image.get_rect()  # Задаем рамку картинки с тексто
                            text_rect.center = (x, y)  # Переносим текст в координаты
                            screen.blit(text_image, text_rect)  # Рисуем текст на экране

                        screen1.fill(GREEN)  # Заливка заднего фона

                        screen1.blit(pole, pole_rect)  # Отрисовываем поле с рамкой
                        screen1.blit(ball, ball_rect)  # Отрисовываем мяч с рамкой
                        screen1.blit(mar, mar_rect)  # Отрисовываем 1 игрока с рамкой
                        screen1.blit(lui, lui_rect)  # Отрисовываем 2 игрока с рамкой
                        screen1.blit(vorota1, vorota1_rect)  # Отрисовываем ворота 1 игрока с рамкой
                        screen1.blit(vorota2, vorota2_rect)  # Отрисовываем ворота 2 игрока с рамкой

                        n = 0  # Обнуляем счетчик голов 2 игрока
                        m = 0  # Обнуляем счетчик голов 1 игрока

                        # Фактор гола в ворота 1 игрока

                        if ball_rect.colliderect(vorota1_rect):
                            n += 1  # увеличиваем счетчик голов 2 игрока на 1
                            ball_rect.x = 490  # задаем координату Х мяча
                            ball_rect.y = 290  # задаем координату Y мяча
                            mar_rect.x = 100  # задаем координату Х 1 игрока
                            mar_rect.y = 290  # задаем координату Y 1 игрока
                            lui_rect.x = 924  # задаем координату Х 2 игрока
                            lui_rect.y = 290  # задаем координату Y 2 игрока
                        score2 += n  # прибавляем гол 2 игроку

                        # Фактор гола в ворота 2 игрока

                        if ball_rect.colliderect(vorota2_rect):
                            m += 1  # увеличиваем счетчик голов 1 игрока на 1
                            ball_rect.x = 490  # задаем координату Х мяча
                            ball_rect.y = 290  # задаем координату Y мяча
                            mar_rect.x = 100  # задаем координату Х 1 игрока
                            mar_rect.y = 290  # задаем координату Y 1 игрока
                            lui_rect.x = 924  # задаем координату Х 2 игрока
                            lui_rect.y = 290  # задаем координату Y 2 игрока
                        score1 += m  # прибавляем гол 1 игроку

                        if ball_rect.y <= height - 100 or ball_rect.y >= 0 or ball_rect.x <= 980 or ball_rect.x >= 10:  # Условие не выхода мяча за пределы поля
                            if mar_rect.colliderect(
                                    ball_rect) and mar_rect.x <= ball_rect.x and mar_rect.y <= ball_rect.y:  # Столкновение рамок игрока 1 и мяча
                                ball_rect.x += 10  # Изменяем скорость движения мяча по Х и У
                                ball_rect.y += 10
                            if mar_rect.colliderect(
                                    ball_rect) and mar_rect.x >= ball_rect.x and mar_rect.y <= ball_rect.y:
                                ball_rect.x -= 10
                                ball_rect.y += 10
                            if mar_rect.colliderect(
                                    ball_rect) and mar_rect.x <= ball_rect.x and mar_rect.y >= ball_rect.y:
                                ball_rect.x += 10
                                ball_rect.y -= 10
                            if mar_rect.colliderect(
                                    ball_rect) and mar_rect.x >= ball_rect.x and mar_rect.y >= ball_rect.y:
                                ball_rect.x -= 10
                                ball_rect.y -= 10
                            if mar_rect.colliderect(
                                    ball_rect) and mar_rect.x == ball_rect.x and mar_rect.y >= ball_rect.y:
                                ball_rect.y -= 10
                                ball_rect.x += 0
                            if mar_rect.colliderect(
                                    ball_rect) and mar_rect.x >= ball_rect.x and mar_rect.y == ball_rect.y:
                                ball_rect.x -= 10
                                ball_rect.y += 0
                            if mar_rect.colliderect(
                                    ball_rect) and mar_rect.x == ball_rect.x and mar_rect.y <= ball_rect.y:
                                ball_rect.y += 10
                                ball_rect.x += 0
                            if mar_rect.colliderect(
                                    ball_rect) and mar_rect.x <= ball_rect.x and mar_rect.y == ball_rect.y:
                                ball_rect.x += 10
                                ball_rect.y += 0

                        if ball_rect.y <= height - 100 or ball_rect.y >= 0 or ball_rect.x <= 980 or ball_rect.x >= 10:  # Условие невыхода мяча за пределы поля
                            if lui_rect.colliderect(
                                    ball_rect) and lui_rect.x <= ball_rect.x and lui_rect.y <= ball_rect.y:  # Столкновение рамок игрока 2 и мяча
                                ball_rect.x += 10  # Изменяем скорость движения мяча по Х и У
                                ball_rect.y += 10
                            if lui_rect.colliderect(
                                    ball_rect) and lui_rect.x >= ball_rect.x and lui_rect.y <= ball_rect.y:
                                ball_rect.x -= 10
                                ball_rect.y += 10
                            if lui_rect.colliderect(
                                    ball_rect) and lui_rect.x <= ball_rect.x and lui_rect.y >= ball_rect.y:
                                ball_rect.x += 10
                                ball_rect.y -= 10
                            if lui_rect.colliderect(
                                    ball_rect) and lui_rect.x >= ball_rect.x and lui_rect.y >= ball_rect.y:
                                ball_rect.x -= 10
                                ball_rect.y -= 10
                            if lui_rect.colliderect(
                                    ball_rect) and lui_rect.x == ball_rect.x and lui_rect.y >= ball_rect.y:
                                ball_rect.y -= 10
                                ball_rect.x += 0
                            if lui_rect.colliderect(
                                    ball_rect) and lui_rect.x >= ball_rect.x and lui_rect.y == ball_rect.y:
                                ball_rect.x -= 10
                                ball_rect.y += 0
                            if lui_rect.colliderect(
                                    ball_rect) and lui_rect.x == ball_rect.x and lui_rect.y <= ball_rect.y:
                                ball_rect.y += 10
                                ball_rect.x += 0
                            if lui_rect.colliderect(
                                    ball_rect) and lui_rect.x <= ball_rect.x and lui_rect.y == ball_rect.y:
                                ball_rect.x += 10
                                ball_rect.y += 0

                        if ball_rect.x >= 980:  # Условие невыхода мяча за пределы поля
                            ball_rect.x -= 10
                        if ball_rect.x <= 9:
                            ball_rect.x += 10
                        if ball_rect.y >= 550:
                            ball_rect.y -= 10
                        if ball_rect.y <= 0:
                            ball_rect.y += 10

                        draw_text1(screen, f'{score1}', 40, 465, 30, WHITE)  # Выводим на экран количество голов 1 игрока
                        draw_text1(screen, f'{score2}', 40, 560, 30, WHITE)  # Выводим на экран количество голов 2 игрока

                        if score1 == 3:  # Условие окончания игры: 1 игрок забил 3 гола
                            pygame.mixer.music.stop() # Остановка музыки
                            draw_text1(screen, 'PLAYER 1 WIN', 40, 465, 300, WHITE)
                            run = False
                            print('Game over')

                        if score2 == 3:  # Условие окончания игры: 2 игрок забил 3 гола
                            pygame.mixer.music.stop() # Остановка музыки
                            draw_text1(screen, 'PLAYER 2 WIN', 40, 465, 300, WHITE)
                            run = False
                            print('Game over')

                        pygame.display.update()  # Обновляем экран
                    pygame.quit()

                    pygame.display.flip()
                    fpsClock.tick(fps)
                    print("Старт игры")
                if quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()