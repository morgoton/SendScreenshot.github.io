# modules

from selenium import webdriver # указываем модуль webdriver из selenium для работы с web-формами
from time import sleep # указываем модуль sleep из time для перерыва между действиями
from email.mime.multipart import MIMEMultipart # указываем модуль MIMEMultipart из email для указания основных данных при отправки письма
from email.mime.text import MIMEText # указываем модуль MIMEText из email для прикрепления текста в письме
from email.mime.base import MIMEBase # указываем модуль MIMEBase из email для прикрепления вложения
from email import encoders # указываем модуль encoders из email для прикрепления вложения при работе с 64-битной системой
import smtplib # импортируем библиотеку smtplib для работы с сервером smtp
import os.path # импортируем библиотеку os.path для работы с файлами в системе (указание директории)
import shutil # импортируем библиотеку shutil для работы с файлами в системе (изменение директории)

# code

driver = webdriver.Chrome() # создаем переменную для работы с framework webdriver selenium для браузера Chrome
driver.get('https://github.com/login') # открываем web-страницу github.com для авторизации
driver.maximize_window() # раскрываем на полное окно
sleep(1) # сон 1 сек перед выполнением следующего действия
login = driver.find_element_by_id('login_field') # находим элемент (id) для ввода логина
''' login.send_keys(' ... ') ''' # вводим логин
sleep(1) # сон 1 сек перед выполнением следующего действия
password = driver.find_element_by_id('password') # находим элементем (id) для ввода пароля
''' password.send_keys(' ... ') ''' # вводим пароль
driver.find_element_by_name('commit').click() # находим элемент (name) кнопки для авторизации и нажимаем
driver.implicitly_wait(5) # ожидаем, если будут задержки при авторизации
search = driver.find_element_by_name('q') # находим элемент (name) для ввода данных в поиск
search.send_keys('python') # вводим слово 'python'
driver.find_element_by_id('jump-to-results').click() # находим элемент (id) кнопки для запуска поиска и нажимаем
driver.maximize_window() # раскрываем на полное окно
driver.get_screenshot_as_file('github_python.png') # делаем скриншот текущей страницы
driver.implicitly_wait(5) # ожидаем, если будут задержки при создании скриншота
''' shutil.move('...default directory', '...second directory') ''' # меняем директорию расположения скриншота с дефолтной
sleep(1) # сон 1 сек перед выполнением следующего действия

''' email_user = '...login mail' ''' # создаем переменную с указанием логина для почты
''' email_password = '...password' ''' # создаем переменную с указнием пароля для почты
''' email_send = '...email send' ''' # создаем переменную с указанием почты с которой будет отправлено сообщение
''' email_cc = '...cc email' ''' # создаем переменную с указанием почты копии при отправке сообщения
adress = [email_send] + [email_cc] # создаем переменную объединяющую почту с которой будет осуществленна отправка и которая будет указана в копии
message = 'Screenshot Python topic from github' # создаем переменную указывающую текст сообщения
subject = 'Screenshot' # создаем переменную указывающую тему сообщения
''' file_location = '...second directory' ''' # создаем переменную указывающую актуальную директорию расположения скриншота

msg = MIMEMultipart() # создаем переменную работы с модулем MIMEMultipart для отправки сообщения
msg['From'] = email_user # создаем переменную отправки сообщения, указывая ранее созданную переменную с какой почты будет отправлено сообщения
msg['To'] = email_send # создаем переменную отправки сообщения, указывая ранее созданную переменную на какую почту будет отправлено сообщение
msg['CC'] = email_cc # создаем переменную отправки сообщения, указывая ранее созданную переменную копии почты на которую будет отправлено сообщение
msg['Subject'] = subject # создаем переменную отправки сообщения,указывая ранее созданную переменную темы письма
msg.attach(MIMEText(message, 'plain')) # вкладываем текст сообщения в письмо используя модуль MIMEText

filename = os.path.basename(file_location) # создаем переменную ссылающуюся на ранее созданную переменную с директорией файла со скриншотом
part = MIMEBase('application', 'octet-stream') # создаем переменную для работы с файловой системой используя модуль MIMEBase
part.set_payload(open(file_location, 'rb').read()) # открываем файл указывая ранее созданную переменную с директорией и читаем его
part.add_header('Content-Disposition', 'attachment;filename="github_python.png"') # добавляем заголовок для указания названия файла, который необходимо прикрепить в письмо
encoders.encode_base64(part) # указываем кодировщик для прикрепления файла при работе в 64-битной системе
msg.attach(part) # прикрепляем файл

text = msg.as_string() # создаем переменную с помощью которой прикрепляем сообщение в письмо
server = smtplib.SMTP('smtp.gmail.com', 587) # создаем переменную указывающую данные сервера SMTP
server.starttls() # стартуем сервер
server.login(email_user, email_password) # авторизовываемся на почте с помощью сервера
server.sendmail(email_user, adress, text) # указываем для сервера почту авторизации, почту для отправки и копии письма, текст сообщения
server.quit() # закрываем работу с сервером
