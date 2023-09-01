const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/student-results-db', {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

mongoose.connection.on('error', (err) => {
	console.error(`MongoDB connection error: ${err}`);
});
