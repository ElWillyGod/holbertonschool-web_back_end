export default function getStudentIdsSum(arrayObjet) {
  return arrayObjet.reduce((sum, obj) => sum + obj.id, 0);
}
