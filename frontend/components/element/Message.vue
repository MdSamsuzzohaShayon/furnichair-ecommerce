<template>
    <div >
        <p class="text-red-900 px-4 py-2 capitalize w-full bg-red-100 text-red-900" v-for="message in errorMessageList">
            {{ message }} <span class="float-right">
                <Icon name="grommet-icons:close" size="20" v-on:click.prevent="elementStore.resetErrorMessageList()" />
            </span> </p>
        <p class="text-teal-900 px-4 py-2 capitalize bg-teal-100 w-full" v-for="message in successMessageList">{{ message }} <span
                class="float-right cursor-pointer">
                <Icon name="grommet-icons:close" size="20" v-on:click.prevent="elementStore.resetSuccessMessageList()" />
            </span> </p>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useElementStore from '@/stores/ElementsStore';

const elementStore = useElementStore();

const { errorMessageList, successMessageList } = storeToRefs(elementStore);

</script>

<style scoped></style>