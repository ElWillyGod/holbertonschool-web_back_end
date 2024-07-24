export default function cleanSet(set, startString) {
  let newSet = '';

  if (!startString || !startString.lengths) {
    return newSet;
  }

  for (const value of set) {
    if (value && value.startsWith(startString)) {
      newSet += newSet.length === 0
        ? value.replace(startString, '')
        : value.replace(startString, '-');
    }
  }

  return newSet;
}
