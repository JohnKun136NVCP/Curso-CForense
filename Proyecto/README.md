<p>
<img src="https://play-lh.googleusercontent.com/PHjV5b_9bMCgYLn5Cz2Cy2sI7qMZ6iEtP-Mb1tSYzKUI-Mq1Sp0_f5evhmWgAaT81Q" width="70" height="70" align="right"/>
</p>

# Proyecto prebecario. 💻🛡🔐🔎
## Introducción. 📝📄🖌📸
<p align = "justify">
Es importante aprender a aplicar los conocimientos adquiridos, ya  será de gran utilidad en algún momento y también nos ayudará a estar prevenidos para un ataque o en este caso lo que se tratará este proyecto es más ponerse uno a prueba. 

Situación, imaginemos que en algún momento tiene que analizar en una computadora, hace los procedimientos correspondientes y además al momento de copiar el disco se da cuenta que solo hay un archivo llamado *doki_doki.jpg* y lo que primero que uno pensaría es ignorarlo. Sin embargo, le encargaron hacer una análisis exhaustivo de cada archivo y programa. Pero lo único que tiene es una computadora con Linux y se acordó de sus clases de Cómputo Forense, por lo cual no se dejó engañar por ser una simple imagen *las apariencias engañan*. Lo que aplicará es el concepto de **Esteganografía** para obtener información de esa imagen. 
</p>

## Materiales. 🛠⛏⚙️
1. Sistema Operativo Linux (Cualquier distribución debian).
2. Herramienta [streghide](http://steghide.sourceforge.net/documentation/manpage_es.php)
3. Lenguaje de programación, puede ser (C,C++,Java,Bash,Python). El último de preferencia.
4. GitHub.

## Instrucciones. 🧩💾✉️📇
1. En la imagen proporcionada se ha ocultado un archivo de texto 📄, para obtenerlo debeŕas instalar una herramienta de esteganografía llamada steghide, una vez que cuentes con dicho programa deberás usar el siguiente comando:


    steghide extract -sf doki_doki.jpeg


Posteriormente ingresa el salvoconducto solicitado: **proteco**.

Listo! ✔️ ya tienes tu archivo oculto. 😎


2. Una vez que obtengas el archivo de texto plano te podrás dar cuenta que este se encuentra cifrado 😨 , por ello deberás hacer lo siguiente:

 * Haz un programa que descifre el mensaje de binario a ASCII (ver tabla). 
 * Pasa el mensaje obtenido a base64.
 * Finalmente convierte el mensaje de base64 a lenguaje natural. Es decir, decodificar el lenguaje Base64 a lenguaje humano.

3. Una vez que descifres el mensaje, sube tu programa y el resultado en un archivo txt a este repositorio.

## Para punto extra sobre calificación.
 * Haga un script en bash que permita leer la imagen e implementar el código que utilices para descifrar el archivo, este tiene que dar como salida el mensaje oculto junto con el archivo. 
