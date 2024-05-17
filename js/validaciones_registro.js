function validar() {
  
    const nameField = document.getElementById("nombre");
    const name2Field = document.getElementById("nombre2");
    const emailField = document.getElementById("emailregistro");
    const passField = document.getElementById("passwordreg");
  
    const nameRegex = /^[a-zA-Z]/;
    const name2Regex = /^[a-zA-Z]/;
    const emailRegex = /^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$/;
    const passRegex = /^\S{8,}$/;
    const showError = (message) => {
      alert(message);
    };
  
    if (!nameRegex.test(nameField.value)) {
      showError("Por favor ingresa un nombre válido");
      return;
    }

    if (!name2Regex.test(name2Field.value)) {
      showError("Por favor ingresa un apellido válido");
      return;
    }
  
    if (!emailRegex.test(emailField.value)) {
      showError("Por favor ingresa un correo válido");
      return;
    }
  
    if (!passRegex.test(passField.value)) {
      console.log(`Valor de la contraseña: ${passField.value}`);
      console.log(`Resultado de la prueba: ${passRegex.test(passField.value)}`);
      showError("Por favor ingresa una contraseña válida de 8 carácteres");
      return;
    }


    alert('¡Formulario enviado correctamente!')
      
  }
