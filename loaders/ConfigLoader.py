import json
import customtkinter as ctk

class ConfigLoader:
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
            themeName = self.configData["theme"]
            if themeName in ["green", "dark-blue", "blue"]:
                ctk.set_default_color_theme(themeName)
            else: ctk.set_default_color_theme("themes/"+ themeName +".json")

        if "themeMode" in self.configData:
            themeMode = self.configData["themeMode"]
            ctk.set_appearance_mode(themeMode)
            
        if "windowSize" in self.configData:
            windowSize = self.configData["windowSize"]
            size = windowSize.get(windowType, {"x": 800, "y": 600})
            x = size.get("x", 800)
            y = size.get("y", 600)
            app.geometry(f"{x}x{y}")

