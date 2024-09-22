const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const students = data.split('\n').slice(1);
      const numberOfStudents = students.length;
      console.log(`Number of students: ${numberOfStudents}`);
      const fields = {};
      students.forEach((student) => {
        const [firstname, lastname, age, field] = student.split(',');
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });
      Object.keys(fields).forEach((field) => {
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      });
    })
    .catch((err) => {
      throw new Error(`Error reading file: ${err.message}`);
    });
}

module.exports = countStudents;