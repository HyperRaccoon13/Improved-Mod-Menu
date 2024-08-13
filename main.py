import customtkinter as ctk
from PIL import Image, ImageTk
import os
import json

assetPath = "assets/"
configPath = "config.json"

class ConfigLoader():
    def __init__(self, configFile):
        self.configFile = configFile
        self.configData = self._loadConfig()
    
    def _loadConfig(self):
        try:
            with open(self.configFile, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {self.configFile} was not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: JSON decoding failed. Please check the config file.")
            return {}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {}

    def applyConfig(self, app, windowType="main"):
        if "theme" in self.configData:
            theme = self.configData["theme"]
            ctk.set_appearance_mode(theme)

        if "windowSize" in self.configData:
            windowSize = self.configData["windowSize"]
            size = windowSize.get(windowType, {"x": 800, "y": 600})
            x = size.get("x", 800)
            y = size.get("y", 600)
            app.geometry(f"{x}x{y}")

class AssetLoader():
    def __init__(self, assetDirectory):
        self.assetDirectory = assetDirectory
        self.assetDictionary = self._createAssetDict()
        self.loadedAssets = {}
        self.loadAssets()

    def _createAssetDict(self):
        assetDictionary = {}

        for root, dirs, files in os.walk(self.assetDirectory):
            for file in files:
                filePath = os.path.join(root, file)
                assetName, _ = os.path.splitext(file)
                assetDictionary[assetName] = filePath
        return assetDictionary
    
    def loadAssets(self):
        for name, path in self.assetDictionary.items():
            try:
                if not os.path.exists(path):
                    print(f"Warning: File not found at {path}")
                    continue
                image = Image.open(path)
                self.loadedAssets[name] = image
            except Exception as e:
                print(f"Failed to load image at {path}. Error: {e}")


    def GetAsset(self, name):
        return self.loadedAssets.get(name)

class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        configLoader.applyConfig(self, windowType="settings")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("HyperModMenu")
        #self.geometry("400x150")

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

