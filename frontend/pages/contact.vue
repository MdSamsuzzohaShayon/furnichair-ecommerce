<template>
    <div class="container mx-auto px-2 min-h-80">
        <h1 class="mt-8">Contact Us</h1>
        <Message />
        <div class="contact-us flex flex-col md:flex-row gap-4">
            <div class="contact-form w-full md:w-4/6">
                <h2 class="mt-8">We would love to hear from you.</h2>
                <p>If you’ve got great products your making or looking to work with us then drop us a line.</p>
                <form class="flex flex-col gap-4 mt-8" v-on:submit.prevent="contactSubmitHandler">
                    <div class="input-group w-full">
                        <input required="true" type="text" id="user-name"
                            class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                            placeholder="Name" v-model="willContact.name">
                    </div>
                    <div class="input-group w-full">
                        <input required="true" type="email" id="user-email"
                            class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                            placeholder="Email" v-model="willContact.email">
                    </div>
                    <div class="input-group w-full">
                        <textarea required="true" rows="5" id="user-email"
                            class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                            placeholder="Message" v-model="willContact.message" />
                    </div>
                    <div class="input-group w-full">
                        <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold"
                            type="submit">Submit</button>
                    </div>
                </form>
            </div>
            <div class="address w-full md:w-2/6">
                <h2 class="mt-8">Address</h2>
                <p v-for="a in address" v-bind:key="a.id">{{ a.name }} : {{ a.value }}</p>
                <h2 class="mt-8">Social Media</h2>
                <ul class="flex justify-start">
                    <li v-for="link in socialLinks" class="text-teal-950">
                        <NuxtLink v-bind:to="link.link">
                            <Icon v-bind:name="link.name" size="30" />
                        </NuxtLink>
                    </li>
                </ul>
                <h2 class="mt-8">We're Open</h2>
                <p>Our store has re-opened for shopping, exchanges Every day 11am to 7pm</p>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useContactStore from '../stores/ContactStore';
import useSettingStore from '../stores/SettingsStore';
import useElementsStore from '../stores/ElementsStore';

const contactStore = useContactStore();
const settingStore = useSettingStore();
const elementStore = useElementsStore();

const { willContact } = storeToRefs(contactStore);
const { address, socialLinks } = storeToRefs(settingStore);

const contactSubmitHandler = async (e: Event) => {
    elementStore.resetErrorMessageList();
    elementStore.resetSuccessMessageList();
    const { data: contactData, error: contactError, refresh: contactRequest, status: contactStatus } = await useFetch(`${BACKEND_URL}/contacts/new/`, {
        key: `contact-${new Date().getSeconds()}${new Date().getMilliseconds()}`,
        method: "POST",
        body: willContact.value
    });

    if (contactStatus.value === 'success' && contactData.value) {
        // Show success message
        console.log(contactData);
        const formEl = e.target as HTMLFormElement;
        formEl.reset();
        elementStore.setSuccessMessageList(['Thank you for connecting with us, our member will reply on you message!'])
    }
}
</script>

<style lang="scss" scoped></style>