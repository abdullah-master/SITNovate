document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('certificateForm');
    const digitCodeInput = document.getElementById('digitCode');

    // Validate 12-digit code input
    digitCodeInput.addEventListener('input', (e) => {
        e.target.value = e.target.value.replace(/[^0-9]/g, '').slice(0, 12);
    });

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const formData = {
            certificateName: document.getElementById('certificateName').value,
            certifierName: document.getElementById('certifierName').value,
            digitCode: digitCodeInput.value
        };

        // Here you would typically send this data to your server
        console.log('Form submitted:', formData);
        
        // For demo purposes, show success message
        alert('Certificate information submitted successfully!');
        form.reset();
    });
});
