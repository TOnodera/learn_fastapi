import http from '@/Domain/Utility/http';
import UserCreate from './UserCreate';

class User {
  async create(user) {
    const creator = new UserCreate(user);
    await creator.create();
  }
  async update() {}
  async all() {
    const response = await http.get('/users');
    return response.data;
  }
}
export default User;
