import customtkinter as ctk
from loaders import ConfigLoader
from loaders import AssetLoader

assetPath = "assets/"
configPath = "config.json"

class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        configLoader.applyConfig(self, windowType="settings")
        

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("HyperModMenu")

        configLoader.applyConfig(self, windowType="main")

        settingButtonIcon = ctk.CTkImage(light_image=assetLoader.GetAsset("gears-solid"),
                                         dark_image=assetLoader.GetAsset("gears-solid"),
                                         size=(40, 30))
        
        self.settings_button = ctk.CTkButton(self, image=settingButtonIcon, text="",
                                             command=self.OpenSettingPannel,
                                             width=0, height=0, fg_color="transparent")
        self.settings_button.pack(pady=20)


    def OpenSettingPannel(self):
        settingWindow = SettingsWindow(self)
        settingWindow.grab_set()


if __name__ == "__main__":
    configLoader = ConfigLoader(configPath)
    assetLoader = AssetLoader(assetPath)
    mainModMenu = App()
    mainModMenu.mainloop()

