/**
 * js/contact.js
 * Client-side validation and form submission handler.
 * Note: This currently simulates a backend submission for UI purposes.
 */

document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');
    const successMessage = document.getElementById('form-success-message');

    if (!contactForm) return;

    // Helper to toggle error states
    const setError = (input, messageId, isValid) => {
        const errorEl = document.getElementById(messageId);
        if (isValid) {
            input.setAttribute('aria-invalid', 'false');
            input.removeAttribute('aria-describedby');
            if (errorEl) errorEl.classList.remove('active');
        } else {
            input.setAttribute('aria-invalid', 'true');
            if (errorEl) {
                input.setAttribute('aria-describedby', messageId);
                errorEl.classList.add('active');
            }
        }
    };

    // Validation patterns
    const patterns = {
        name: /.+/,
        email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        phone: /^[\d\s\+\-\(\)]{7,}$/ // simple check supporting formats like 0712 543781
    };

    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        let formIsValid = true;

        // 1. Validate Full Name
        const nameInput = document.getElementById('fullName');
        const isNameValid = nameInput.value.trim() !== '';
        setError(nameInput, 'fullName-error', isNameValid);
        if (!isNameValid) formIsValid = false;

        // 2. Validate Phone
        const phoneInput = document.getElementById('phoneNumber');
        const isPhoneValid = patterns.phone.test(phoneInput.value.trim());
        setError(phoneInput, 'phoneNumber-error', isPhoneValid);
        if (!isPhoneValid) formIsValid = false;

        // 3. Validate Email (Optional, but must be valid if filled)
        const emailInput = document.getElementById('emailAddress');
        let isEmailValid = true;
        if (emailInput.value.trim() !== '') {
            isEmailValid = patterns.email.test(emailInput.value.trim());
        }
        setError(emailInput, 'emailAddress-error', isEmailValid);
        if (!isEmailValid) formIsValid = false;

        // 4. Validate Message
        const messageInput = document.getElementById('message');
        const isMessageValid = messageInput.value.trim() !== '';
        setError(messageInput, 'message-error', isMessageValid);
        if (!isMessageValid) formIsValid = false;

        if (formIsValid) {
            // FRONT-END ONLY SIMULATION: Replace form with success message temporarily
            // TODO: In a real implementation, send data via fetch() to a backend here.
            contactForm.style.display = 'none';
            successMessage.style.display = 'block';

            // Reset form in the background
            contactForm.reset();

            // Screen reader optimization: move focus to success message
            successMessage.setAttribute('tabindex', '-1');
            successMessage.focus();
        }
    });

    // Optional: Real-time validation clear on input
    const inputs = contactForm.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.addEventListener('input', () => {
            if (input.getAttribute('aria-invalid') === 'true') {
                setError(input, `${input.id}-error`, true);
            }
        });
    });
});
