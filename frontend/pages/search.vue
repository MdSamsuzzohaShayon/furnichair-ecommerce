<template>
    <div class="container mx-auto px-2 min-h-80">
        <h1 class="mt-8">{{ productList.length }} items found</h1>
        <button class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 px-1 placeholder:text-teal-950/50 mt-4 mb-4" v-on:click.prevent="elementStore.openFilterBar()">
            Filter 
            <Icon name="clarity:filter-line" size="30" />
        </button>
        <ProductFilter />
        <div v-for="p in productList">
            <!-- <NuxtLink v-bind:to="`/products/${p.id}/`">{{ p.title }}</NuxtLink> -->
            <ProductCard v-bind:product="p" />
        </div>
    </div>
</template>

<script setup lang="ts">

import { storeToRefs } from 'pinia';
import useProductStore from '../stores/ProductStore';
import useElementStore from '../stores/ElementsStore';

const elementStore = useElementStore();
const productStore = useProductStore();
const { productList } = storeToRefs(productStore);

const params = new URLSearchParams(window.location.search);
await productStore.fetchProducts(params.get('q'));
</script>
