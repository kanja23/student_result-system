const express = require('express');
const app = express();
const ejs = require('ejs');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', (req, res) => {
	res.render('index', { pageTitle: 'Home' });
});
