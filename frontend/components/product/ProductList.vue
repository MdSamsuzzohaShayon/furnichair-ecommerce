<template>
    <div>
        <!-- <h1>Product List</h1> -->
        <!-- productList -->
        <table class="w-full mt-4">
            <thead>
                <tr>
                    <th class="p-2 text-center border border-teal-900">ID</th>
                    <th class="p-2 text-center border border-teal-900">Title</th>
                    <th class="p-2 text-center border border-teal-900">Category</th>
                    <th class="p-2 text-center border border-teal-900">Price</th>
                    <th class="p-2 text-center border border-teal-900">Discounted Price</th>
                    <th class="p-2 text-center border border-teal-900">Stock</th>
                    <th class="p-2 text-center border border-teal-900">Perform</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="product in productList">
                    <td class="p-2 text-center border border-teal-900/50">{{ product.id }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ product.title }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ product.category?.name }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ product.price }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ product.discount_price }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ product.total_stock }}</td>
                    <td class="p-2 text-center border border-teal-900/50">
                        <Icon class="pr-2" size="20" name="lucide:trash-2" color="red"
                            v-on:click.prevent="deleteProductHandler(product.id)" />
                        <NuxtLink v-bind:to="`/products/${product.id}`">
                            <Icon class="pr-2" size="20" name="bytesize:eye" color="teal" />
                        </NuxtLink>
                        <Icon class="pr-2" size="20" name="line-md:edit" v-on:click.prevent="updateProductHandler(product.id)" color="teal" />
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';

import useProductStore from '@/stores/ProductStore';

const productsStore = useProductStore();

const { productList } = storeToRefs(productsStore);

const deleteProductHandler = (pId: number | null) => {
    console.log("Delete product -> ", pId);
}

const updateProductHandler=(pId: number)=>{
    productsStore.setProductUpdate(true);
    productsStore.setProductToUpdate(pId);
}

</script>

<style scoped></style>