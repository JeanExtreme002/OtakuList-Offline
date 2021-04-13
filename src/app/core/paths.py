from os import environ, listdir
from os.path import exists, join, splitext

def get_filenames_by_extensions(directory, allowed_extensions = [".png", ".jpeg", ".jpg", ".gif"]):
    if not exists(directory): return list()
    return [join(directory, img) for img in listdir(directory) if splitext(img)[-1] in allowed_extensions]

ui_path = "ui"
image_path = "images"
background_path = join(image_path, "backgrounds")
local_storage_path = join(environ["LOCALAPPDATA"], "OtakuList Offline")

application_data_filename = join(local_storage_path, "appdata.json")
application_icon_filename = join(image_path, "icon.ico")

login_window_ui_filename = join(ui_path, "loginWindow.ui")
background_image_filenames = get_filenames_by_extensions(background_path)
