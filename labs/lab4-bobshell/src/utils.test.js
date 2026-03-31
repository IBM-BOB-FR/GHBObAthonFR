// Test file for utils.js
const {
    formatDate,
    validateEmail,
    generateId,
    sanitizeInput,
    calculatePagination
} = require('./utils');

describe('Utils Tests', () => {
    describe('formatDate', () => {
        test('should format date to ISO string', () => {
            const date = new Date('2024-01-01');
            const result = formatDate(date);
            expect(result).toContain('2024-01-01');
        });
    });

    describe('validateEmail', () => {
        test('should validate correct email', () => {
            expect(validateEmail('test@example.com')).toBe(true);
        });

        test('should reject invalid email', () => {
            expect(validateEmail('invalid-email')).toBe(false);
        });
    });

    describe('generateId', () => {
        test('should generate unique IDs', () => {
            const id1 = generateId();
            const id2 = generateId();
            expect(id1).not.toBe(id2);
        });
    });

    describe('sanitizeInput', () => {
        test('should trim whitespace', () => {
            expect(sanitizeInput('  test  ')).toBe('test');
        });
    });

    describe('calculatePagination', () => {
        test('should calculate correct offset', () => {
            const result = calculatePagination(2, 10);
            expect(result.offset).toBe(10);
            expect(result.limit).toBe(10);
        });
    });
});

// Made with Bob
