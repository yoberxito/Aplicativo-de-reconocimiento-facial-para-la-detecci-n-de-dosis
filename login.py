import PySimpleGUI as sg

sg.theme('DarkPurple1')

def iniciar_sesion(usuario, password):
	if(usuario == "" or password ==""):
		sg.popup_error('Debes rellenar los campes')
	else:
		if(usuario == "ycieza@gmail.com" and password == "1234"):
			sg.popup_ok("Usuario y PASSWORD correctos")
		else:
			sg.popup_error("Usuario o PASSWORD incorrectos")
layout = [
	[sg.Image(filename='images/login.png', pad=((95, 0), (10, 10)))
	],
	[sg.Text('usuario: ', size=(100, 1), justification='center')],
	[sg.InputText('', pad=((0, 0),(1, 10)), key='user')],
	[sg.Text('PASSWORD: ', size=(100, 1), justification='center')],
	[sg.InputText('', password_char="*", key='password')],
	[sg.Button('Iniciar Sasion', key='login'), sg.Button('Cancelar', key='close')]
	]
Window = sg.Window('login', layout, size=(250,250))
while True:
	event, values = Window.read()
	if event == sg.WIN_CLOSED or event =='close':
		break
	elif(event == 'login'):
		iniciar_sesion(values['user'], values['password'])