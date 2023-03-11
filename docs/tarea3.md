# Modificar el controlador

En esta sección usted agregará un nuevo endpoint o URL a su aplicación, siguendo los mismos pasos del punto anterior.

1. Agregue un nuevo método al controlador llamado `sayHello` mapeado a un Get en la dirección `say_hello`. Este método debe retornar el texto `Hello World`. Pruebe su aplicación, los dos métodos (`/` y `/say_hello`)deberían funcionar.

2. Agregue una prueba unitaria `sayHello` para el método que acaba de crear.

3. Modifique el método anterior para que reciba como parámetro el nombre de la persona `String name`. Agregue la anotación `RequestParam` para indicar que este parámetro se recibira en la URL, por ejemplo:

   ```java
   String sayHello(@RequestParam(defaultValue = "World") String name) { ... }
   ```

   El método debe retornar ahora el texto `Hello name` donde `name` debe ser el valor recibido en el parámetro name. Si el parámetro es vacío o nulo, debe retornar el texto original `Hello World`. Pruebe su aplicación.

4. Agrege ua prueba unitaria llamada `sayHelloName` donde se use un valor para el parámetro name.

## Referencias

- [Building an Application with Spring Boot](https://spring.io/guides/gs/spring-boot/)
- [Spring @RequestParam Annotation](https://www.baeldung.com/spring-request-param)
