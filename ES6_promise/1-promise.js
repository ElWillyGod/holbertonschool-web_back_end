export default function getFullResponseFromAPI(sera) {
  return new Promise((resolve, error) => {
    if (sera) {
      resolve({
        status: 200,
        body: 'Success',
      });
    } else {
      error(new Error('The fake API is not working currently'));
    }
  });
}
