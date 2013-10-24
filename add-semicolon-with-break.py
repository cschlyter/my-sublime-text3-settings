import sublime, sublime_plugin

class EndlineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			line = self.view.line(region)
			self.view.insert(edit, line.end(), ";")
			self.view.run_command('run_macro_file', {"file": "res://Packages/Default/Add Line.sublime-macro"})
