import http from 'k6/http';

const params = {
  headers: {
    'Content-Type': 'application/json',
  },
};

const login_payload = JSON.stringify({
  username: 'foo',
  password:'bar'
});

export default function () {
  http.post('http://api-server:80/login', login_payload, params);
  http.get('http://api-server:80/hello_world');
  for (let item_id = 1; item_id <= 10; item_id++) {
    http.get(`http://api-server:80/item?item_id=${item_id}`, {
      tags: { name: 'http://api-server:80/item' },
    });
  }
}

export function handleSummary(data) {
  return {
    '/tmp/k6/summary.json': JSON.stringify(data),
  };
}
