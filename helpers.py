# ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Subtitle1', 'Subtitle2', 'Body1', 'Body2', 'Button', 'Caption', 'Overline', 'Icon']
screen_helper = """
ScreenManager:
    FirstScreen:
    LoginScreen:
    RegisterScreen:
    HomeScreen:

<FirstScreen>:
    name: 'first'
    MDLabel:
        text: 'АВТОРИЗАЦИЯ'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        font_style: 'H5'
    MDLabel:
        text: 'Войдите в имеющийся аккаунт или нажмите "регистрация", чтобы создать новый'
        halign: 'center'
        size_hint: (0.7, 0.2)
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        theme_text_color: "Secondary"
        font_style: 'Body1'
    MDRectangleFlatButton:
        text: "Войти"
        pos_hint: {'center_x': 0.35, 'center_y': 0.5}
        on_press: root.manager.current = 'login'
    MDRectangleFlatButton:
        text: "Регистрация"
        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
        on_press: root.manager.current = 'register'
    
<LoginScreen>:
    name: 'login'
    MDLabel:
        text: 'ВХОД'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        font_style: 'H4'
    MDTextField:
        id: log_username_field
        hint_text: "Введите имя пользователя"
        icon_right: "account-box"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 270
    MDTextField:
        id: log_password_field
        hint_text: "Введите пароль"
        icon_right: "lock"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 270
    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.2, 'center_y': 0.4}
        on_press: root.manager.current = 'first'
    MDRectangleFlatButton:
        text: "Войти"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: root.check_logs()

<RegisterScreen>:
    id: registerScreen
    name: 'register'
    MDLabel:
        text: 'РЕГИСТРАЦИЯ'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        font_style: 'H5'
    MDTextField:
        id: reg_username_field
        hint_text: "Введите имя пользователя"
        icon_right: "account-box"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 270
    MDTextField:
        id: reg_password_field
        hint_text: "Введите пароль"
        icon_right: "lock"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 270
    MDTextField:
        id: reg_email_field
        hint_text: "Введите e-mail"
        helper_text: "На него придет код с подтверждением"
        helper_text_mode: "on_focus"
        icon_right: "email"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 270
    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.2, 'center_y': 0.3}
        on_press: root.manager.current = 'first'
    MDRectangleFlatButton:
        text: "Создать аккаунт"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: root.check_reg()

<HomeScreen>:
    name: 'home'
    MDLabel:
        text: 'Greetings, u have passed it'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        font_style: 'H6'
"""