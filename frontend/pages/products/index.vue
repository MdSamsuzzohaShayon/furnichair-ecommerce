<template>
  <div class="container mx-auto px-2 min-h-80">
    <h1 class="mt-8">Products</h1>
    <button
      class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 px-1 placeholder:text-teal-950/50 mt-4 mb-4"
      v-on:click.prevent="elementStore.openFilterBar()"
    >
      Filter
      <Icon name="clarity:filter-line" size="30" />
    </button>
    <ProductFilter />
    <div class="grid grid-cols-1 md:grid-cols-4 gap-5 mt-2">
      <div v-for="p in productList">
        <!-- <NuxtLink v-bind:to="`/products/${p.id}/`">{{ p.title }}</NuxtLink> -->
        <ProductCard v-bind:product="p" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import useProductStore from "../../stores/ProductStore";
import useElementStore from '../../stores/ElementsStore';

const elementStore = useElementStore();
const productStore = useProductStore();

await productStore.fetchProducts();
const { productList } = storeToRefs(productStore);
// definePageMeta({
//     layout: 'products'
// });

// const { data: products } = await useFetch('http://localhost:8000/api/products/');
</script>

<style scoped></style>
