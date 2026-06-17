<template>
    <div class="container mx-auto px-2 static">
        <h2 class="text-4xl mt-8">Shop by categories</h2>
        <div class="categories grid gap-4 grid-cols-4 mt-4">
            <!-- grid gap-4 grid-cols-3 grid-rows-3 -->
            <div class="category-item w-full bg-white shadow" v-for="cat in categoryList">
                <NuxtLink v-bind:to="'/categories/' + cat.id + '/'" class="w-full flex items-center justify-center flex-col" >
                    <img v-bind:src="CLOUDINARY_BASE_URL + '/' + cat.image" alt="" class="h-52 w-full object-center object-cover">
                    <h4 class="text-2xl font-normal w-full align-left p-2">{{ cat.name }}</h4>
                </NuxtLink>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useCategoryStore from '@/stores/CategoryStore';
// https://dev.to/rafaelmagalhaes/pinia-and-nuxt-3-4ij5
const categoryStore = useCategoryStore();
const { categoryList } = storeToRefs(categoryStore);

</script>