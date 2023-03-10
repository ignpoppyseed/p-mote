PORT = 60044
import requests, time
def main():
    from flask import Flask, render_template
    from waitress import serve
    import os, random, pyautogui, win32api, socket, time, requests, flask, logging


    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False

    @app.errorhandler(429)
    def limit_reached(e):
        response = flask.make_response({"status": "429", "url": "https://http.cat/429"})
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    @app.errorhandler(404)
    def page_not_found(e):
        response = flask.make_response({"status": "404", "url": "https://http.cat/404"})
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    @app.route('/')
    def home():
        return render_template('index.html')

    '''@app.route('/<req>')
    def central(req):
        print(req)
        return 'hi!'''

    @app.route('/skip_back') 
    def skip_back(): 
        key_code = win32api.MapVirtualKey(0xB1, 0)
        win32api.keybd_event(0xB1, key_code)
        return '', 200, {'Access-Control-Allow-Origin': '*'}

    @app.route('/play_pause') 
    def play_pause(): 
        key_code = win32api.MapVirtualKey(0xB3, 0)
        win32api.keybd_event(0xB3, key_code)
        return '', 200, {'Access-Control-Allow-Origin': '*'}

    @app.route('/skip_forward') 
    def skip_forward(): 
        key_code = win32api.MapVirtualKey(0xB0, 0)
        win32api.keybd_event(0xB0, key_code)
        return '', 200, {'Access-Control-Allow-Origin': '*'}

    @app.route('/vol_down') 
    def vol_down(): 
        key_code = win32api.MapVirtualKey(0xAE, 0)
        win32api.keybd_event(0xAE, key_code)
        return '', 200, {'Access-Control-Allow-Origin': '*'}

    @app.route('/vol_mute')
    def vol_mute(): 
        key_code = win32api.MapVirtualKey(0xAD, 0)
        win32api.keybd_event(0xAD, key_code)
        return '', 200, {'Access-Control-Allow-Origin': '*'}

    @app.route('/vol_up')
    def vol_up(): 
        key_code = win32api.MapVirtualKey(0xAF, 0)
        win32api.keybd_event(0xAF, key_code)
        return '', 200, {'Access-Control-Allow-Origin': '*'}

    @app.route('/youtube_fullscreen')
    def youtube_fullscreen():
        old_position = pyautogui.position()
        pyautogui.moveTo(747, 525)
        pyautogui.click()
        pyautogui.click()
        pyautogui.moveTo(old_position)
        return '', 200, {'Access-Control-Allow-Origin': '*'}

    @app.route('/mouse')
    def mouse_page():
        return render_template('mouse.html')

    @app.route('/mouse_control/<direction>/<step_size>')
    def mouse_control(direction, step_size):
        direction = direction.lower()
        if direction not in ['up', 'down', 'left', 'right']: return '', 400, {'Access-Control-Allow-Origin': '*'}
        if not step_size.isdigit(): return '', 400, {'Access-Control-Allow-Origin': '*'}
        else: step_size = int(step_size)

        if direction == 'up': pyautogui.move(0, -step_size)
        if direction == 'down': pyautogui.move(0, step_size)
        if direction == 'left': pyautogui.move(-step_size, 0)
        if direction == 'right': pyautogui.move(step_size, 0)
        return '', 200, {'Access-Control-Allow-Origin': '*'}

    @app.route('/mouse_click/<button>/<times>')
    def mouse_click(button, times):
        button = button.lower()
        if button not in ['left', 'right']: return '', 400, {'Access-Control-Allow-Origin': '*'}
        if not times.isdigit(): return '', 400, {'Access-Control-Allow-Origin': '*'}
        else: times = int(times)

        pyautogui.click(button=button, clicks=times)

        return '', 200, {'Access-Control-Allow-Origin': '*'}

    @app.route('/keyboard')
    def keyboard_page():
        return render_template('keyboard.html')

    @app.route('/send_text/<text>')
    def send_text(text):
        pyautogui.write(text)
        pyautogui.press('enter')
        return '', 200, {'Access-Control-Allow-Origin': '*'}
    
    '''@app.route('/show_keypress/<key>')
    def show_keypress(key):
        print(key)
        return '', 200, {'Access-Control-Allow-Origin': '*'}
    
    @app.route('/show_keypress')
    def show_keypress_page():
        return render_template('test.html')'''

    print(f'''
                                       888            
                                       888            
                                       888            
88888b.         88888b.d88b.   .d88b.  888888 .d88b.  
888 "88b        888 "888 "88b d88""88b 888   d8P  Y8b 
888  888 888888 888  888  888 888  888 888   88888888 
888 d88P        888  888  888 Y88..88P Y88b. Y8b.     
88888P"         888  888  888  "Y88P"   "Y888 "Y8888  
888                                                   
888                                                   
888

access ip: {socket.gethostbyname(socket.gethostname())}:{PORT}''')
    #logging.getLogger('waitress').setLevel(logging.ERROR)
    serve(app, host="0.0.0.0", port=PORT, threads=6)#, _quiet=True)

import pystray, tkinter, socket
from plyer import notification
from PIL import Image
from tkinter import Tk

def on_exit_clicked(icon):
    webserver.terminate()
    icon.stop()
    notification.notify(title='p-mote shutdown successful!', message=f'webserver terminated and icon removed. thanks for using p-mote!', app_name='p-mote')
def show_credits_message(icon):
    root = Tk()
    root.title('p-mote credits')
    root.geometry('517x70')
    tkinter.Label(root, text = 'created by poppy: https://github.com/ignpoppyseed', font=('Sans-Serif 16')).place(relx=.5, rely=.5,anchor=tkinter.CENTER)
    root.mainloop()
def show_info_message(icon):
    root = Tk()
    root.title('p-mote info')
    root.geometry('402x144')
    tkinter.Label(root, text = f'3/3/23\np-mote should only ever be run locally.\nip: {socket.gethostbyname(socket.gethostname())}:{PORT}\np+lm <3', font=('Sans-Serif 16')).place(relx=.5, rely=.5,anchor=tkinter.CENTER)
    root.mainloop()
def show_start_message():
    root = Tk()
    root.title('p-mote credits')
    root.geometry('517x77')
    tkinter.Label(root, text = f'webserver started!\naccess ip: {socket.gethostbyname(socket.gethostname())}:{PORT}', font=('Sans-Serif 16')).place(relx=.5, rely=.5,anchor=tkinter.CENTER)
    root.mainloop()

def none():
    pass

icon_image = Image.open('static\\images\\remote.png')
icon = pystray.Icon('p-mote', icon_image, 'p-mote')
icon.menu = pystray.Menu(
    pystray.MenuItem('info', show_info_message, default=True),
    pystray.MenuItem('credits', show_credits_message),
    pystray.MenuItem('exit', on_exit_clicked),
    pystray.MenuItem(f'access ip: {socket.gethostbyname(socket.gethostname())}:{PORT}', none),
    )

def check_for_online():
    while True:
        try: 
            requests.get(f'http://{socket.gethostbyname(socket.gethostname())}:{PORT}')
            notification.notify(title='p-mote webserver started!', message=f'access ip: {socket.gethostbyname(socket.gethostname())}:{PORT}', app_name='p-mote')
            return
        except Exception as e: time.sleep(0.3)

if __name__ == '__main__':
    import multiprocessing
    webserver = multiprocessing.Process(target=main)
    online_checker = multiprocessing.Process(target=check_for_online)
    webserver.start()
    online_checker.start()
    icon.run()