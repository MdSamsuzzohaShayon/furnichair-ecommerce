<template>
    <div class="min-h-80">

        <Head>
            <Title>Shakil Furniture | {{ productSingle.title }}</Title>
            <Meta name="description" :content="productSingle.description" />
            <Meta name="keywords" :content="`${productSingle.title}, ${productSingle.title} features, benefits, specifications, buy ${productSingle.title}, Ecommerce, Shopping, Online Store`" />
        </Head>
        <ProductDetail v-bind:product="productSingle" />
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useProductStore from '../../stores/ProductStore';

const { id } = useRoute().params;

const productStore = useProductStore();

await productStore.fetchSingleProduct(id);

const { productSingle } = storeToRefs(productStore);



// definePageMeta({
//     layout: 'products'
// });

</script>

