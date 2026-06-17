<template>
    <div class="bg-white shadow-md h-full text-center">
        <NuxtLink v-bind:to="`/products/${product.id}/`">
            <img v-bind:src="CLOUDINARY_BASE_URL + '/' + product.image1" class="w-full h-60 md:h-80 object-fit object-cover" v-bind:alt="product.title" loading="lazy" >
            <!-- <p class="font-semibold capitalize mt-4 md:mt-8 text-teal-950">{{ product.title }}</p> -->
            <h2 class="text-teal-950 ">{{ product.title }}</h2>
            <p v-if="product.discount_price" class="text-teal-950"> ৳{{ product.discount_price }} <span class="line-through text-teal-950/50 ml-4">৳{{ product.price }}</span> </p>
            <p v-else class="text-teal-950" > ৳{{ product.price }} </p>
            <p class="text-teal-950 pb-2">Stock {{ product.total_stock }}</p>
            <!-- <button type="button" class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold">Detail</button> -->
        </NuxtLink>
    </div>
</template>

<script setup>
const { product } = defineProps(['product'])

</script>

<style scoped></style>