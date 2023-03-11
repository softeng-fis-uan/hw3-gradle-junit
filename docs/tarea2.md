# Agregar un controlador

Para agregar una nueva página a su aplicación siga los siguientes pasos:

1. **Agregue un nuevo controlador a la aplicación**. Cree una clase controlador `HelloController` dentro de la carpeta `ejemplo/src/main/java`, en el paquete `co.edu.uan.sofeng.ejemplo` con el siguiente código:

   ```java
   package co.edu.uan.sofeng.ejemplo;

   import org.springframework.web.bind.annotation.GetMapping; 
   import org.springframework.web.bind.annotation.RestController; 
   
   @RestController 
   public class HelloController {
      @GetMapping("/")
      public String index() {
         return "Welcome to Spring Boot!";
      }
   } 
   ```

2. **Ejecute la aplicación**. Use el siguiente comando desde la carpeta `ejemplo`:

   ```bash
   ./gradlew bootRun
   ```

   Debería poder abrir la página web desde su navegador en la dirección `http://localhost:8080`

3. **Agregue sus pruebas unitarias**. Cree una clase de pruebas dentro de la carpeta `ejemplo/src/test/java`, en el paquete `co.edu.uan.sofeng.ejemplo` con el siguiente código:

   ```java
   package co.edu.uan.sofeng.ejemplo;

   import static org.hamcrest.Matchers.equalTo;
   import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
   import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

   import org.junit.jupiter.api.Test;

   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
   import org.springframework.boot.test.context.SpringBootTest;
   import org.springframework.http.MediaType;
   import org.springframework.test.web.servlet.MockMvc;
   import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;

   @SpringBootTest
   @AutoConfigureMockMvc
   public class HelloControllerTests {

      @Autowired
      private MockMvc mvc;

      @Test
      public void getHello() throws Exception {
            mvc.perform(MockMvcRequestBuilders.get("/").accept(MediaType.APPLICATION_JSON))
                    .andExpect(status().isOk())
                    .andExpect(content().string(equalTo("Welcome to Spring Boot!")));
      }
   }
   ```

4. **Ejecute las pruebas unitarias**. Para esto use el siguiente comando desde la carpeta `ejemplo`:

   ```bash
   ./gradlew test
   ```

   Verá un resultado similar al siguiente:

   ```bash
   ...
   BUILD SUCCESSFUL in 2s
   4 actionable tasks: 2 executed, 2 up-to-date
   ```

   Y puede encontrar el resultado de sus pruebas en la carpeta `ejemplo/build/reports/tests/test`

5. Puede agregar también pruebas de integración donde no se usen mocks creando una clase de prueba como la siguiente:

   ```java
   package co.edu.uan.sofeng.ejemplo;

   import org.junit.jupiter.api.Test;

   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.boot.test.context.SpringBootTest;
   import org.springframework.boot.test.web.client.TestRestTemplate;
   import org.springframework.http.ResponseEntity;

   import static org.assertj.core.api.Assertions.assertThat;

   @SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
   public class HelloControllerIntegrationTests {

      @Autowired
      private TestRestTemplate template;

      @Test
      public void getHello() throws Exception {
         ResponseEntity<String> response = template.getForEntity("/", String.class);
         assertThat(response.getBody()).isEqualTo("Welcome to Spring Boot!");
      }
   }
   ```

## Referencias

- [Building an Application with Spring Boot](https://spring.io/guides/gs/spring-boot/)
