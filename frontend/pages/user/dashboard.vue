<template>
    <div class="container mx-auto px-2 static min-h-80">
        <div class="flex justify-between flex-col md:flex-row user-dashboard">
            <div class="left-side-bar w-full md:w-2/12 sticky top-0 h-fit md:h-screen bg-white">
                <ul class="w-full px-2 py-4 md:py-8 flex gap-4 flex-row md:flex-col flex-wrap">
                    <li v-for="dsi in userDashboardSidebar" v-on:click.prevent="elementStore.changeDSID(dsi.id)"
                        class="border-1 border-teal-950 flex justify-start items-center gap-2 p-0 md:p-2 cursor-pointer">
                        <Icon v-bind:name="dsi.name" size="20" />
                        <p class="capitalize">{{ dsi.text }}</p>
                    </li>
                </ul>
            </div>
            <div class="content w-full md:w-10/12">
                <div class="selected-item pt-4 md:pt-8 px-0 md:px-4" v-if="selectedDSID === 1">
                    <h2>Profile</h2>
                    <!-- Update Profile -->
                    <!-- Change address  -->
                    <!-- Change phone number  -->
                    <UserDetail v-bind:userInfo="userInfo" />
                </div>
                <div class="selected-item pt-4 md:pt-8 px-0 md:px-4" v-else-if="selectedDSID === 2">
                    <h2>Order</h2>
                    <!-- <OrderDetail /> -->
                    <OrderList />
                </div>
                <div class="selected-item pt-4 md:pt-8 px-0 md:px-4" v-else-if="selectedDSID === 3">
                    <h2 >Address Book <span class="float-right text-lg cursor-pointer" v-on:click="addNewAddressComp" >Add New
                            <Icon name="ep:plus" size="20" color="blue" />
                        </span> </h2>
                    <AddressList v-bind:userInfo="userInfo" v-if="showAddressList === true" />
                    <AddressAddUpdate v-else />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';

import useUserStore from '../../stores/UserStore';
import useElementStore from '../../stores/ElementsStore';
import useOrderStore from '../../stores/OrderStore';

// Meta
definePageMeta({
  middleware: ["auth"]
  // or middleware: 'auth'
});

const userStore = useUserStore();
const elementStore = useElementStore();
const orderStore = useOrderStore();

const { userInfo } = storeToRefs(userStore);
const { userDashboardSidebar, selectedDSID, addAddress, showAddressList } = storeToRefs(elementStore);

const accessToken = useCookie(ACCESS_TOKEN);
if (!accessToken.value) {
    console.error('There is no access token');

}

if (accessToken.value) {
    await orderStore.fetchOrders(accessToken.value);
}

const addNewAddressComp=()=>{
    elementStore.setAddUpdateAddress(true);
    elementStore.setShowAddOrAddress(false);
}


</script>

<style lang="scss" scoped></style>