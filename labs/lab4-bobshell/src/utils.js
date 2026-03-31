// Utility functions for the application

/**
 * Format date to ISO string
 * @param {Date} date - Date object to format
 * @returns {string} Formatted date string
 */
function formatDate(date) {
    return date.toISOString();
}

/**
 * Validate email address
 * @param {string} email - Email to validate
 * @returns {boolean} True if valid
 */
function validateEmail(email) {
    // TODO: Improve email validation regex
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

/**
 * Generate random ID
 * @returns {string} Random ID
 */
function generateId() {
    // TODO: Use UUID library instead of Math.random
    return Math.random().toString(36).substr(2, 9);
}

/**
 * Sanitize user input
 * @param {string} input - User input to sanitize
 * @returns {string} Sanitized input
 */
function sanitizeInput(input) {
    // TODO: Implement proper XSS protection
    return input.trim();
}

/**
 * Calculate pagination
 * @param {number} page - Current page
 * @param {number} limit - Items per page
 * @returns {object} Pagination info
 */
function calculatePagination(page, limit) {
    // TODO: Add validation for negative numbers
    const offset = (page - 1) * limit;
    return { offset, limit };
}

// TODO: Add error handling utilities
// TODO: Implement retry mechanism for failed operations
// TODO: Add caching utilities

module.exports = {
    formatDate,
    validateEmail,
    generateId,
    sanitizeInput,
    calculatePagination
};

// Made with Bob
