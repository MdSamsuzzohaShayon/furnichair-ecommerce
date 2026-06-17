<template>
    <div>
        <div class="item mt-4 w-full bg-white" v-for="a in userInfo.address">
            <div class="p-4 flex justify-between items-center">
                <div class="text-detail">
                    <p>ID: {{ a.id }}</p>
                    <p>Area: {{ a.area }}, City: {{ a.city }}</p>
                    <p>Country: {{ a.country }}, Phone: {{ a.phone }}</p>
                </div>
                <div class="contaoller">
                    <p class="cursor-pointer text-teal-900" v-on:click.prevent="selectAddressToUpdate(a.id)">Update</p>
                    <p class="cursor-pointer text-red-900">Delete</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import useElementsStore from '@/stores/ElementsStore';
import useUserStore from '@/stores/UserStore';
const { userInfo } = defineProps(['userInfo']);

const elementStore = useElementsStore();
const userStore = useUserStore();

const selectAddressToUpdate = (addressId: number) => {
    if (!addressId) return;
    userStore.setUserAddressAddOrUpdate(addressId);
    elementStore.setAddUpdateAddress(false);
    elementStore.setShowAddOrAddress(false);
}

</script>

<style scoped></style>