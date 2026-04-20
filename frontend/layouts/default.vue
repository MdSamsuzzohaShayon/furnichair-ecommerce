<template>
    <div>
        <div v-on:click="wrapperHandler">
            <header class="shadow-sm bg-white">
                <div class="bottom-main-menu container mx-auto px-2 py-6 flex justify-between">
                    <div class="block md:hidden cursor-pointer w-1/3">
                        <Icon name="grommet-icons:menu" size="20" v-on:click.prevent="elementsStore.openMobileMenu()"
                            ref="sidebarOpenSvgEl" id="menu-open-btn" />
                    </div>
                    <nav class="w-4/5 md:w-1/3 fixed md:static left-0 top-0 z-20 md:z-0 md:block items-start justify-between bg-white"
                        :class="showMobileMenu ? 'flex' : 'hidden md:flex'" ref="sidebarDivEl">
                        <ul
                            class="flex justify-start list-none flex-col md:flex-row bg-white h-screen md:h-fit w-fit md:w-full px-4 py-8 md:p-0 gap-4 md:gap-1">
                            <li class="mr-4 cursor-pointer font-semibold" v-for="menu in menus"
                                v-on:click.prevent="elementsStore.closeMobileMenu()">
                                <NuxtLink v-bind:to="menu.link" class="capitalize">{{ menu.text }}</NuxtLink>
                            </li>
                        </ul>
                        <div class="close-button block md:hidden w-fit  px-4 py-8 cursor-pointer"
                            v-on:click="mobileMenuCloseHandler">
                            <Icon name="grommet-icons:close" size="20" />
                        </div>
                    </nav>
                    <div class="flex justify-center w-1/3">
                        <NuxtLink to="/"><img v-bind:src="logoUrl" alt="" class="h-8"></NuxtLink>
                    </div>
                    <nav class="w-1/3">
                        <ul class="flex justify-end list-none">
                            <li v-for="rm in rightMenus" class="ml-4 cursor-pointer">
                                <Icon v-bind:name="rm.name" size="20" v-bind:color="rm.color" v-if="rm.id === 1"
                                    v-on:click.prevent="displaySearchBarHandler" id="search-btn" />
                                <NuxtLink v-bind:to="rm.link" v-else-if="rm.id === 2" class="cursor-pointer">
                                    <Icon v-bind:name="rm.name" size="20" v-bind:color="rm.color" />
                                </NuxtLink>
                                <NuxtLink to="/admin/" v-else-if="rm.id === 3 && userInfo.is_staff">
                                    <Icon v-bind:name="rm.name" size="20" v-bind:color="rm.color" />
                                </NuxtLink>
                                <NuxtLink v-bind:to="rm.link" v-else-if="rm.id === 3">
                                    <Icon v-bind:name="rm.name" size="20" v-bind:color="rm.color" />
                                </NuxtLink>
                                <Icon v-bind:name="rm.name" size="20" v-bind:color="rm.color"
                                    v-else-if="rm.id === 4 && isAuthenticated === true" v-on:click.prevent="logoutHandler" />
                            </li>
                        </ul>
                    </nav>
                </div>
                <div class="search-bar-menu bg-white text-teal-950 absolute top-0 left-0 w-full z-20"
                    v-if="showSearchBar === true">
                    <div class="container mx-auto px-2 py-6 flex justify-between items-center">
                        <form class="flex items-center justify-center" v-on:submit.prevent="searchHandler">
                            <button type="submit" class="px-4">
                                <Icon size="20" name="simple-line-icons:magnifier" class="text-teal-950" />
                            </button>
                            <input type="text" id="search-text" class="bg-real-100 text-teal-950 outline-0 text-3xl capitalize"
                                placeholder="Search...." ref="searchInputEl" v-model="state.q">
                        </form>
                        <div class="close-button">
                            <Icon name="grommet-icons:close" size="20" class="text-teal-950"
                                v-on:click.prevent="elementsStore.setShowSearchBar(false)" />
                        </div>
                    </div>
                </div>
            </header>

            <div class="whole-display-overflow absolute h-full w-full bg-teal-950 z-10 opacity-70 left-0 top-0 "
            v-bind:class="shadowOverflow ? 'block' : 'hidden'"></div>


            <slot />

            <footer class="bg-teal-950 text-teal-50 mt-8">
                <div class="container mx-auto px-2 flex justify-between items-center flex-col md:flex-row py-8 gap-4">
                    <div class="newsletter w-full md:w-1/4">
                        <p>Subscribe to get special offers, free giveaways, and once-in-a-lifetime deals.</p>
                        <form v-on:submit.prevent="subscribeSubmitHandler">
                            <div class="input-group w-full flex items-center">
                                <div
                                    class="icon-holder bg-teal-900 outline-0 py-2 border-y border-teal-100/25 text-teal-50 placeholder:text-teal-100/50 w-1/12 text-center">
                                    <Icon name="material-symbols:mail-outline" color="white" size="20" />
                                </div>
                                <input required="true" type="email" id="user-first-name"
                                    class="bg-teal-900 outline-0 px-3 py-2 border-y border-teal-100/25 px-1 text-teal-50 placeholder:text-teal-100/50 w-10/12"
                                    placeholder="Enter your email" v-on:change="wishlistEmailChangeHandler">
                                <button
                                    class="icon-holder bg-teal-900 outline-0 py-2 border-y border-teal-100/25 text-teal-50 placeholder:text-teal-100/50 w-1/12"
                                    type="submit">
                                    <Icon name="mdi-light:arrow-right-circle" color="white" class="p-0" size="20" />
                                </button>
                            </div>
                        </form>
                    </div>
                    <div class="middle-social-menu border-0 md:border-b border-teal-90 w-full md:w-1/4">
                        <div class="container mx-auto px-2 py-2">
                            <ul class="flex justify-start">
                                <li v-for="link in socialLinks">
                                    <NuxtLink v-bind:to="link.link">
                                        <Icon v-bind:name="link.name" size="20" color="white" />
                                    </NuxtLink>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="address w-full md:w-1/4">
                        <p v-for="a in address" v-bind:key="a.id">{{ a.name }} : {{ a.value }}</p>
                    </div>
                </div>
            </footer>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useElementsStore from '@/stores/ElementsStore';
