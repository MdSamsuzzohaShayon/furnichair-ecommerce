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
        <div class="w-full flex justify-center">
            <div class="password-reset w-full md:w-2/5">
                <h1 class="pt-8">Set New Password</h1>
                <form class="flex flex-col gap-4 mt-8" v-on:submit.prevent="resetPasswordHandler">
                    <div class="input-group w-full">
                        <input required="true" type="password" id="user-password"
                            class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                            placeholder="Password" v-model="state.password">
                    </div>
                    <div class="input-group w-full">
                        <input required="true" type="password" id="user-confirm-password"
                            class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                            placeholder="Confirm Password" v-model="state.confirm_password">
                    </div>
                    <div class="input-group w-full">
                        <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold"
                            type="submit">Submit</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useElementStore from '../../../stores/ElementsStore';
const token = useRoute().params.token;

const elementStore = useElementStore();
const { errorMessageList, successMessageList } = storeToRefs(elementStore);

const state = reactive({
    password: '',
    confirm_password: ''
});

const resetPasswordHandler = async (e: Event) => {
    elementStore.resetErrorMessageList();
    elementStore.resetSuccessMessageList();
    if (token) {
        try {
            console.log(state, state.password);

            const { data, error, status } = await useFetch(`${BACKEND_URL}/accounts/resetpassword/${token}/`, {
                method: "PUT",
                body: {
                    password: state.password,
                    confirm_password: state.confirm_password
                }
            });
            if (status.value === 'success' && data.value) {
                elementStore.setSuccessMessageList([data.value.detail])
            } else {
                elementStore.setErrorMessageList(Object.values(error.value.data)[0]);
            }
            // console.log(Object.values(responseObj));
        } catch (error) {
            elementStore.setErrorMessageList([JSON.stringify(error)])
        }

    }
}
</script>

<style lang="scss" scoped></style>