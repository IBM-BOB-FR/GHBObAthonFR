// Main application file
const express = require('express');
const userRoutes = require('./routes/users');
const productRoutes = require('./routes/products');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// TODO: Add authentication middleware
// TODO: Implement rate limiting for API endpoints

// Routes
app.use('/api/users', userRoutes);
app.use('/api/products', productRoutes);

// TODO: Add error handling middleware
// TODO: Implement logging system

// Health check endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'OK', timestamp: new Date() });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// TODO: Add graceful shutdown handling
// TODO: Implement database connection pooling

module.exports = app;

// Made with Bob
