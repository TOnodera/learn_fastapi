<template>
  <div>
    <base-contents>
      <template #header>
        <breadcrumbs />
      </template>
      <template #contents>
        <v-data-table
          :headers="headers"
          :items="users"
          :items-per-page="5"
          class="elevation-1"
          @click:row="rowClicked"
        ></v-data-table>
      </template>
    </base-contents>
  </div>
</template>

<script>
import BaseContents from '@/components/admin/BaseContents';
import Breadcrumbs from '@/components/admin/Breadcrumbs';
import User from '@/Domain/User/User';
export default {
  name: 'User',
  components: {
    BaseContents,
    Breadcrumbs,
  },
  async mounted() {
    const user = new User();
    this.users = await user.all();
  },
  methods: {
    rowClicked(value) {
      console.log(value.id, value.name, value.email);
    },
  },
  data() {
    return {
      headers: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        { text: 'name', value: 'name' },
        { text: 'email', value: 'email' },
      ],
      users: [],
    };
  },
};
</script>
