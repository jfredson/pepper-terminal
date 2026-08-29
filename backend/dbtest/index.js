const express = require('express');
 const { Pool } = require('pg');

 const app = express();
 const port = process.env.PORT || 3000;

 // Create a PostgreSQL connection pool using DATABASE_URL from .env
 const pool = new Pool({
   connectionString: process.env.DATABASE_URL,
 });

 app.use(express.static('public'));

 app.get('*', (req, res) => {
   res.sendFile(path.join(__dirname, 'public', 'index.html'));
 });

 app.get('/dbtest', async (req, res) => {
   try {
     const result = await pool.query('SELECT NOW()');
     res.json({ success: true, time: result.rows[0].now });
   } catch (err) {
     console.error('Database query error:', err);
     res.status(500).json({ success: false, error: err.message });
   }
 });

 app.listen(port, () => {
   console.log(`Server listening on port ${port}`);
 });
