import sublime, sublime_plugin
import webbrowser

class open_browser_url(sublime_plugin.TextCommand):

   def run(self,edit):
      url = self.view.file_name()
      url = url.replace('\\', '/')
      url = url.replace('file:////', '/')
      url = url.replace('/home/faron/www/faronintel/html/','f5/')
      url = url.replace('/home/faron/var/Scripts/htmls/','f5/')
      url = 'http://' + url
      webbrowser.open_new(url)
