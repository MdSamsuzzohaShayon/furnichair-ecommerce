<template>
    <div class="container mx-auto px-2 ">
        <div class="message-content w-full mt-8">
            <Message />
        </div>
        <div class="main-content flex flex-col md:flex-row justify-start gap-8">
            <div class="sign-in w-full md:w-2/5">
                <h1 class="pt-8">Login</h1>
                <form class="flex flex-col gap-4 mt-8" v-on:submit.prevent="signinHandler">
                    <div class="input-group w-full">
                        <input required="true" type="email" id="user-email"
                            class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                            placeholder="Email" v-model="userSignin.email">
                    </div>
                    <div class="input-group flex justify-between gap-4">
                        <input required="true" type="password" id="user-password"
                            class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                            placeholder="Password" v-model="userSignin.password">
                    </div>
                    <div class="input-group w-full">
                        <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold"
                            type="submit">Login</button>
                    </div>
                    <div class="input-group w-full flex flex-col">
                        <NuxtLink to="/user/passwordforget" class="underline">Password forgotten?</NuxtLink>
                        <NuxtLink to="/user/signup" class="underline">Don't have an account? register.</NuxtLink>
                    </div>
                </form>
            </div>

            <div class="new-customer w-full md:w-2/5">
                <h1 class="pt-8">New Customer</h1>
                <p class="mt-8 mb-2">Sign up for early Sale access plus tailored new arrivals,trends and promotions. To
                    opt
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
import useUserStore from '@/stores/UserStore';
import useElementStore from '@/stores/ElementsStore';
import type { ISignInResponse } from '~/types/UserType';
import { ACCESS_TOKEN, REFRESH_TOKEN } from '~/utils/constant';

const oneDayInSeconds = 24 * 60 * 60; // 1 day = 24 hours * 60 minutes * 60 seconds


interface SignInProps {
    is_staff?: boolean;
}

const props = defineProps<SignInProps>();

const userStore = useUserStore();
const elementStore = useElementStore();

const { userSignin, isAuthenticated } = storeToRefs(userStore);
const { errorMessageList, successMessageList } = storeToRefs(elementStore);


const signinHandler = async (_event: SubmitEvent): Promise<void> => {
    elementStore.resetErrorMessageList();
    elementStore.resetSuccessMessageList();

    const validData = userStore.serializedUserSignin;

    if (!validData) {
        elementStore.setErrorMessageList(["Invalid data!"]);
        return;
    }

    const {
        data,
        error,
        status,
    } = await useFetch<ISignInResponse>(
        `${BACKEND_URL}/accounts/signin/`,
        {
            method: "POST",
            body: validData,
        }
    );

    if (status.value !== "success" || !data.value) {
        if (error.value?.statusCode === 401) {
            elementStore.setErrorMessageList(["Invalid credentials!"]);
        } else if (error.value) {
            elementStore.setErrorMessageList([JSON.stringify(error.value)]);
        }

        return;
    }

    userStore.setIsAuthenticated(true);

    const { access, refresh: refreshToken } = data.value;

    const accessTokenCookie = useCookie<string>(ACCESS_TOKEN, {
        maxAge: 60 * 15,
        sameSite: "lax",
        secure: import.meta.env.PROD,
        path: "/",
    });

    accessTokenCookie.value = access;

    const refreshTokenCookie = useCookie<string>(REFRESH_TOKEN, {
        maxAge: 60 * 60 * 24 * 7,
        sameSite: "lax",
        secure: import.meta.env.PROD,
        path: "/",
    });

    refreshTokenCookie.value = refreshToken;

    await userStore.fetchUser(access);

    await navigateTo(
        props.is_staff
            ? "/admin/"
            : "/user/dashboard/"
    );
};
</script>

<style scoped></style>