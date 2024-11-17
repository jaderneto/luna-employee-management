// form.js
function validateForm(event) {
    event.preventDefault();

    const errorMessages = document.querySelectorAll('.error-message');
    errorMessages.forEach(msg => msg.remove());

    let isValid = true;

    const fields = ['first_name', 'last_name', 'full_name', 'birth_date', 'email', 'hire_date'];
    fields.forEach(field => {
        const input = document.querySelector(`input[name="${field}"]`);
        if (input.value.trim() === '') {
            isValid = false;
            displayError(input, `${field.replace('_', ' ')} is required.`);
        }
    });

    if (isValid) {
        submitForm();
    }
}

document.querySelector('form').addEventListener('submit', validateForm);
