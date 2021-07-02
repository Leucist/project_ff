import helpers
import socket
import json

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDIconButton, MDRectangleFlatButton
# from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder

from kivy.core.window import Window   # REMOVE --------------------------- >
Window.size = (375, 812)              # REMOVE --------------------------- >

host = socket.gethostbyname(socket.gethostname())
port = 0
server = ("192.168.0.101", 9090)


class Project_FF(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        self.screen = Screen()

        # icon_btn = MDIconButton(icon="language-python", pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.username = Builder.load_string(helpers.username_helper)
        self.password = Builder.load_string(helpers.password_helper)
        log_btn = MDRectangleFlatButton(text="Войти", pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                        on_release=self.check_logs)

        self.screen.add_widget(self.username)
        self.screen.add_widget(self.password)
        self.screen.add_widget(log_btn)
        return self.screen

    def check_logs(self, obj):
        missed = []
        if self.username.text == "":
            missed.append("имя пользователя")
        if self.password.text == "":
            missed.append("пароль")
        # empty_space_error = MDLabel(text="Данное поле должно быть заполнено",
        #                             halign="center",
        #                             theme_text_color="Error",
        #                             font_style="Subtitle2")
        if len(missed) == 2:
            error_msg = 'Необходимо ввести имя пользователя и пароль'
        elif len(missed) == 1:
            error_msg = 'Необходимо ввести ' + missed[0]
        else:  # если введен login и пароль >
            data = {"login": self.username.text, "password": self.password.text}
            data = json.dumps(data)  # data serialized
            # data_loaded = json.loads(data)  # data loaded
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((host, port))
            sock.setblocking(False)
            sock.sendto(data.encode('utf-8'), server)
            return 
        self.dialog = MDDialog(title='[color=ff8c00]Ошибка[/color]',
                               text=error_msg, size_hint=(0.8, 1),
                               buttons=[MDIconButton(icon="close", pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                                     on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


Project_FF().run()
