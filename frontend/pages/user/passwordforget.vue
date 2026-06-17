<template>
    <div class="container mx-auto px-2 min-h-80">
        <div class="message-content w-full">
            <p class="text-red-900 px-4 py-2 capitalize w-full bg-red-100" v-for="message in errorMessageList">
                {{ message }} <span class="float-right cursor-pointer">
                    <Icon name="grommet-icons:close" size="20" v-on:click.prevent="elementStore.resetErrorMessageList()" />
                </span> </p>

            <p class="text-teal-900 px-4 py-2 capitalize w-full bg-teal-100" v-for="message in successMessageList">
                {{ message }} <span class="float-right cursor-pointer">
                    <Icon name="grommet-icons:close" size="20"
                        v-on:click.prevent="elementStore.resetSuccessMessageList()" />
                </span> </p>
        </div>
        <div class="main-content flex flex-col md:flex-row justify-start gap-8">
            <div class="forget-password w-full md:w-2/5">
                <h1 class="mt-8">Forget password</h1>
                <form class="flex flex-col gap-4 mt-4" v-on:submit.prevent="forgetpasswordHandler">
                    <div class="input-group w-full">
                        <input required="true" type="email" id="user-email"
                            class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                            placeholder="Email" v-model="emailOfUser">
                    </div>
                    <div class="input-group w-full">
                        <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold"
                            type="submit">Submit</button>
                    </div>
                    <div class="input-group w-full flex flex-col">
                        <NuxtLink to="/user/signin/" class="underline">Remember password?</NuxtLink>
                    </div>
                </form>
            </div>

            <div class="new-customer w-full md:w-2/5">
                <h1 class="pt-8">New Customer</h1>
                <p class="mt-8 mb-2">Sign up for early Sale access plus tailored new arrivals,trends and promotions. To opt
                    out,
                    click unsubscribe in our emails.</p>
                <NuxtLink to="/user/signup">
                    <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 font-bold"
                        type="button">Register</button>
                </NuxtLink>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useUserStore from '../../stores/UserStore';
import useElementStore from '../../stores/ElementsStore';
import { UserRequestSuccessResInt } from '../../types/UserType'


const userStore = useUserStore();
const elementStore = useElementStore();

const { emailOfUser } = storeToRefs(userStore);
const { errorMessageList, successMessageList } = storeToRefs(elementStore);


const forgetpasswordHandler = async (e: Event) => {
    try {
        elementStore.resetErrorMessageList();
        elementStore.resetSuccessMessageList();
        const { data, error, status } = await useFetch<UserRequestSuccessResInt>(`${BACKEND_URL}/accounts/forgotpassword/`, {
            method: "PUT",
            body: {
                email: emailOfUser.value
            }
        });
        if (status.value === 'success' && data.value) {
            if (data.value.detail) elementStore.setSuccessMessageList([data.value.detail])
        } else if (error.value && error.value.data && Object.values(error.value.data).length > 0) {
            // @ts-ignore
            elementStore.setErrorMessageList(Object.values(error.value.data)[0]);
        }else{
            elementStore.setErrorMessageList(["No user found with this email!"]);
        }
    } catch (error) {
        console.log({ error: error });
        
    }
}
</script>

<style scoped></style>