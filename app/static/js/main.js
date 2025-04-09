// Utility function to display messages
function showMessage(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.role = 'alert';

    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    `;

    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);

    // Auto dismiss after 5 seconds
    setTimeout(() => {
        alertDiv.classList.remove('show');
        setTimeout(() => alertDiv.remove(), 150);
    }, 5000);
}

// Add smooth scrolling to answers
document.addEventListener('DOMContentLoaded', function () {
    // Check if URL has an answer fragment identifier
    if (window.location.hash) {
        const answerId = window.location.hash.substring(1);
        const element = document.getElementById(answerId);

        if (element) {
            // Smooth scroll to answer
            element.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });

            // Highlight the answer briefly
            element.classList.add('bg-light');
            setTimeout(() => {
                element.classList.remove('bg-light');
            }, 2000);
        }
    }
});