<template>
    <div class="w-full overflow-x-auto">
        <!-- <ul class="w-full md:w-2/6">
            <li></li>
        </ul>
        <div class="message-content w-full">

        </div> -->
        <table class="w-full mt-4">
            <thead>
                <tr>
                    <th class="p-2 text-center border border-teal-900">ID</th>
                    <th class="p-2 text-center border border-teal-900">Name</th>
                    <th class="p-2 text-center border border-teal-900">Email</th>
                    <th class="p-2 text-center border border-teal-900">Message</th>
                    <th class="p-2 text-center border border-teal-900">Date</th>
                    <th class="p-2 text-center border border-teal-900">Perform</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="contact in contactList">
                    <td class="p-2 text-center border border-teal-900/50">{{ contact.id }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ contact.name }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ contact.email }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ contact.message }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ isoToDate(contact.created_at) }}</td>
                    <td class="p-2 text-center border border-teal-900/50">
                        <p class="cursor-pointer text-teal-900" v-on:click.prevent="previewContactMessage(contact.id)">Preview
                        </p>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useContactStore from '@/stores/ContactStore';

const contactStore = useContactStore();

const { contactList } = storeToRefs(contactStore);

const accessToken = useCookie(ACCESS_TOKEN);

if (accessToken && accessToken.value) {
    await contactStore.fetchContacts(accessToken.value);
}else{
    console.error("Access token does not have any value");
}



const previewContactMessage = (contactId: number) => {
    console.log(contactId);
}

</script>

<style scoped></style>