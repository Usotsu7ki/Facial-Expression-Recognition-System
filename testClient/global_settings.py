
login_style_path=r"login/res/qss/style-1.qss" #1234
camera_style_path=r"cameraWindow/res/qss/style.qss" #123
admin_style_path=r"admin/res/qss/style.qss" #123
contactus_style_path=r"contactUs/res/qss/style.qss"  #123
help_style_path=r"help/res/qss/style.qss" #123
forget_style_path=r"forget/res/qss/style-1.qss" #1234
register_style_path = r"register/res/qss/style-1.qss" #1234

isLocal = False

def change_style_sheet(style):
    global login_style_path, camera_style_path, admin_style_path, contactus_style_path, help_style_path, forget_style_path, register_style_path
    if style == "sea":
        login_style_path = r"login/res/qss/style-2.qss"  # 1234
        camera_style_path = r"cameraWindow/res/qss/style1.qss"  # 123
        admin_style_path = r"admin/res/qss/style1.qss"  # 123
        contactus_style_path = r"contactUs/res/qss/style1.qss"  # 123
        help_style_path = r"help/res/qss/style1.qss"  # 123
        forget_style_path = r"forget/res/qss/style-2.qss"  # 1234
        register_style_path = r"register/res/qss/style-2.qss"  # 1234
    elif style =="sky":
        login_style_path = r"login/res/qss/style-1.qss"  # 1234
        camera_style_path = r"cameraWindow/res/qss/style.qss"  # 123
        admin_style_path = r"admin/res/qss/style.qss"  # 123
        contactus_style_path = r"contactUs/res/qss/style.qss"  # 123
        help_style_path = r"help/res/qss/style.qss"  # 123
        forget_style_path = r"forget/res/qss/style-1.qss"  # 1234
        register_style_path = r"register/res/qss/style-1.qss"  # 1234
    elif style =="desert":
        login_style_path = r"login/res/qss/style-3.qss"  # 1234
        camera_style_path = r"cameraWindow/res/qss/style2.qss"  # 123
        admin_style_path = r"admin/res/qss/style2.qss"  # 123
        contactus_style_path = r"contactUs/res/qss/style2.qss"  # 123
        help_style_path = r"help/res/qss/style2.qss"  # 123
        forget_style_path = r"forget/res/qss/style-3.qss"  # 1234
        register_style_path = r"register/res/qss/style-3.qss"  # 1234
    elif style =="grassland":
        login_style_path = r"login/res/qss/style-4.qss"  # 1234
        camera_style_path = r"cameraWindow/res/qss/style3.qss"  # 123
        admin_style_path = r"admin/res/qss/style3.qss"  # 123
        contactus_style_path = r"contactUs/res/qss/style3.qss"  # 123
        help_style_path = r"help/res/qss/style3.qss"  # 123
        forget_style_path = r"forget/res/qss/style-4.qss"  # 1234
        register_style_path = r"register/res/qss/style-4.qss"  # 1234


