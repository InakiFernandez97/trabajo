function validarLogin() {
    // Obtener los valores de los campos de email y password
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
  
    // Verificar las credenciales (esto es solo un ejemplo, debes reemplazarlo con tu lógica real)
    if (email === 'test@duoc.cl' && password === 'test1') {
      alert('Ingreso correcto');
      return true; // Permitir que el formulario se envíe
    } else {
      alert('Credenciales incorrectas');
      return false; // Evitar que el formulario se envíe
    }
  }