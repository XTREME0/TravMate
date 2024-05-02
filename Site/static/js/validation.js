// validation.js

document.getElementById('signupForm').addEventListener('submit', function(event) {
    var username = document.getElementById('username').value.trim();
    var email = document.getElementById('email').value.trim();
    var password = document.getElementById('password').value;
    var passwordConfirm = document.getElementById('password-confirm').value;

    var errors = {};

    // Username validation
    if (!username) {
        errors.username = 'Username is required.';
    } else if (!/^[a-zA-Z0-9@/./+/-/_]{1,150}$/.test(username)) {
        errors.username = 'Username can only contain letters, digits, and @/./+/-/_ and should be between 1 and 150 characters.';
    }

    // Email validation
    if (!email) {
        errors.email = 'Email is required.';
    } else if (!/\S+@\S+\.\S+/.test(email)) {
        errors.email = 'Invalid email address.';
    }

    // Password validation
    if (!password) {
        errors.password = 'Password is required.';
    } else if (password.length < 8) {
        errors.password = 'Password must be at least 8 characters long.';
    } else if (!/(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}/.test(password)) {
        errors.password = 'Password must contain at least one uppercase letter, one lowercase letter, and one number.';
    }

    // Password confirmation validation
    if (password !== passwordConfirm) {
        errors.passwordConfirm = 'Passwords do not match.';
    }

    // Display errors
    Object.keys(errors).forEach(function(field) {
        var errorMessage = errors[field];
        var errorElement = document.getElementById(field + '-error');
        if (errorElement) {
            errorElement.textContent = errorMessage;
        }
    });

    // Prevent form submission if there are errors
    if (Object.keys(errors).length > 0) {
        event.preventDefault();
    }
});
