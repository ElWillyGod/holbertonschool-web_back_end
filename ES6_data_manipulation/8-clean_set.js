export default function cleanSet(set, startString) {
  if (startString.length === 0) {
    return '';
  }

  let newSet = '';

  for (const value of set) {
    if (value.startsWith(startString)) {
      newSet += newSet.length === 0
        ? value.replace(startString, '')
        : value.replace(startString, '-');
    }
  }

  return newSet;
}
