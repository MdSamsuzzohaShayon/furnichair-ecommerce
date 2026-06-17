<template>
    <div>
        <!-- <h1>Wishlist List</h1> -->
        <!-- wishlistList -->
        <table class="w-full mt-4">
            <thead>
                <tr>
                    <th class="p-2 text-center border border-teal-900">ID</th>
                    <th class="p-2 text-center border border-teal-900">Email</th>
                    <th class="p-2 text-center border border-teal-900">Date</th>
                    <th class="p-2 text-center border border-teal-900">Perform</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="wishlist in wishlistList">
                    <td class="p-2 text-center border border-teal-900/50">{{ wishlist.id }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ wishlist.email }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ isoToDate(wishlist.created_at) }}</td>
                    <td class="p-2 text-center border border-teal-900/50">
                        <Icon class="pr-2" size="20" name="lucide:trash-2" color="red"
                            v-on:click.prevent="deleteWishlistHandler(wishlist.id)" />
                        <!-- <NuxtLink v-bind:to="`/wishlists/${wishlist.id}`">
                            <Icon class="pr-2" size="20" name="bytesize:eye" color="teal" />
                        </NuxtLink> -->
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';

import useWishlistStore from '@/stores/WishlistStore';

const wishlistStore = useWishlistStore();

const { wishlistList } = storeToRefs(wishlistStore);

const deleteWishlistHandler = (pId: number | null) => {
    console.log("Delete wishlist -> ", pId);
}


const accessToken = useCookie(ACCESS_TOKEN);
if (!accessToken.value) {
    console.error('There is no access token');

}
if (accessToken.value) {

    await wishlistStore.fetchWishlist(accessToken.value);


}


</script>

<style scoped></style>