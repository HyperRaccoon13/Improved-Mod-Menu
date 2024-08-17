#!python
import argparse
import customtkinter as ctk
from managers import ConfigManager
from managers import AssetManager

def RunArguments():
    parser = argparse.ArgumentParser(description='Launch the HyperModMenu application.')
    parser.add_argument('configPath', type=str, help='Path to the configuration file')
    return parser.parse_args()

configPath = ""

# /-----------------[ Setting Window ]-----------------/#
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
            configManager.ApplyConfig(self)

        settingsMenuMasterFrame = ctk.CTkFrame(self)
        settingsMenuMasterFrame.pack(expand=True, fill='both')

        settingsMenuFrame = ctk.CTkFrame(settingsMenuMasterFrame)
        settingsMenuFrame.pack(side="left", anchor="n", padx=20, pady=20)

        self.themeModeOptionMenu = ctk.CTkOptionMenu(settingsMenuFrame, values=["dark", "light", "system"], command=ThemeModeOptionMenuCallback)
        self.themeModeOptionMenu.pack(pady=(0, 10), padx=10)
        self.themeModeOptionMenu.set(configManager.GetConfigValues("themeMode"))

        self.themeOptionMenu = ctk.CTkOptionMenu(settingsMenuFrame, values=configManager.GetAvailableThemes(configManager.GetConfigValues("themePath")), command=ThemeOptionMenuCallback)
        self.themeOptionMenu.pack(pady=(5, 5), padx=10)
        self.themeOptionMenu.set(configManager.GetConfigValues("theme"))


# /-----------------[ Main Window ]-----------------/#
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("HyperModMenu")

        configManager.ApplyConfig(self, windowType="main")

        mainMenuMasterFrame = ctk.CTkFrame(self)
        mainMenuMasterFrame.pack(expand=True, fill='both')


        settingButtonIcon = ctk.CTkImage(light_image=assetManager.GetAsset("gears-solid"),
                                         dark_image=assetManager.GetAsset("gears-solid"),
                                         size=(40, 30))
        
        self.settings_button = ctk.CTkButton(mainMenuMasterFrame, image=settingButtonIcon, text="",
                                             command=self.OpenSettingPannel,
                                             width=0, height=0, fg_color="transparent")
        self.settings_button.pack(pady=20)


    def OpenSettingPannel(self):
        settingWindow = SettingsWindow(self)
        settingWindow.grab_set()

if __name__ == "__main__":
    runargs = RunArguments()
    configManager = ConfigManager(runargs.configPath)
    assetManager = AssetManager(configManager.GetConfigValues("assetsPath"))
    
    mainModMenu = App()
    mainModMenu.mainloop()