<template>
  <div>
    <base-contents>
      <template #header></template>
      <template #contents></template>
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
