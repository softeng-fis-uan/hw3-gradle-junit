# Crear un contenedor usando Docker

En esta sección usted creará un contenedor para la aplicacioó usando Docker. Antes de comenzar asegurese que Docker Desktop este corriendo en su computador.

1. **Cree el archivo `Dockerfile` para su aplicación**. Dentro de la carpeta ejemplo cree un archivo `Dockerfile` con el siguiente contenido:

   ```docker
   FROM eclipse-temurin:11
   COPY build/libs/ejemplo-0.0.1-SNAPSHOT.jar .
   ENTRYPOINT ["java","-jar","/ejemplo-0.0.1-SNAPSHOT.jar"]
   EXPOSE 8080
   ```

2. Construya la imagen del contenedor docker usando el siguiente comando:

   ```bash
   docker build --tag=ejemplo:latest .
   ```

   Vera un resutado similar al siguiente:

   ```bash
    [+] Building 12.6s (7/7) FINISHED                                                                                             
    => [internal] load build definition from Dockerfile                                                                     0.1s
    => => transferring dockerfile: 179B                                                                                     0.0s
    => [internal] load .dockerignore                                                                                        0.0s
    => => transferring context: 2B                                                                                          0.0s
    => [internal] load metadata for docker.io/library/eclipse-temurin:17                                                    1.7s
    => [internal] load build context                                                                                        0.7s
    => => transferring context: 42.18MB                                                                                     0.6s
    => [1/2] FROM docker.io/library/openjdk:17-jdk-alpine@sha256:4b6abae565492dbe9e7a894137c966a7485154238902f2f25e9dbd97  10.1s
    => => resolve docker.io/library/openjdk:17-jdk-alpine@sha256:4b6abae565492dbe9e7a894137c966a7485154238902f2f25e9dbd978  0.0s
    => => sha256:5843afab387455b37944e709ee8c78d7520df80f8d01cf7f861aae63beeddb6b 2.81MB / 2.81MB                           0.3s
    => => sha256:53c9466125e464fed5626bde7b7a0f91aab09905f0a07e9ad4e930ae72e0fc63 928.44kB / 928.44kB                       0.7s
    => => sha256:d8d715783b80cab158f5bf9726bcada5265c1624b64ca2bb46f42f94998d4662 186.80MB / 186.80MB                       7.7s
    => => sha256:4b6abae565492dbe9e7a894137c966a7485154238902f2f25e9dbd9784383d81 319B / 319B                               0.0s
    => => sha256:a996cdcc040704ec6badaf5fecf1e144c096e00231a29188596c784bcf858d05 951B / 951B                               0.0s
    => => sha256:264c9bdce361556ba6e685e401662648358980c01151c3d977f0fdf77f7c26ab 3.48kB / 3.48kB                           0.0s
    => => extracting sha256:5843afab387455b37944e709ee8c78d7520df80f8d01cf7f861aae63beeddb6b                                0.2s
    => => extracting sha256:53c9466125e464fed5626bde7b7a0f91aab09905f0a07e9ad4e930ae72e0fc63                                0.1s
    => => extracting sha256:d8d715783b80cab158f5bf9726bcada5265c1624b64ca2bb46f42f94998d4662                                2.1s
    => [2/2] COPY build/libs/ejemplo-0.0.1-SNAPSHOT.jar .                                                                   0.4s
    => exporting to image                                                                                                   0.2s
    => => exporting layers                                                                                                  0.2s
    => => writing image sha256:1f0862192fcd30a557914c0b55f2293b79c081fa758ea502fb0bf85dfa1ec2ee                             0.0s
    => => naming to docker.io/library/ejemplo:latest                                                                        0.0s
   ```

3. **Iniciar el contenedor de la aplicación**. Inicie la aplicación usando el comando `docker run` y especificando el nombre de la imagen que acaba de crear:

   ```bash
   docker run -dp 8080:8080 ejemplo
   ```

   Despues de unos segundos podra ingresar a `http://localhost:8080` y ver su aplicación funcionando.

4. Otros comandos que puede usar con docker.

   - Para ver una lista de los contenedores que estan corriendo puede usar el comando `docker ps`.

   - Puede detener un contenedor usando el comando `docker stop <container_name>`, por ejemplo:

     ```bash
     docker stop ejemplo
     ```

## Referencias

- [Dockerizing a Spring Boot Application](https://www.baeldung.com/dockerizing-spring-boot-application)
- [Docker: Get started](https://docs.docker.com/get-started/)
