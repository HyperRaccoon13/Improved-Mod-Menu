import json
import customtkinter as ctk
import os

class ConfigManager:
    def __init__(self, configFile):
        self.configFile = configFile
        self.configData = self._LoadConfig()

    def _LoadConfig(self):
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
        


    # /-----------------[ Helper Function ]-----------------/#

    def GetConfigValues(self, key, default=None):
        return self.configData.get(key, default)
    
    def GetAvailableThemes(self, themePath):
        themeName = [os.path.splitext(filename)[0] for filename in os.listdir(themePath) if filename.endswith(".json")]
        return ["green", "dark-blue", "blue"] + themeName
    
    def GetWindowSize(self, windowType, split=False):
        sizeString = self.configData.get("windowSize", {}).get(windowType, "800x600")
        try:
            xString, yString = sizeString.split("x")
            x = int(xString)
            y = int(yString)
        except (ValueError, TypeError):
            x, y = 800, 600

        if split:
            return x, y
        else: return f"{x}x{y}"


    def ApplyConfig(self, app, windowType="main"):
        if "themePath" in self.configData:
            themePath = self.configData["themePath"]

        if "theme" in self.configData:
            themeName = self.configData["theme"]
            if themeName in ["green", "dark-blue", "blue"]:
                ctk.set_default_color_theme(themeName)
            else: ctk.set_default_color_theme(f"{themePath}/{themeName}.json")
            
        if "themeMode" in self.configData:
            themeMode = self.configData["themeMode"]
            ctk.set_appearance_mode(themeMode)
            
        if "windowSize" in self.configData:
            app.geometry(self.GetWindowSize(windowType))

    def UpdateConfig(self, key, value):
        self.configData[key] = value
        self._SaveConfig()

    def _SaveConfig(self):
        try:
            with open(self.configFile, "w") as file:
                json.dump(self.configData, file, indent=4)
        except Exception as e:
            print(f"An error occuurred while saving the config file: {e}")

