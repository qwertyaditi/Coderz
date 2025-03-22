// index.js
const express = require('express');
const app = express();

// A simple test route:
app.get('/', (req, res) => {
  res.send('Hello from Express!');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
