from utils.text_object import TextObject
from utils.button import Button
from utils import config as c

#Главное меню с пятью кнопками и лого

class MainMenu:
    def create_menu(self):
        for i, (text, handler) in enumerate((('PLAY', on_play),
                                             ('QUIT', on_quit))):
            b = Button(c.menu_offset_x,
                       c.menu_offset_y + (c.menu_button_h + 5) * i,
                       c.menu_button_w,
                       c.menu_button_h,
                       text,
                       handler,
                       padding=5)
            self.objects.append(b)
            self.menu_buttons.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)
