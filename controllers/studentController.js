const Student = require('../models/studentModel');

exports.getAllStudents = (req, res) => {
	Student.find({}, (err, students) => {
		if (err) {
			console.error(err);
			return res.status(500).json({ error: 'Internal server error' });
		}
		return res.json(students);
	});
};
