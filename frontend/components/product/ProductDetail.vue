<template>
    <div class="container mx-auto px-2">
        <div class="flex justify-between items-center md:items-start gap-4 flex-col md:flex-row">
            <div class="w-full md:w-3/6">
                <img :src="state.previewImage ? CLOUDINARY_BASE_URL + '/' + state.previewImage : CLOUDINARY_BASE_URL + '/' + product.image1"
                    v-bind:alt="product.title" class="mx-auto my-7">
            </div>
            <div class="w-full md:w-3/6 text-teal-950">
                <h1 class="text-4xl my-7">{{ product.title }}</h1>
                <div class="product-images flex justify-start gap-4">
                    <img v-if="product.image1 && product.image1 !== null"
                        v-bind:src="CLOUDINARY_BASE_URL + '/' + product.image1" v-bind:alt="product.title"
                        class="w-20 h-20 border-4 border-teal-100"
                        v-on:click.prevent="imgChangeHandler(product.image1)">
                    <img v-if="product.image2 && product.image2 !== null"
                        v-bind:src="CLOUDINARY_BASE_URL + '/' + product.image2" v-bind:alt="product.title"
                        class="w-20 h-20 border-4 border-teal-100"
                        v-on:click.prevent="imgChangeHandler(product.image2)">
                    <img v-if="product.image3 && product.image3 !== null"
                        v-bind:src="CLOUDINARY_BASE_URL + '/' + product.image3" v-bind:alt="product.title"
                        class="w-20 h-20 border-4 border-teal-100"
                        v-on:click.prevent="imgChangeHandler(product.image3)">
                    <img v-if="product.image4 && product.image4 !== null"
                        v-bind:src="CLOUDINARY_BASE_URL + '/' + product.image4" v-bind:alt="product.title"
                        class="w-20 h-20 border-4 border-teal-100"
                        v-on:click.prevent="imgChangeHandler(product.image4)">
                </div>
                <h2 class="mt-4" v-if="product.discount_price && product.discount_price > 0"> ৳{{ product.price }}
                    <span class="line-through text-teal-950/50 ml-4">৳{{ product.price }}</span>
                </h2>
                <h2 class="mt-4" v-else>৳{{ product.price }}</h2>

                <h3 class="font-blod border-b-2 mt-4 pb-2">Product Description</h3>
                <p class="mb-7">{{ product.description }}</p>
                <div class="add-to-cart flex gap-4 mt-4">
                    <div class="quantity flex justify-around bg-white text-teal-950 border border-teal-950/25 w-2/6">
                        <button class="bg-none text-teal-50 border-0 px-5 py-2" v-on:click.prevent="state.quantity++">
                            <Icon name="ep:plus" size="20" color="blue" />
                        </button>
                        <input type="number" v-bind:max="product.total_stock"
                            class="remove-arrow text-teal-950 outline-0 text-base border-0" v-model="state.quantity"
                            min="1">
                        <button class="bg-none text-teal-50 border-0 px-5 py-2" v-on:click.prevent="state.quantity--">
                            <Icon name="ep:minus" size="20" color="blue" />
                        </button>
                    </div>
                    <button
                        class="flex w-4/6 items-center gap-4 justify-center bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold "
                        v-on:click="addToCartHandler">
                        <Icon name="simple-line-icons:basket" size="30" />
                        Add to cart
                    </button>
                </div>
                <div class="buy-now mt-2">
                    <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-3 w-full font-bold"
                        v-on:click="buyNowHandler">Buy Now</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useProductStore from '@/stores/ProductStore';
import useElementStore from '@/stores/ElementsStore';
import useUserStore from '@/stores/UserStore';
import useOrderStore from '@/stores/OrderStore';
import type { OrderInterface } from '@/types/ProductOrderType';



const { product } = defineProps(['product']);

const productStore = useProductStore();
const elementsStore = useElementStore();
const userStore = useUserStore();
const orderStore = useOrderStore();

const state = reactive({
    quantity: 1,
    previewImage: null as string | null
});
const { userInfo } = storeToRefs(userStore)

// const { cartList } = storeToRefs(productStore)
const imgChangeHandler = (selectedImgUrl: string) => {
    state.previewImage = selectedImgUrl;
}
const addToCartHandler = (e: Event) => {
    e.preventDefault();
    const newProduct = { id: `${window.crypto.randomUUID()}`, pId: product.id, qty: state.quantity };
    productStore.addItemToCart(newProduct);
}
const buyNowHandler = async (e: Event) => {
    e.preventDefault();
    const accessToken = useCookie(ACCESS_TOKEN);
    if (!accessToken.value) {
        console.error('There is no access token');
        return;

    }

    if (!userInfo.value.address) {
        console.error("No address found");

        return;
    }
    const { data: orderData, status: orderStatus, error: orderErrors } = await useFetch<OrderInterface>(`${BACKEND_URL}/orders/new/`, {
        method: "POST",
        body: {
            product: product.id,
            quantity: 1,
            address: userInfo.value.address[0].id,
        },
        headers: {
            "Authorization": `Bearer ${accessToken.value}`
        }
    });
    if (orderStatus.value === 'success' && orderData.value) {
        orderStore.addNewOrder(orderData.value);
        navigateTo("/user/dashboard/");
    } else {
        console.log(orderErrors.value);
        elementsStore.setErrorMessageList(Object.entries(orderErrors.value));
    }

}


</script>

<style scoped></style>