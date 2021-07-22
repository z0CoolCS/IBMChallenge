# IBMChallenge
Este es un proyecto que busca resolver un reto haciendo uso de las tecnologías de IBM.  
Las tecnologías a usar son:  
- IBM Watson Assistant  
- IBM Watson Discovery 

Para la comunicación entre ambas tecnologías se hizo uso de **ngrok**, un tunel de dirección pública que permite tener una dirección de un servidor local. Es decir, se pueda consumir los servicios que esten corriendo en mi máquina local desde cualquier computadora en otra red.  

Usted puede descarga ngrok desde la siguiente ruta: https://ngrok.com/download  

Para correr el aplicativo siga los siguientes pasos
1. Inicie el servidor en flask.
    python server.py
2. Ejecute ngrok  
    ./ngrok http 8000
3. Pruebe el chatbot  

Algunas consideraciones:  
- Ngrok en su versión gratuita no ofrece dirección únicas. Eso quiere que al volver a ejecutar ngrok, este generara una nueva dirección la cuál debe ser actualizada en Watson Assistant.  
- Dentro del servidor flask esta definido que el puerto de comunicación es el 8000. En caso usted desea cambiarlo tambien debe fijar el mismo valor al ejecutar ngrok. 

