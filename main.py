import socket
import json

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDIconButton, MDRectangleFlatButton
# from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from helpers import screen_helper

from kivy.core.window import Window  # REMOVE --------------------------- >

Window.size = (375, 812)  # REMOVE --------------------------- >

server = ('192.168.188.1', 9090)


def send_to_server(data):
    data = json.dumps(data, ensure_ascii=False)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server)
    sock.setblocking(False)
    sock.send(data.encode('utf-8'))
    response = sock.recv(1024)
    return response


class HomeScreen(Screen):
    pass


class FirstScreen(Screen):
    pass


class LoginScreen(Screen):
    def check_logs(self):
        missed = []
        username = self.ids.log_username_field.text
        password = self.ids.log_password_field.text
        if username == "":
            missed.append("имя пользователя")
        if password == "":
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
            data = ['loginform', {"login": username, "password": password}]
            response = send_to_server(data)
            if response == 0:
                sm = ScreenManager()
                sm.add_widget(RegisterScreen(name='HomeScreen'))
            else:
                error_msg = 'Неверный пароль или имя пользователя'  # чисто на всякий~
                if response == 1:
                    error_msg = 'Неверный пароль'
                elif response == 2:
                    error_msg = 'Неверное имя пользователя'
                self.dialog = MDDialog(title='[color=ffc400]Ошибка[/color]',
                                       text=error_msg, size_hint=(0.8, 1),
                                       buttons=[MDIconButton(icon="close", pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                                             on_release=self.close_dialog)]
                                       )
                self.dialog.open()
            return
        self.dialog = MDDialog(title='[color=ffc400]Ошибка[/color]',
                               text=error_msg, size_hint=(0.8, 1),
                               buttons=[MDIconButton(icon="close", pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                                     on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class RegisterScreen(Screen):
    def check_reg(self):
        missed = []
        username = self.ids.reg_username_field.text
        password = self.ids.reg_password_field.text
        email = self.ids.reg_email_field.text
        if username == "":
            missed.append("имя пользователя")
        if password == "":
            missed.append("пароль")
        if email == "":
            missed.append("адрес электронной почты")
        if len(missed) == 3:
            error_msg = 'Необходимо ввести имя пользователя, пароль и адрес электронной почты'
        elif len(missed) == 2:
            error_msg = 'Необходимо ввести ' + missed[0] + ' и ' + missed[1]
        elif len(missed) == 1:
            error_msg = 'Необходимо ввести ' + missed[0]
        else:
            data = ['registerform', {"login": username, "password": password, "email": email}]
            response = send_to_server(data)
            if response == 0:
                pass  # success
            else:
                error_msg = 'Неверный пароль или имя пользователя'  # чисто на всякий~
                if response == 1:
                    error_msg = 'Введен неверный код подтверждения'
                    # ---!!!---------------->
                    # и какие-то тут еще варианты че делать надо предоставить ака "try again"
                    # ---!!!---------------->
                elif response == 2:
                    error_msg = 'Некорректный email-адрес'
                self.dialog = MDDialog(title='[color=ffc400]Ошибка[/color]',
                                       text=error_msg, size_hint=(0.8, 1),
                                       buttons=[MDIconButton(icon="close", pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                                             on_release=self.close_dialog)]
                                       )
                self.dialog.open()
            return
        self.dialog = MDDialog(title='[color=ffc400]Ошибка[/color]',
                               text=error_msg, size_hint=(0.8, 1),
                               buttons=[MDIconButton(icon="close", pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                                     on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


sm = ScreenManager()
sm.add_widget(FirstScreen(name='first'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(RegisterScreen(name='register'))



class Project_FF(MDApp):
    def build(self):

        # ---!!!---------------->
        # check if user is logged from prev.session and some other prefs
        # ---!!!---------------->

        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = "A400"
        self.theme_cls.theme_style = "Dark"
        # self.screen = Screen()
        #
        # # icon_btn = MDIconButton(icon="language-python", pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # self.username = Builder.load_string(helpers.username_helper)
        # self.password = Builder.load_string(helpers.password_helper)
        # log_btn = MDRectangleFlatButton(text="Войти", pos_hint={'center_x': 0.5, 'center_y': 0.4},
        #                                 on_release=self.check_logs)
        #
        # self.screen.add_widget(self.username)
        # self.screen.add_widget(self.password)
        # self.screen.add_widget(log_btn)

        self.screen = Builder.load_string(screen_helper)

        return self.screen

    def on_close(self):
        pass
        # automatically called when user closes the app


Project_FF().run()
