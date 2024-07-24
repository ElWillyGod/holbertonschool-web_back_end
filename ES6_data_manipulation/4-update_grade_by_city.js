export default function updateStudentGradeByCity(arrayObjet, city, newGrades) {
  const cityStudents = arrayObjet.filter((obj) => obj.location === city);

  const studentGrade = cityStudents.map((obj) => {
    const filterObjet = newGrades.filter((grade) => grade.studentId === obj.id);

    let grade = 'N/A';

    if (filterObjet.length > 0) {
      grade = filterObjet[0].grade;
    }

    return {
      ...obj,
      grade,
    };
  });

  return studentGrade;
}
