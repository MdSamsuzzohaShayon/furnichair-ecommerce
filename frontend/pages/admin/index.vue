<template>
    <div class="container mx-auto px-2 static min-h-80">
        <!-- <h2>Admin Panel</h2> -->
        <div class="flex justify-between flex-col md:flex-row admin-panel">
            <div class="left-side-bar w-full md:w-2/12 sticky top-0 h-fit md:h-screen bg-white">
                <ul class="w-full px-2 py-4 md:py-8 flex gap-4 flex-row md:flex-col flex-wrap">
                    <li v-for="dsi in dashboardSidebar" v-on:click.prevent="elementStore.changeDSID(dsi.id)"
                        class="border-1 border-teal-950 flex justify-start items-center gap-2 p-0 md:p-2 cursor-pointer">
                        <Icon v-bind:name="dsi.name" size="20" />
                        <p class="capitalize">{{ dsi.text }}</p>
                    </li>
                </ul>
            </div>
            <div class="content w-full md:w-10/12">
                <div class="selected-item pt-4 md:pt-8 px-0 md:px-4" v-if="selectedDSID === 1">
                    <h2>Product <span class="float-right text-lg cursor-pointer" v-on:click="addProductComp">Add New
                            <Icon name="ep:plus" size="20" color="blue" />
                        </span> </h2>
                    <ProductList v-if="showProductList === true" />
                    <ProductAdd v-else />
                </div>
                <div class="selected-item pt-4 md:pt-8 px-0 md:px-4" v-else-if="selectedDSID === 2">
                    <h2>Category</h2>
                    <CategoryAdd />
                    <CategoryList />
                </div>
                <div class="selected-item pt-4 md:pt-8 px-0 md:px-4" v-else-if="selectedDSID === 3">
                    <h2>Delivery Place</h2>
                    <DeliveryPlaceAdd/>
                    <DeliveryPlaceList />
                </div>
                <div class="selected-item pt-4 md:pt-8 px-0 md:px-4" v-else-if="selectedDSID === 4">
                    <h2>Setting</h2>
                    <SettingAdd />
                </div>
                <div class="selected-item pt-4 md:pt-8 px-0 md:px-4" v-else-if="selectedDSID === 5">
                    <h2>Order</h2>
                    <!-- <OrderDetail /> -->
                    <OrderList />
                </div>
                <div class="selected-item pt-4 md:pt-8 px-0 md:px-4" v-else-if="selectedDSID === 6">
                    <h2>Wishlist</h2>
                    <WishlistList />
                </div>
                <div class="selected-item pt-4 md:pt-8 px-0 md:px-4" v-else-if="selectedDSID === 7">
                    <h2>Inbox</h2>
                    <ContactList />
                </div>
                <div class="selected-item pt-4 md:pt-8 px-0 md:px-4" v-else-if="selectedDSID === 8">
                    <h2>User</h2>
                    <UserList />
                </div>
            </div>
        </div>
        <p class="text-red-900 px-4 py-2 capitalize" v-for="message in errorMessageList">{{ message }}</p>
        <p class="text-teal-900 px-4 py-2 capitalize" v-for="message in successMessageList">{{ message }}</p>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';

import useElementStore from '@/stores/ElementsStore';
import useProductStore from '@/stores/ProductStore';
import useOrderStore from '@/stores/OrderStore';
import useUserStore from '@/stores/UserStore';
import useDeliveryPlaceStore from '@/stores/DeliveryPlaceStore';

// Meta
definePageMeta({
    middleware: ["auth"]
    // or middleware: 'auth'
});

const elementStore = useElementStore();
const productsStore = useProductStore();
const orderStore = useOrderStore();
const userStore = useUserStore();
const deliveryPlaceStore = useDeliveryPlaceStore();

const { dashboardSidebar, selectedDSID, errorMessageList, successMessageList, addProduct, showProductList } = storeToRefs(elementStore);

const accessToken = useCookie(ACCESS_TOKEN);
if (!accessToken.value) {
    console.error('There is no access token');
}

const fetchAtBeginning = [];
fetchAtBeginning.push(productsStore.fetchProducts());
fetchAtBeginning.push(deliveryPlaceStore.fetchAllPlaces());

if (accessToken.value) {
    fetchAtBeginning.push(orderStore.fetchAllOrders(accessToken.value));
    fetchAtBeginning.push(userStore.fetchAllUser(accessToken.value));
    // Check if the token is invalid - make a request with refresh token to get new access token
}
await Promise.all(fetchAtBeginning);

// Fetch according to buttons
const addProductComp = async () => {
    elementStore.setAddProduct(true);
    elementStore.setShowProductList(false);
    await productsStore.fetchProducts();
}

</script>

<style lang="scss" scoped></style>