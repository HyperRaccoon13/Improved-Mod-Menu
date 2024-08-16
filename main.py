#!python
import argparse
import customtkinter as ctk
from loaders import ConfigManager
from loaders import AssetManager

def ExecutableArguments():
    parser = argparse.ArgumentParser(description='Launch the HyperModMenu application.')
    parser.add_argument('configPath', type=str, help='Path to the configuration file')
    return parser.parse_args()


class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        configManager.ApplyConfig(self, windowType="settings")


        def ThemeModeOptionMenuCallback(value):
            configManager.UpdateConfig("themeMode", value)
            configManager.ApplyConfig(self)

        def ThemeOptionMenuCallback(value):
            configManager.UpdateConfig("theme", value)


        def SettingsMenuRefreshCallback():
            pass

        settingsMenuFrame = ctk.CTkFrame(self)
        settingsMenuFrame.pack(side="left", anchor="n", padx=20, pady=20)

        self.themeModeOptionMenu = ctk.CTkOptionMenu(settingsMenuFrame, values=["dark", "light", "system"], command=ThemeModeOptionMenuCallback)
        self.themeModeOptionMenu.pack(pady=(0, 10), padx=10)
        self.themeModeOptionMenu.set(configManager.GetConfigValues("themeMode"))

        self.themeOptionMenu = ctk.CTkOptionMenu(settingsMenuFrame, values=["blue", "dark-blue", "green"], command=ThemeOptionMenuCallback)
        self.themeOptionMenu.pack(pady=(5, 5), padx=10)
        self.themeOptionMenu.set(configManager.GetConfigValues("theme"))

        
        self.settingsMenuRefreshButton = ctk.CTkButton(settingsMenuFrame, text="Refresh", command=SettingsMenuRefreshCallback)
        self.settingsMenuRefreshButton.pack(pady=(10, 0), padx=10)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("HyperModMenu")

        configManager.ApplyConfig(self, windowType="main")

        settingButtonIcon = ctk.CTkImage(light_image=assetManager.GetAsset("gears-solid"),
                                         dark_image=assetManager.GetAsset("gears-solid"),
                                         size=(40, 30))
        
        self.settings_button = ctk.CTkButton(self, image=settingButtonIcon, text="",
                                             command=self.OpenSettingPannel,
                                             width=0, height=0, fg_color="transparent")
        self.settings_button.pack(pady=20)


    def OpenSettingPannel(self):
        settingWindow = SettingsWindow(self)
        settingWindow.grab_set()

if __name__ == "__main__":
    exeArgs = ExecutableArguments()
    configManager = ConfigManager(exeArgs.configPath)
    assetManager = AssetManager(configManager.GetConfigValues("assetsPath"))
    mainModMenu = App()
    mainModMenu.mainloop()

