function validar() {
    const nameField = document.getElementById("nombre");
    const name2Field = document.getElementById("nombre2");
    const emailField = document.getElementById("email");
    const passField = document.getElementById("password");
    const pass2Field = document.getElementById("password2");
  
    const nameRegex = /^[a-zA-Z]/;
    const name2Regex = /^[a-zA-Z]/;
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%]+.com/;
    const passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
    const pass2Regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;

    const showError = (message) => {
      alert(message);
    };
  
    if (!nameRegex.test(nameField.value)) {
      showError("Por favor ingresa un nombre válido");
      return;
    }

    if (!name2Regex.test(name2Field.value)) {
      showError("Por favor ingresa un nombre válido");
      return;
    }
  
    if (!emailRegex.test(emailField.value)) {
      showError("Por favor ingresa un correo válido");
      return;
    }
  
    if (!passRegex.test(passField.value)) {
      showError("Por favor ingresa una contraseña válida");
      return;
    }

    if (!pass2Regex.test(pass2Field.value)) {
      showError("Por favor ingresa una contraseña válida");
      return;
    }

    alert('¡Formulario enviado correctamente!')
      
  }
  