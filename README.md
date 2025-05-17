# Instrucciones de uso

1. Armar la estructura del proyecto. (la misma se aclara en la siguiente sección)

2. Ejecutar `docker compose up --build -d` en la raíz.

   Esto levanta:
   - Un contenedor **"frontend"** en el **puerto 80**  
     Endpoint: `localhost:80/`
   - Un contenedor **"backend"** en el **puerto 8080**  
     Endpoints:
     - `localhost:8080/multiplicar` → espera 2 parámetros numéricos y devuelve un mensaje con el resultado  
     - `localhost:8080/logs` → muestra los logs guardados

3. Ingresar a `localhost:80` (frontend) y enviar dos números para una multiplicación.  
   Se debe mostrar el resultado en pantalla.  
   (funciona haciendo un fetch al backend: `http://localhost:8080/multiplicar?x=2&y=3`)

4. Modificaciones posibles:
   - Si modificamos los parámetros X e Y a otros valores, como `x=5&y=10`, se obtendrá otro resultado (50).
   - Si se hace un `curl` directo al backend y se omite uno de los dos parámetros o se pasa algo distinto a un número, se devuelve un error con código 400.

5. Debe devolver el múltiplo de estos números y guardarlo en logs en un volumen para persistencia con el siguiente formato:  
   `[timestamp] - mensaje`

6. También se puede ingresar al siguiente endpoint para ver los logs:  
   `http://localhost:8080/logs`

    6- Tambien se puede ingresar al siguiente endpoint para ver los logs
       http://localhost:8080/logs
