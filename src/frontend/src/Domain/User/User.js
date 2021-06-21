import http from '@/Domain/Utility/http';

class User {
  async create(user) {
    const response = await http.post('/users/create', {
      name: user.name,
      email: user.email,
      memo: user.memo,
      image: user.image,
    });
    return response.data;
  }
  async update(user) {
    const response = await http.put(`/users/${user.id}`, {
      name: user.name,
      email: user.email,
      memo: user.memo,
      image: user.image,
    });
    return response.data;
  }
  async all() {
    const response = await http.get('/users');
    return response.data;
  }
}
export default User;
