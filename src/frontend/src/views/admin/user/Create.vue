<template>
  <div>
    <base-contents>
      <template #header></template>
      <template #contents>
        <template>
          <v-form ref="form" v-model="valid">
            <v-text-field
              v-model="user.name"
              :counter="10"
              :rules="[nameRules.required, nameRules.length]"
              label="名前"
              required
            ></v-text-field>

            <v-text-field
              v-model="user.email"
              :rules="[emailRules.required, emailRules.validEmail]"
              label="E-mail"
              required
            ></v-text-field>

            <v-file-input truncate-length="15" @change="selected"></v-file-input>

            <v-textarea
              name="input-7-1"
              filled
              label="メモ"
              auto-grow
              v-model="user.memo"
            ></v-textarea>

            <v-btn :disabled="!valid" color="primary" depressed elevation="2" @click="send"
              >送信</v-btn
            >
          </v-form>
        </template>
      </template>
    </base-contents>
  </div>
</template>

<script>
import BaseContents from '@/components/admin/BaseContents';
import User from '@/Domain/User/User';
export default {
  name: 'User',
  components: {
    BaseContents,
  },
  data() {
    return {
      user: {
        name: '',
        email: '',
        memo: '',
        image: '',
      },
      uploadFile: null,
      valid: false,
      nameRules: {
        required: (v) => !!v || '名前を入力して下さい。',
        length: (v) =>
          (2 <= v.length && v.length <= 100) || '２文字以上１００文字以内で入力して下さい。',
      },
      emailRules: {
        required: (v) => !!v || 'メールアドレスを入力して下さい。',
        validEmail: (email) => {
          const regex = /^.+[^.]@.+\..+$/;
          return regex.test(email) || '正しい形式のメールアドレスを登録して下さい。';
        },
      },
    };
  },
  methods: {
    async send() {
      const user = new User();
      const data = await user.create(this.user);
      console.log(`送信完${data}`);
    },
    selected(file) {
      this.uploadFile = file;
    },
  },
};
</script>
