export default function getStudentsByLocation(arrayObjet, city) {
  return arrayObjet.filter((obj) => obj.location === city);
}
