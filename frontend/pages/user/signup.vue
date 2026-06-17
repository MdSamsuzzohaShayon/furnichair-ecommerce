<template>
    <div class="container mx-auto px-2 flex justify-center min-h-80">
        <div class="sign-in w-full md:w-2/5">
            <h1 class="pt-8">Register</h1>
            <Message />
            <form class="flex flex-col gap-4 mt-8" v-on:submit.prevent="signupHandler">
                <div class="input-group w-full">
                    <input required="true" type="text" id="user-first-name"
                        class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                        placeholder="First Name" v-model="userSignup.first_name">
                </div>
                <div class="input-group w-full">
                    <input required="true" type="text" id="user-last-name"
                        class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                        placeholder="Last Name" v-model="userSignup.last_name">
                </div>
                <div class="input-group w-full">
                    <input required="true" type="email" id="user-email"
                        class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                        placeholder="Email" v-model="userSignup.email">
                </div>
                <div class="input-group w-full">
                    <input required="true" type="password" id="user-password"
                        class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                        placeholder="Password" v-model="userSignup.password">
                </div>
                <div class="input-group w-full">
                    <input required="true" type="password" id="user-confirm-password"
                        class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                        placeholder="Confirm Password" v-model="userSignup.confirm_password">
                </div>
                <div class="input-group w-full">
                    <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold"
                        type="submit">Register</button>
                </div>
                <div class="input-group w-full flex flex-col">
                    <NuxtLink to="/user/signin" class="underline">Already have an account? login.</NuxtLink>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useUserStore from '../../stores/UserStore';
import useElementStore from '../../stores/ElementsStore';

// Meta
definePageMeta({
  middleware: ["auth"]
  // or middleware: 'auth'
});

const userStore = useUserStore();
const elementStore = useElementStore();

const { userSignup } = storeToRefs(userStore);
const { errorMessageList, successMessageList } = storeToRefs(elementStore);

const signupHandler = async (e: Event) => {
    elementStore.resetErrorMessageList();
    elementStore.resetSuccessMessageList();
    const validData = userStore.serializedUserSignup
    if (validData) {
        // https://youtrack.jetbrains.com/issue/WEB-58600
        // @ts-ignore
        const { data, pending, error, refresh, status } = await useFetch(`${BACKEND_URL}/accounts/signup/`, {
            method: "POST",
            body: validData
        });
        // console.log({ data: data.value, pending: pending.value, error: error.value, refresh: refresh, status: status.value });
        if (data.value) {
            if (status.value === 'success') {
                elementStore.setSuccessMessageList(Object.values(data.value));
            } else {
                elementStore.setErrorMessageList(Object.values(data.value))
            }
        }

    }
}



</script>

<style scoped></style>