import useSettingsStore from '@/stores/SettingsStore';
import useUserStore from '@/stores/UserStore';
import useCategoryStore from '@/stores/CategoryStore';
import useWishlistStore from '@/stores/WishlistStore';

const elementsStore = useElementsStore();
const categoryStore = useCategoryStore();
const settingsStore = useSettingsStore();
const userStore = useUserStore();
const wishlistStore = useWishlistStore();


const searchInputEl = ref<HTMLInputElement | null>(null);
const sidebarDivEl = ref<HTMLDivElement | null>(null);
const sidebarOpenSvgEl = ref<HTMLOrSVGElement | null>(null);
const state = reactive({ q: null });

defineExpose({ searchInputEl });
let refreshTokenCycle: any = null;

const { menus, rightMenus, shadowOverflow, showMobileMenu, showSearchBar } = storeToRefs(elementsStore);
const { logoUrl, socialLinks, address } = storeToRefs(settingsStore);
const { isAuthenticated, userInfo } = storeToRefs(userStore);
const { wishlistEmailAdd } = storeToRefs(wishlistStore);



const wrapperHandler = (e: Event) => {


    // if (!e.target) return;
    // if (!shadowOverflow.value) return;
    // const clickedEl: HTMLElement = e.target as HTMLElement;
    // const exceptElIds: string[] = ["menu-open-btn", "search-btn"];
    // if (clickedEl.id && exceptElIds.includes(clickedEl.id)) return;


    // if (!sidebarDivEl.value) return;
    // const withinBoundary = e.composedPath().includes(sidebarDivEl.value);
    // if (!withinBoundary) {
    //     elementsStore.closeMobileMenu();
    //     elementsStore.closeFilterBar();
    //     elementsStore.setShadowOverflow(false);
    // }

    // if (showSearchBar.value || showMobileMenu.value){
    //     elementsStore.setShadowOverflow(true);
    // }

}


const mobileMenuCloseHandler = (e: Event) => {
    console.log(e);
    elementsStore.closeMobileMenu();
}

// Show or hide elements
const displaySearchBarHandler = (e: Event) => {
    elementsStore.setShowSearchBar(true);
    // showSearchBar.value = !showSearchBar.value;
    setTimeout(() => {
        if (searchInputEl.value) {
            searchInputEl.value.focus()
        }
    }, 500);
}

const logoutHandler = async (e: Event) => {
    const token = useCookie('token');
    token.value = null;
    userStore.setIsAuthenticated(false);
    await navigateTo('/');
}


const searchHandler = async (e: Event) => {
    showSearchBar.value = !showSearchBar.value;
    elementsStore.setShowSearchBar(false);
    await navigateTo(`/search/?q=${state.q}`);
}


const subscribeSubmitHandler = async (e: Event) => {
    e.preventDefault();
    console.log("Submit - 1");
    const { data: userInfo, error: userError, refresh: refreshRequest, status: userStatus } = await useFetch(`${BACKEND_URL}/wishlist/new/`, {
        key: `wishlist-${new Date().getSeconds()}${new Date().getMilliseconds()}`,
        method: 'POST',
        body: {
            email: wishlistEmailAdd.value
        }
    });


    if (userStatus.value === 'success' && userInfo.value) {
        const formElement = e.target as HTMLFormElement;
        formElement.reset();
        wishlistStore.setWishlistEmailAdd('');
    }
}



const wishlistEmailChangeHandler = (e: Event) => {
    const inputEl = e.target as HTMLInputElement;
    wishlistStore.setWishlistEmailAdd(inputEl.value);
}







onMounted(async () => {
    const token = useCookie("token");

    const fetchAtBeginning = []
    if (!token || !token.value) {
        userStore.setIsAuthenticated(false);
    } else {
        userStore.setIsAuthenticated(true);
        const userInfo = localStorage.getItem('userInfo');
        if (userInfo) userStore.setUserInfo(JSON.parse(userInfo));

        // @ts-ignore
        const { access: accessBefore, refresh: refreshBefore } = token.value;

        if (accessBefore && refreshBefore) {
            await userStore.setRefreshToken(refreshBefore);
            const tokenUpdate = useCookie("token");
            // @ts-ignore
            const { access: accessAfter, refresh: refreshAfter } = tokenUpdate.value;
            fetchAtBeginning.push(userStore.fetchUser(accessAfter));

            // Refresh token in every 9 minuts
            refreshTokenCycle = setInterval(async () => {
                await userStore.setRefreshToken(refreshBefore);
            }, TOKEN_REFRESH_TIME);
        }
    }
    fetchAtBeginning.push(categoryStore.fetchCategories());
    await Promise.all(fetchAtBeginning);

});

onUnmounted(() => {
    console.log("Unmount default layout ", refreshTokenCycle);

    if (refreshTokenCycle) {
        clearInterval(refreshTokenCycle);
    }
});

</script>