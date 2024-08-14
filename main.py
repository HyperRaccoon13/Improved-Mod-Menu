
import customtkinter as ctk
from loaders import ConfigLoader
from loaders import AssetLoader

assetPath = "assets"
configPath = "config.json"


class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        configLoader.ApplyConfig(self, windowType="settings")


        def ThemeModeOptionMenuCallback(value):
            configLoader.UpdateConfig("themeMode", value)

        def ThemeOptionMenuCallback(value):
            configLoader.UpdateConfig("theme", value)

        def SettingsMenuRefreshCallback():
            pass

        settingsMenuFrame = ctk.CTkFrame(self)
        settingsMenuFrame.pack(side="left", anchor="n", padx=20, pady=20)

        self.themeModeOptionMenu = ctk.CTkOptionMenu(settingsMenuFrame, values=["dark", "light", "system"], command=ThemeModeOptionMenuCallback)
        self.themeModeOptionMenu.pack(pady=(0, 10), padx=10)
        self.themeModeOptionMenu.set(configLoader.GetConfigValues("themeMode"))

        self.themeOptionMenu = ctk.CTkOptionMenu(settingsMenuFrame, values=["blue", "dark-blue", "green"], command=ThemeOptionMenuCallback)
        self.themeOptionMenu.pack(pady=(5, 5), padx=10)
        self.themeOptionMenu.set(configLoader.GetConfigValues("theme"))

        
        self.settingsMenuRefreshButton = ctk.CTkButton(settingsMenuFrame, text="Refresh", command=SettingsMenuRefreshCallback)
        self.settingsMenuRefreshButton.pack(pady=(10, 0), padx=10)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("HyperModMenu")

        configLoader.ApplyConfig(self, windowType="main")

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

