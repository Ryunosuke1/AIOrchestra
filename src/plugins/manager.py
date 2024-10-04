import importlib.util
import os

class PluginManager:
    def __init__(self, plugin_folder):
        self.plugin_folder = plugin_folder
        self.plugins = {}

    def load_plugins(self):
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(self.plugin_folder, filename))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                self.plugins[module_name] = module

    def get_plugin(self, plugin_name):
        return self.plugins.get(plugin_name)