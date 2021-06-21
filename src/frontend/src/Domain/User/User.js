import http from '@/Domain/Utility/http';
import UserCreate from './UserCreate';

class User {
  async create(name, email) {
    const creator = new UserCreate(name, email);
    await creator.create();
  }
  async all() {
    const response = await http.get('/users');
    return response.data;
  }
}
export default User;
