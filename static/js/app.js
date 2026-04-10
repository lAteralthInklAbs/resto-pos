/**
 * RestoPoS - Restaurant Point of Sale
 * Client-side JavaScript for real-time order calculation and form validation
 */

document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Form validation feedback
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
});

/**
 * Calculate running total for order form
 * Called from order.html inline script
 */
function calculateOrderTotal() {
    const qtyInputs = document.querySelectorAll('.qty-input');
    let total = 0;

    qtyInputs.forEach(input => {
        const qty = parseInt(input.value) || 0;
        const price = parseInt(input.dataset.price) || 0;
        total += qty * price;
    });

    return total;
}

/**
 * Format currency as Indian Rupees
 */
function formatCurrency(amount) {
    return `Rs. ${amount.toLocaleString('en-IN')}`;
}

/**
 * Validate order has at least one item
 */
function validateOrder() {
    const qtyInputs = document.querySelectorAll('.qty-input');
    let hasItems = false;

    qtyInputs.forEach(input => {
        if (parseInt(input.value) > 0) {
            hasItems = true;
        }
    });

    if (!hasItems) {
        alert('Please select at least one item to place an order.');
        return false;
    }

    return true;
}
