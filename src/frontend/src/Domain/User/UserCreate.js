import http from '@/Domain/Utility/http';

class UserCreate {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  validate() {
    return true;
  }

  async create() {
    if (!this.validate()) {
      return;
    }
    const response = await http.post('/users/create', {
      name: this.name,
      email: this.email,
    });
    console.log(response);
  }
}

export default UserCreate;
