<template>
    <div class="container mx-auto px-2 min-h-80">
        <h1 class="mt-8">Cart</h1>
        <div class="cart-list mt-4">
            <div class="cart" v-for="c in cartList" v-bind:key="c.id">
                <div v-if="findProductById(c.pId)" v-bind:set="product = findProductById(c.pId)"
                    class="flex justify-between items-center bg-white mb-2 flex-col md:flex-row">
                    <img v-bind:src="CLOUDINARY_BASE_URL + '/' + findProductById(c.pId)?.image1" v-bind:alt="product?.title" class="w-full md:w-44 h-44 object-fit object-cover" loading="lazy" >
                    <h3 class="font-bold mt-4 md:mt-0 text-lg">{{ product?.title }}</h3>
                    <div class="seg-1 flex flex-col justify-center items-center h-full">
                        <div class="q-controller flex items-center justify-center">
                            <button class="bg-none text-teal-50 border-0 px-5 py-2" v-on:click.prevent="qtyChange(true)">
                                <Icon name="ep:plus" size="20" color="blue" />
                            </button>
                            <p>Quantity: {{ c.qty }}</p>
                            <button class="bg-none text-teal-50 border-0 px-5 py-2" v-on:click.prevent="qtyChange(false)">
                                <Icon name="ep:minus" size="20" color="blue" />
                            </button>
                        </div>
                    </div>
                    <div class="seg-2 flex flex-row md:flex-row py-2 md:py-0 px-2 gap-2">
                        <NuxtLink v-bind:to="`/checkout/${c.id}/`">
                            <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold">Checkout</button>
                        </NuxtLink>
                        <button type="button" v-on:click.prevent="removeFromCart(c.id)"
                            class="bg-red-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold">
                            Cancel
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useProductStore from '../../stores/ProductStore';
import type { IProduct } from '~/types';


const productStore = useProductStore();

await productStore.fetchProducts();
productStore.fetchCartFromLocalStorage();

const { cartList, productList } = storeToRefs(productStore);

const findProductById = (pId: number) => {
    const findProduct: IProduct | undefined = productList.value.find((p) => p.id === pId);
    if (findProduct) return findProduct;
    return null;
}

const qtyChange = (addQty: boolean) => {
    if (addQty) {
        console.log("Add more");
    } else {
        console.log("Sub more");
    }
}


const removeFromCart = (cId: string) => {
    productStore.removeItemFromCart(cId);
}
</script>

<style lang="scss" scoped></style>