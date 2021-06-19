<template>
  <div>
    <base-contents>
      <template #header>
        <breadcrumbs />
      </template>
      <template #contents></template>
    </base-contents>
  </div>
</template>

<script>
import BaseContents from '@/components/admin/BaseContents';
import Breadcrumbs from '@/components/admin/Breadcrumbs';
export default {
  name: 'User',
  components: {
    BaseContents,
    Breadcrumbs,
  },
};
</script>
