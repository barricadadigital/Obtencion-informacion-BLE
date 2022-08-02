# Obtencion-informacion-BLE
La idea de crear esta herramienta surge de una investigación sobre la reutilización de claves de emparejamiento de los dispositivos Bluetooth Low Energy (BLE). Estas claves se llaman Long Term Key (LTK) y son utilizadas por los dispositivos BLE para el cifrado en las comunicaciones. El objetivo de esta PoC es simplemente crear unos scripts basados en cliente-servidor, que permitirían obtener información de dispositivos emparejados para posteriormente, en caso de obtener la LTK poder crackearlos.
Ver otra herramienta creada durante esta investigación en https://github.com/Casta085/Bluetooth-Low-Energy-Impersonation 

# Modelo de amenaza
Asumimos que el atacante tiene la posibilidad de acceder durante un corto periodo de tiempo a las instalaciones de una oficina de la empresa víctima, a partir de ahora “Víctima”. El atacante no volverá a tener acceso físico a las instalaciones, pero tendrá acceso total con privilegios “SYSTEM” a uno o varios de los ordenadores de dicha oficina.
Además, se presupone que los trabajadores de dicha oficina utilizan teclados inalámbricos con conexiones BLE para su uso en el día a día. Dichos teclados utilizan conexiones seguras y cifradas, con algoritmos fuertes, por lo que no es posible romper dicho cifrado mediante ataques específicos.
Por último, se da por hecho que es posible conectar el dispositivo a una red de invitados de la empresa. Aunque podría realizarse este mismo ataque sin dicha conexión de formas más elaboradas.

#Hardware y Software requerido para el ataque
Para la realización de esta PoC se ha utilizado:
• Raspberry.
• MicroBit v1.5 con placa NRF.
• Script de envío de información script.py
• Script de obtención de información server.py

#Como usarlo
Simplemente se debe colocar una Raspberry con una placa Microbit y BtleJack instalado en el dispositivo, en el lugar dónde se quiere obtener la información de conexiones BLE.

Por otro lado debe iniciarse el servidor en un entorno con conexión al exterior, y deben modificarse las partes del código que quedan marcadas dentro de cada script.
