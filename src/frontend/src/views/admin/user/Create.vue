<template>
  <div>
    <base-contents>
      <template #header></template>
      <template #contents>
        <template>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="name"
              :counter="10"
              :rules="nameRules"
              label="名前"
              required
            ></v-text-field>

            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="E-mail"
              required
            ></v-text-field>

            <!--<v-textarea name="input-7-1" filled label="メモ" auto-grow v-model="memo"></v-textarea>-->

            <v-btn color="primary" depressed elevation="2" @click="send">送信</v-btn>
          </v-form>
        </template>
      </template>
    </base-contents>
  </div>
</template>

<script>
import BaseContents from '@/components/admin/BaseContents';
import UserCreate from '@/Domain/User/UserCreate';
export default {
  name: 'User',
  components: {
    BaseContents,
  },
  data() {
    return {
      name: '',
      email: '',
    };
  },
  methods: {
    async send() {
      const user = new UserCreate(this.name, this.email);
      await user.create();
    },
  },
};
</script>
