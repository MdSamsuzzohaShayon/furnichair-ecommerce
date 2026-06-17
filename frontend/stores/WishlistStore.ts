import { defineStore } from "pinia";
import type { WishlistInterface } from "@/types/WishlistType";

const useWishlistStore = defineStore('wishlistStore', {
    state: () => ({
        wishlistList: [] as WishlistInterface[],
        wishlistEmailAdd: '' as string,
    }),
    actions: {
        setWishlistEmailAdd(emailAddress: string){
            this.wishlistEmailAdd = emailAddress;
        },
        deleteWishlist(catId: number) {
            this.wishlistList = this.wishlistList.filter((c: WishlistInterface) => c.id !== catId);
        },
        async fetchWishlist(accessToken: string) {
            const { data: wishlistData, refresh: refreshRequest, status: wishlistStatus } = await useFetch<WishlistInterface[]>(`${BACKEND_URL}/wishlist/list/`, {
                key: `wishlist-${new Date().getSeconds()}-${new Date().getMilliseconds()}`,
                headers: {
                    "Authorization": `Bearer ${accessToken}`
                }
            });
            if (wishlistStatus.value === 'success' && wishlistData.value) {
                this.wishlistList = wishlistData.value;
            }

        },
    }
});


export default useWishlistStore;