<template>
    <div class="min-h-80">
        <UserSignin v-bind:is_staff="true" />
    </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import useUserStore from '@/stores/UserStore';

// Meta
definePageMeta({
  middleware: ["auth"]
  // or middleware: 'auth'
});


const userStore = useUserStore();

const { isAuthenticated, userInfo } = storeToRefs(userStore);

onMounted(() => {
    if (isAuthenticated.value === true) {
        if (userInfo.value.is_admin === true || userInfo.value.is_staff === true){
            navigateTo('/admin/');
        }else{
            navigateTo('/user/dashboard');
        }
    }
});
</script>

<style lang="scss" scoped></style>