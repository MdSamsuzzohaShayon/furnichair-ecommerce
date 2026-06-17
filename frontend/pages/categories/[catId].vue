<template>
    <div class="container mx-auto px-2 min-h-80" >
        <Head>
            <Title>Shakil Furniture | {{ currentCategory?.name }}</Title>
            <Meta name="description" :content="`Browse our extensive ${currentCategory?.name} collection featuring the latest trends and top-quality items.`" />
            <Meta name="keywords" :content="`${currentCategory?.name}, Category Products, Ecommerce, Shopping, Online Store`" />
        </Head>
        <h1 class="mt-8">Category: {{ currentCategory?.name }}</h1>
        <div class="grid grid-cols-4 gap-5 mt-4">
            <div v-for="p in productList">
                <!-- <NuxtLink v-bind:to="`/products/${p.id}/`">{{ p.title }}</NuxtLink> -->
                <ProductCard v-bind:product="p" />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import useProductStore from '../../stores/ProductStore';
import useCategoryStore from '../../stores/CategoryStore';
import { storeToRefs } from 'pinia';
const { catId } = useRoute().params;

const productStore = useProductStore();
const categoryStore = useCategoryStore();

const { productList } = storeToRefs(productStore);
const { currentCategory } = storeToRefs(categoryStore);

categoryStore.setCurrentCategory(parseInt(catId, 10))
await productStore.fetchProductsByCategory(catId);

</script>

<style lang="scss" scoped></style>