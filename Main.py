import pygame as pg
from pygame.locals import *
import pygame_gui
import sys, os
import pygame_widgets
import pygame_menu
import pygame_menu.locals as _locals


window_surface = pg.display.set_mode((600, 800))
pg.font.init()
type_font = pg.font.SysFont(None, 35)
but_font = pg.font.SysFont(None, 35)
per_font = pg.font.SysFont('inkfree', 30)
per_font2 = pg.font.SysFont('inkfree', 24)
totfont = pg.font.SysFont(None, 50)
clock = pg.time.Clock()
input_box1 = pg.Rect(200, 100, 140, 32)
button1 = pg.Rect(200, 600, 200, 32)
button2 = pg.Rect(200, 600, 200, 32)
percentbox = pg.Rect(200, 434, 200, 32)
addpercent = pg.Rect(170, 415, 27, 33)
subpercent =  pg.Rect(170, 454, 27, 33)
back_blue = (174, 198, 207)
color_inactive = pg.Color('purple')
color_active = pg.Color(102, 102, 102)
color_invalid = pg.Color(100, 0, 0)
color = color_inactive
active = False
mx, my = pg.mouse.get_pos() 
click = False
active1 = False
meal1 = ('')
percent = 20
percent1 = str('20')
script_dir = os.path.dirname(__file__)

# easy way to add text onto the window
def draw_text(text, totfont, color, surface, x, y):
    textobj = totfont.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect = topleft = (x, y)
    surface.blit(textobj, textrect)

# first window pop up
def main(type_font, clock, input_box1, color_inactive, color_active, color_invalid, color, meal1, percent, percent1):
    pg.font.init()
    mx, my = pg.mouse.get_pos()
    click = False
    active = False
    percent1 = percent
    percent1 = str(percent1)

    running = True
    while running:

        draw_text(("person 1:"), but_font, (255, 255, 255), window_surface, 150, 105)

        #inputbox1(meal1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box1.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN: 
                            print(meal1)
                            
                    elif event.key == pg.K_BACKSPACE:
                        meal1 = meal1[:-1]
                    else:
                        meal1 += event.unicode
            # total button
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button1.collidepoint(mouse_pos):
                    running = False
                    cal(meal1, percent)
            # percent amount box
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if addpercent.collidepoint(mouse_pos):
                    percent = (percent + 5)
                    percent1 = str(percent)
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if subpercent.collidepoint(mouse_pos):
                    percent = (percent - 5)
                    percent1 = str(percent)

        window_surface.fill(back_blue)
        txt_surface = type_font.render(meal1, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box1.w = width
        window_surface.blit(txt_surface, (input_box1.x+5, input_box1.y+5))
        pg.draw.rect(window_surface, color, input_box1, 2)
        draw_text(("Meal Price ($):"), per_font, (255, 255, 255), window_surface, 15, 95)
        
        # Total Button Designs
        pg.draw.rect (window_surface, (255, 127, 80), button1)
        draw_text(("Total"), but_font, (255, 255, 255), window_surface, 275, 605)
        
        # percent picker
        image = pg.image.load(script_dir+"/breath.png")
        window_surface.blit(image, (135, 400))
            
            # check hit boxes add and subtract arrows (uncomment to check)
        #pg.draw.rect(window_surface, color, addpercent, 2)
        #pg.draw.rect(window_surface, color, subpercent, 2)
            
            # percent box
        pg.draw.rect(window_surface, color, percentbox, 2)
        draw_text((percent1), type_font, (0, 0, 255), window_surface, 283, 439)
        draw_text(("Tip amount (%):"), per_font2, (255, 255, 255), window_surface, 3, 439)

        pg.display.update()
        clock.tick()


# second window pop up
def cal(meal1, percent):

    running = True
    while running:
        
        window_surface.fill(back_blue)
        
        # mathy Stuff
        fin_meal = meal1
        fin_meal = float(fin_meal)
        final_percent = percent/100.0
        add_percent = fin_meal*final_percent
        final_price = (add_percent + fin_meal)
        print_price = round(final_price, 2)
        fin_print = '$' + str(print_price)
        
        # Back Button
        pg.draw.rect (window_surface, (255, 127, 80), button2)
        draw_text(("Back"), but_font, (255, 255, 255), window_surface, 275, 605)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False 
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button2.collidepoint(mouse_pos):
                    running = False
                    main(type_font, clock, input_box1, color_inactive, color_active, color_invalid, color, meal1, percent, percent1)
        
        # checking percent
        meal = meal1
        meal = int(meal)
        if percent > 0:
            if meal >= 0:
                draw_text(fin_print, totfont, (255, 255, 255), window_surface, 20, 20)
            else:
                draw_text("Error price amount is invalid", totfont, (255, 255, 255), window_surface, 20, 20) 
        else:
            draw_text("Error percent amount is invalid", totfont, (255, 255, 255), window_surface, 20, 20) 

        pg.display.update()
        clock.tick()

if __name__ == '__main__':
    pg.init()
    main(type_font, clock, input_box1, color_inactive, color_active, color_invalid, color, meal1, percent, percent1)
    pg.quit()