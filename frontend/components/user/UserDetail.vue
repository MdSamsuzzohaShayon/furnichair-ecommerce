<template>
    <div class="w-full mt-4">
        <h1 v-if="userInfo.first_name">{{ userInfo?.first_name + " " + userInfo?.last_name }}</h1>
        <p v-if="userInfo.id">ID# {{ userInfo?.id }}</p>
        <p v-if="userInfo.email">{{ userInfo.email }}</p>
    </div>
</template>

<script setup lang="ts">
const { userInfo } = defineProps(['userInfo']);
</script>

<style scoped></style>