<template>
    <div>
        <header class="shadow-sm bg-white">
            <nav class="container mx-auto p-4 flex justify-between">
                <NuxtLink to="/"><img v-bind:src="logoUrl" alt="" class="h-8"></NuxtLink>
            </nav>
        </header>

        <!-- Output the page content  -->
        <slot />
        <footer class="container mx-auto p-4 flex justify-between border-t-1">
            <ul
                class="flex justify-start list-none flex-col md:flex-row h-screen md:h-fit w-full px-4 py-8 md:p-0 gap-4 md:gap-1">
                <li class="cursor-pointer font-semibold mr-4" v-for="menu in menus">
                    <NuxtLink v-bind:to="menu.link" class="capitalize">{{ menu.text }}</NuxtLink>
                </li>
            </ul>
        </footer>
    </div>
</template>


<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useSettingsStore from '../stores/SettingsStore';
import useElementsStore from '../stores/ElementsStore';

// Pinia State
const settingsStore = useSettingsStore();
const elementsStore = useElementsStore();

const { logoUrl } = storeToRefs(settingsStore);
const { menus } = storeToRefs(elementsStore);
</script>

