function togglePassword() {
        var passwordInput = document.getElementsByName("password")[0];
        if (passwordInput.type === "password") {
            passwordInput.type = "text";
        } else {
            passwordInput.type = "password";
        }
    }