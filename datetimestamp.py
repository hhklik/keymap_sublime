import datetime, getpass
import sublime, sublime_plugin
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    """
    Función para generar valores aleatorios
    Puede recibir:
        size = longitud de la cadena
            Defecto 6
        chars = caracteres a utilizar para buscar la cadena
            Defecto letras mayusculas y numeros
    """
    return ''.join(random.choice(chars) for _ in range(size))

class AddDateTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%d/%m/%Y") } )

class AddDateStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%d/%m/%Y/") } )

class AddTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%H:%M:%S") } )

class AddRandomStringAllCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  id_generator(10) } )

class AddRandomStringLowercaseCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  id_generator(10,string.ascii_lowercase) } )

class AddRandomStringUppercaseCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  id_generator(10,string.ascii_uppercase) } )

class AddRandomStringOnlyLettersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  id_generator(10,string.ascii_uppercase + string.ascii_lowercase) } )
