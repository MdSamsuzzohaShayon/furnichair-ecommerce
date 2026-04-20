<template>
    <div class="relative index-page-content">
        <div class="new-arrival-wrapper" v-for="(na, index) in newArrivals" v-bind:key="index">
            <div class="single-arrival-item relative h-fit md:h-screen flex justify-center items-center flex-col" v-if="selectedProductId === na.id">
                <div class="background-image w-full absolute top-0 left-0 z-0">
                    <img v-bind:src="na.image1" v-bind:alt="na.title"
                        class="arrival-item-img h-80 w-full object-center object-cover">
                </div>
                <div
                    class="text-and-controls absolute left-0 flex justify-center items-center flex-col w-full z-10">
                    <h1 class="text-4xl capitalize font-normal text-4xl leading-6 pt-8 md:pt-0">{{ siteTitle }}</h1>
                    <p class="mt-4 w-full md:w-4/6 px-4 md:p-0 text-center">{{ siteDesc }}</p>
                    <h2 class="text-sm mt-4">{{ na.title }}</h2>
                    <NuxtLink to="/products/">
                        <button
                            class="mt-4 bg-transparent text-teal-900 border-2 border-teal-950 px-5 py-2 font-bold hover:text-teal-50 hover:bg-teal-900">Shop
                            Now</button>
                    </NuxtLink>

                    <div class="slider-controls mt-4 md:mt-32">
                        <button class="border-0 bg-none mr-32">
                            <Icon name="simple-line-icons:arrow-left" size="20" color="black"
                                v-on:click.prevent="settingsStore.changeSliderItem(false)" />
                        </button>
                        <button class="border-0 bg-none">
                            <Icon name="simple-line-icons:arrow-right" size="20" color="black"
                                v-on:click.prevent="settingsStore.changeSliderItem(true)" />
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <Category />

        <section class="section-2 container mx-auto px-2">
            <h2 class="mt-8">Fetured</h2>
            <div class="grid grid-cols-1 md:grid-cols-4 gap-5 mt-4">
                <div v-for="p in featuredProductList">
                    <ProductCard v-bind:product="p" />
                </div>
            </div>
        </section>
        <div class="section-3 container mx-auto px-2">
            <div class="service-advantage py-8 flex justify-between gap-3 items-center">
                <div class="advantage w-2/6 flex justify-between items-center flex-col" v-for="ad in advantages" >
                    <Icon v-bind:name="ad.icon" size="40" color="black" />
                    <h3>{{ ad.title }}</h3>
                    <p>{{ ad.desc }}</p>
                </div>
            </div>
        </div>
        <section class="section-3 container mx-auto px-2">
            <h2 class="mt-8">New Collections</h2>
        </section>
        <section class="section-4 container mx-auto px-2">
            <h2 class="mt-8">Trusted By Top Companies</h2>
            <div class="company-logos flex justify-between mt-4 flex-wrap">
                <div v-for="logo in trustedCompanyLogos" class="w-20 w-1/6" >
                    <img v-bind:src="'/img/'+logo" alt="" class="h-20">
                </div>
            </div>
        </section>

    </div>
</template>

<script setup lang="ts">
import '~/assets/css/index.css';
import { storeToRefs } from 'pinia';
import useSettingsStore from '@/stores/SettingsStore';
import useProductStore from '@/stores/ProductStore';

const settingsStore = useSettingsStore();
const productStore = useProductStore();

const { newArrivals, selectedProductId, siteTitle, siteDesc, featuredProductList, trustedCompanyLogos, advantages } = storeToRefs(settingsStore);
const { productList } = storeToRefs(productStore);

await productStore.fetchProducts();
const newProductList = productList.value.slice(0, 5);
settingsStore.setFeaturedProducts(newProductList);
</script>

<style scoped></style>