<template>
    <div class="container mx-auto px-2 min-h-80">
        <UserSignin v-bind:is_staff="false" />
    </div>
</template>

<script setup lang="ts">
// Meta
definePageMeta({
  middleware: ["auth"]
  // or middleware: 'auth'
});
</script>

<style scoped></style>