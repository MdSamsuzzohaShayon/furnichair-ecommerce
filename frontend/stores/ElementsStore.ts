import { defineStore } from "pinia";
import type { MenuInterface, RightMenuInterface, SidebarMenuInterface } from "@/types/ElementsSettingType";

const useElementStore = defineStore("elementsStore", {
    state: () => ({
        menus: [
            { id: 1, text: 'Home', link: "/" },
            { id: 1, text: 'Product', link: "/products" },
            { id: 2, text: 'About', link: "/about" },
            { id: 3, text: 'Contact', link: "/contact" },
            { id: 3, text: 'Policy', link: "/policy" },
        ] as MenuInterface[],
        rightMenus: [
            { id: 1, name: "simple-line-icons:magnifier", text: "Search", color: 'black', link: '#' },
            { id: 2, name: "simple-line-icons:basket", text: "Cart", color: 'black', link: '/cart' },
            { id: 3, name: "simple-line-icons:user", text: "User Account", color: 'black', link: '/user/signin' },
            { id: 4, name: "heroicons-solid:arrow-right-on-rectangle", text: "Logout", color: 'black', link: '#' },
        ] as RightMenuInterface[],
        dashboardSidebar: [
            { id: 1, name: "bx:box", text: "Product" },
            { id: 2, name: "simple-line-icons:grid", text: "Category" },
            { id: 3, name: "material-symbols:local-shipping-outline-sharp", text: "Delivery" },
            { id: 4, name: "et:gears", text: "Setting" },
            { id: 5, name: "simple-line-icons:handbag", text: "Order" },
            { id: 6, name: "la:clipboard-list", text: "Wishlist" },
            { id: 7, name: "simple-icons:minutemailer", text: "Inbox" },
            { id: 8, name: "simple-line-icons:user", text: "User" },
        ] as SidebarMenuInterface[],
        userDashboardSidebar: [
            { id: 1, name: "simple-line-icons:user", text: "Profile" },
            { id: 2, name: "simple-line-icons:handbag", text: "Order" },
            { id: 3, name: "simple-line-icons:user", text: "Address" },
        ] as SidebarMenuInterface[],
        selectedDSID: 1 as number, // DSI = Dashboard Sidebar ID
        errorMessageList: [] as string[],
        successMessageList: [] as string[],
        isLoading: false as boolean,
        
        // Menus with shadow
        shadowOverflow: false as boolean,
        showFilter: false as boolean,
        showMobileMenu: false as boolean,
        showSearchBar: false as boolean,

        // User Dashboard
        addAddress: false as boolean,
        showAddressList: true as boolean,
        addProduct: false as boolean,
        showProductList: true as boolean,
    }),
    actions: {
        openFilterBar() {
            this.showFilter = true;
            this.shadowOverflow = true;
        },
        closeFilterBar() {
            this.showFilter = false;
            this.shadowOverflow = false;
        },
        openMobileMenu() {
            this.showMobileMenu = true;
            this.shadowOverflow = true;
        },
        closeMobileMenu() {
            this.showMobileMenu = false;
            this.shadowOverflow = false;
        },
        setShowSearchBar(show: boolean){
            this.showSearchBar = show;
            this.shadowOverflow = show;
        },
        setShadowOverflow(overflow: boolean) {
            this.shadowOverflow = overflow;
        },
        setErrorMessageList(messageList: string[]) {
            this.errorMessageList = messageList;
        },
        resetErrorMessageList() {
            this.errorMessageList = [];
        },
        setSuccessMessageList(messageList: string[]) {
            this.successMessageList = messageList;
        },
        resetSuccessMessageList() {
            this.successMessageList = [];
        },
        changeDSID(newDSID: number) {
            this.selectedDSID = newDSID;
        },

        // User dashboard and admin panel
        setAddUpdateAddress(addAddress: boolean) {
            this.addAddress = addAddress;
        },
        setShowAddOrAddress(showAddressList: boolean) {
            this.showAddressList = showAddressList;
        },
        setAddProduct(addProduct: boolean) {
            this.addProduct = addProduct;
        },
        setShowProductList(showProductList: boolean) {
            this.showProductList = showProductList;
        },
    }
});

export default useElementStore;