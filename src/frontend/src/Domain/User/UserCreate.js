import http from '@/Domain/Utility/http';

class UserCreate {
  constructor(user) {
    this.user = user;
  }

  validate() {
    return true;
  }

  async create() {
    if (!this.validate()) {
      return;
    }

    const response = await http.post('/users/create', {
      name: this.user.name,
      email: this.user.email,
      memo: this.user.memo,
      image: this.user.image,
    });
    return response.data;
  }
}

export default UserCreate;
