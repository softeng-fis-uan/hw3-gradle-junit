# Modificar el controlador

En esta sección usted agregará un nuevo endpoint o URL a su aplicación, siguendo los mismos pasos del punto anterior.

1. Agregue un nuevo método al controlador llamado `sayHello` mapeado a un Get en la direccion `say_hello`. Este metodo debe retornar el texto `Hello World`. Pruebe su aplicacion, los dos metodos deberian funcionar.

2. Agregue una prueba unitaria `sayHello` para el metodo que acaba de crear.

3. Modifique el metodo anterior para que reciba como parametro el nombre de la persona `String name`. Agregue la anotacion `RequestParam` para indicar que este parametro se recibira en la URL, por ejemplo:

   ```java
   String sayHello(@RequestParam(defaultValue = "World") String name) { ... }
   ```

   El metodo debe retornar ahora el texto `Hello name` donde name debe ser el valor recibido en el parametro name. Si el parametro es vacio o nulo, debe retornar el texto original `Hello World`. Pruebe su aplicacion.

4. Agrege ua prueba unitaria llamada `sayHelloName` donde se use un valor para el parametro name.

## Referencias

- [Building an Application with Spring Boot](https://spring.io/guides/gs/spring-boot/)
- [Spring @RequestParam Annotation](https://www.baeldung.com/spring-request-param)
