const firebaseConfig = {
    apiKey: "AIzaSyAArL3-mJLlztwftNDjqz_hbJsE-Yo2g6g",
    authDomain: "smartkyc-622d4.firebaseapp.com",
    projectId: "smartkyc-622d4",
    storageBucket: "smartkyc-622d4.appspot.com",
    messagingSenderId: "436952492216",
    appId: "1:436952492216:web:d9b456119f54e31f52ec4d"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);

  const auth  = firebase.auth()
  const database = firebase.database()
  
  // set regrister func
  function register(){
    fname = document.getElementById('fname').value
    email = document.getElementById('email').value 
    password = document.getElementById('password').value
    repassword = ducument.getElementById('repassword').value

    if(validate_email(email) == false || validate_password(password) == false){
        alert('Email or Password is Out of LIne !!')
        return
    }
    if (validate_field(fname) == false){
        alert('Field is Out of Line !!')
        return
    }

    // Auth
    auth.createUser(email,password)
    .then(function(){
        // declare user variable
        var user = auth.currUser
        // add user to firebase 
        var databse_ref = datbase.ref()

        var user_data =  {
            email : email,
            fname : fname,
            password : password,
            repassword : repassword,
            last_login : Date.now()
        }
        databse_ref.child('user/' + user.uid).set(user_data) 
        alert('User Created !')
    })
    .catch(function(error) {
        var error_code = error.code
        var errorr_message = error.message

        alert(error_message)
    })

  function validate_email(email){
    exp = /^[^@]+@\w+(\.\w+)+\w$/
    if (exp.test(email) == true){
        return true
    }else{
        return false
    }
  }

  function validate_password(password){
    if (password < 6){
        return false
    }else{
        return true
    }
  }

  function validate_field(field) {
    if (field == null){
        return false
    }
    if (field.length <= 0){
        return false
    }else{
        return true
    }
  }
}