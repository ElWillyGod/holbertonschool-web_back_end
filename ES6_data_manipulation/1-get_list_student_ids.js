export default function getListStudentIds(arrayObjet) {
  if (!Array.isArray(arrayObjet)) {
    return [];
  }

  return arrayObjet.map((obj) => obj.id);
}
