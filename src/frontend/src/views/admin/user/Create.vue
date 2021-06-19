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

            <v-textarea
              name="input-7-1"
              filled
              label="メモ"
              auto-grow
              value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
            ></v-textarea>

            <v-btn :disabled="!valid" color="success" class="mr-4" @click="validate">
              Validate
            </v-btn>

            <v-btn color="error" class="mr-4" @click="reset"> Reset Form </v-btn>

            <v-btn color="warning" @click="resetValidation"> Reset Validation </v-btn>
          </v-form>
        </template>
      </template>
    </base-contents>
  </div>
</template>

<script>
import BaseContents from '@/components/admin/BaseContents';
export default {
  name: 'User',
  components: {
    BaseContents,
  },
};
</script>
