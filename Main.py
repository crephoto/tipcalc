import pygame as pg
from pygame.locals import *
import pygame_gui
import pygame, sys
import pygame_widgets
import pygame_menu
import pygame_menu.locals as _locals


window_surface = pg.display.set_mode((600, 800))
pg.font.init()
type_font = pg.font.SysFont(None, 35)
but_font = pg.font.SysFont(None, 35)
per_font = pg.font.SysFont('inkfree', 30)
totfont = pg.font.SysFont(None, 50)
clock = pg.time.Clock()
input_box1 = pg.Rect(200, 100, 140, 32)
button1 = pg.Rect(200, 600, 200, 32)
button2 = pg.Rect(200, 600, 200, 32)
back_blue = (174, 198, 207)
color_inactive = pg.Color('purple')
color_active = pg.Color(102, 102, 102)
color_invalid = pg.Color(100, 0, 0)
color = color_inactive
active = False
mx, my = pg.mouse.get_pos() 
click = False
active = False 

def draw_text(text, totfont, color, surface, x, y):
    textobj = totfont.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect = topleft = (x, y)
    surface.blit(textobj, textrect)


def main(type_font, clock, input_box1, color_inactive, color_active, color_invalid, color):
    pg.font.init()
    mx, my = pg.mouse.get_pos()
    click = False
    active = False
    meal1 = '$'

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
                    cal(meal1)
                    pg.quit(main)

        window_surface.fill(back_blue)
        txt_surface = type_font.render(meal1, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box1.w = width
        window_surface.blit(txt_surface, (input_box1.x+5, input_box1.y+5))
        pg.draw.rect(window_surface, color, input_box1, 2)
        draw_text(("Person A:"), per_font, (255, 255, 255), window_surface, 70, 95)
        # Total Button Designs
        pg.draw.rect (window_surface, (255, 127, 80), button1)
        draw_text(("Total"), but_font, (255, 255, 255), window_surface, 275, 605)
        
        pg.display.update()
        clock.tick()



def cal(meal1):

    running = True
    while running:

        window_surface.fill(back_blue)

        draw_text(meal1, totfont, (255, 255, 255), window_surface, 20, 20)

        # Back Button
        pg.draw.rect (window_surface, (255, 127, 80), button2)
        draw_text(("Back"), but_font, (255, 255, 255), window_surface, 275, 605)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False 
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button2.collidepoint(mouse_pos):
                    main(type_font, clock, input_box1, color_inactive, color_active, color_invalid, color)
                    pg.quit(cal)
                    

            pg.display.update()
            clock.tick()

if __name__ == '__main__':
    pg.init()
    main(type_font, clock, input_box1, color_inactive, color_active, color_invalid, color)
    pg.quit()