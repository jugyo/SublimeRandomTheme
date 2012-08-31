import sublime, sublime_plugin
import os
import random

class RandomThemeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    settings = sublime.load_settings('Preferences.sublime-settings')
    current_theme = settings.get('color_scheme')
    files = os.listdir("%s/%s" % (sublime.packages_path(), 'Color Scheme - Default'))
    themes = [t for t in files if not t.endswith('.cache') and not current_theme.endswith(t)]
    new_theme = random.choice(themes)
    theme_path = "Packages/Color Scheme - Default/%s" % new_theme
    settings.set('color_scheme', theme_path)
    sublime.save_settings('Preferences.sublime-settings')
    sublime.status_message("Theme changed: '%s' => '%s'" % (current_theme, new_theme))
