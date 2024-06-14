function validarLogin() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
  
    if (email === 'test@duoc.cl' && password === 'testing1') {
      alert('Ingreso correcto');
      return true; 
    } else {
      alert('Credenciales incorrectas');
      return false;
    }
  }