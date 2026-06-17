<template>
    <div>
        <h3 class="mt-4">{{ addAddress ? 'New Address' : 'Update Address' }}</h3>
        <form class="flex flex-col gap-4 mt-8" v-on:submit.prevent="addressAddUpdateHandler">
            <div class="input-group w-full">
                <input required="true" type="text" id="user-area"
                    class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                    placeholder="Area" v-model="userAddressAddOrUpdate.area">
            </div>
            <div class="input-group w-full">
                <input required="true" type="text" id="user-city"
                    class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                    placeholder="City" v-model="userAddressAddOrUpdate.city">
            </div>
            <div class="input-group flex justify-between gap-4">
                <input required="true" type="text" id="user-country"
                    class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                    placeholder="Country" v-model="userAddressAddOrUpdate.country">
            </div>
            <div class="input-group flex justify-between gap-4">
                <input required="true" type="number" id="user-country"
                    class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50 remove-arrow"
                    placeholder="Phone" v-model="userAddressAddOrUpdate.phone">
            </div>
            <div class="input-group w-full">
                <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold"
                    type="submit">{{ addAddress ? 'Add' : 'Update' }}</button>
            </div>
        </form>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useUserStore from '@/stores/UserStore';
import useElementsStore from '@/stores/ElementsStore';

const userStore = useUserStore();
const elementStore = useElementsStore();

const { userAddressAddOrUpdate, userInfo } = storeToRefs(userStore);
const { addAddress } = storeToRefs(elementStore);

const addressAddUpdateHandler = async (e: Event) => {
    // console.log({ ...userAddressAddOrUpdate.value });
    const accessToken = useCookie(ACCESS_TOKEN);
    if (!accessToken.value) {
        console.error('There is no access token');
        return;

    }

    const organizeData = {
        address: { ...userAddressAddOrUpdate.value }
    }
    const tokenVal = accessToken.value;
    const userId = userInfo.value.id;
    const { data: updateAddress, error: errorFetch, status } = await useFetch(`${BACKEND_URL}/accounts/${userInfo.value.id}/update/`, {
        method: "PUT",
        headers: {
            "Authorization": `Bearer ${accessToken.value}`
        },
        body: organizeData
    });
    if (status.value === 'success' && updateAddress.value) {
        userStore.setUserNewAddress(userAddressAddOrUpdate.value)
        elementStore.setShowAddOrAddress(true);
    } else {
        console.log(errorFetch.value);
    }

}

</script>

<style scoped></style>