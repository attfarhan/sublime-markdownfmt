import sublime, sublime_plugin, subprocess, os, sys, json
from os import environ

class SublimeMarkdownfmt(sublime_plugin.EventListener):
	def on_pre_save_async(self, view):
		filename = sublime.View.file_name(view)
		filename_sans_ext, fileext = os.path.splitext(sublime.View.file_name(view))
		markdownfmt_bin, err, rcode = run_native_shell_command(os.environ['SHELL'], ["which", "markdownfmt"])
		if fileext == '.md':
			command = [markdownfmt_bin, "-w", filename]
			subprocess.Popen(command, env=os.environ, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Code snippet taken from sourcegraph-sublime
# (https://github.com/sourcegraph/sourcegraph-sublime/blob/102dfaa4f366f94791cc47556850d1cd4eaffc47/sourcegraph_lib.py#L114)
def run_native_shell_command(shell_env, command):
	if isinstance(command, list):
		command = " ".join(command)
	native_command = [shell_env]
	if 'zsh' in shell_env:
		native_command += ['-i']
	native_command += ['-l', '-c', command]
	if not shell_env or shell_env == '':
		native_command = command.split()
	process = subprocess.Popen(native_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = process.communicate()
	if out:
		out = out.decode().strip().split('\n')[-1]
	if err:
		err = err.decode().strip()
	return out, err, process.returncode
