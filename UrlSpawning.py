import sublime, sublime_plugin
import webbrowser

class open_browser_url(sublime_plugin.TextCommand):

   def run(self,edit):
      url = self.view.file_name()

      url = url.replace('\\', '/')
      url = url.replace('/home/faron/lib/script/htmls/projects','www.faronintel.ca/projects')
      url = url.replace('/home/faron/lib/script/htmls/deployments','www.faronintel.ca/deployments')
      url = url.replace('/home/faron/lib/script/htmls/html','www.faronintel.ca')
      url = url.replace('/home/www/html','www.faronintel.ca')
      url = url.replace('/home/www/faronintel/html','www.faronintel.ca')
      url = url.replace('home/faron/lib/script/nodes/projects','www.faronintel.ca/nodes')
      url = url.replace('home/faron/bin/local/lib/node_modules','www.faronintel.ca/local')
      url = 'http://' + url
      webbrowser.open_new(url)
