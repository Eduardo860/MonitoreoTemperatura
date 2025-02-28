# MonitoreoTemperatura
Este proyecto implementa un sistema de monitoreo de temperatura basado en IoT utilizando una Raspberry Pi Pico W y un sensor LM35. La temperatura se mide y se envía a ThingSpeak, donde se almacena y visualiza en tiempo real. Además, se calcula el promedio de las últimas 10 mediciones y se generan alertas automáticas cuando la temperatura supera un umbral de 35°C.

Para desarrollar este sistema, se utiliza una Raspberry Pi Pico W, un sensor LM35 y una conexión a internet mediante Wi-Fi. El sensor LM35 mide la temperatura y envía una señal analógica, la cual es leída por la Pico W a través del pin GP26 (ADC0). Luego, el valor se convierte a grados Celsius y se transmite a ThingSpeak, donde los datos quedan almacenados y se pueden graficar para su monitoreo en la nube.

Para llevar a cabo este proyecto, se requieren los siguientes materiales: una Raspberry Pi Pico W, un sensor LM35, cables de conexión y una cuenta en ThingSpeak para visualizar los datos. También se necesita Thonny, un entorno de desarrollo que permite programar en MicroPython y ejecutar el código en la Raspberry Pi Pico W.

La conexión del sensor LM35 con la Raspberry Pi Pico W se realiza de la siguiente manera: el VCC del LM35 se conecta a VBUS (5V) de la Pico W, el GND del sensor se conecta a GND, y el VOUT del LM35 se conecta a GP26 (ADC0). Esto permite que la Raspberry reciba la señal de temperatura y la procese correctamente.

Para instalar y ejecutar el proyecto, primero se debe configurar la Raspberry Pi Pico W instalando MicroPython y conectándola a la computadora mediante USB. Luego, se crea un canal en ThingSpeak y se activan los Fields necesarios:

Field 1: Para almacenar y visualizar la temperatura.
Field 2: Para guardar el promedio de temperatura de las últimas 10 mediciones.
Después, se clona el repositorio de GitHub en la Raspberry Pi Pico W y se edita el archivo config.py con los datos de conexión Wi-Fi y la API Key de ThingSpeak.

Una vez configurado, el código principal (main.py) se ejecuta y comienza a enviar datos a ThingSpeak automáticamente cada 180 segundos. Además, cada 30 minutos, el código calcula el promedio de las últimas 10 mediciones y lo almacena en Field 2. En ThingSpeak, se pueden configurar gráficos para visualizar la temperatura en tiempo real y su promedio, lo que facilita el monitoreo remoto del sistema.

El código del proyecto está disponible en GitHub y contiene los archivos principales necesarios para su funcionamiento. En el repositorio se encuentran los siguientes archivos:

main.py → Código principal que lee la temperatura y la envía a ThingSpeak.
config.py → Archivo donde se configuran las credenciales de Wi-Fi y la API Key de ThingSpeak.
promedio.m → Código en MATLAB que calcula el promedio de las últimas 10 mediciones y lo almacena en ThingSpeak.
alerta.m → Código en MATLAB que envía una alerta si la temperatura supera los 35°C.
README.md → Instrucciones detalladas del proyecto.
