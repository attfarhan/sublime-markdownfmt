import sublime, sublime_plugin, subprocess, os

class SublimeMarkdownfmt(sublime_plugin.EventListener): 
	def on_pre_save(self, view): 
		print ("active view ", sublime.View.file_name(view))
		command = ["/Users/Farhan/GoWork/bin/markdownfmt", "-w", sublime.View.file_name(view)]
		print(command)
		subprocess.Popen(command, env=os.environ, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
