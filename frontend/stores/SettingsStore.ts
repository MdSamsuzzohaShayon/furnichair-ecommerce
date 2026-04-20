import { defineStore } from "pinia";
import type { SocialLinkInterface, NewArrivalInterface, AddressInterface, AdvantagesInt } from "@/types/SiteSettingsType";
import type { ProductInterface } from '@/types/ProductType';

const useSettingsStore = defineStore('settingsStore', {
    state: () => ({
        socialLinks: [
            { id: 1, name: "bxl:facebook", color: 'black', link: '#' },
            { id: 2, name: "bxl:twitter", color: 'black', link: '#' },
            { id: 3, name: "bxl:instagram", color: 'black', link: '#' },
        ] as SocialLinkInterface[],
        logoUrl: "/logo.png" as string,
        siteTitle: "Shakil Furniture",
        siteDesc: "Discover a world of exquisite furniture where style meets functionality. Elevate your living spaces with our curated collection of timeless pieces, designed to transform your house into a home.",
        newArrivals: [
            { id: 1, title: "Product 1", category: 1, description: "Desc", image1: "/img/bg-1.jpg" },
            { id: 2, title: "Product 2", category: 2, description: "Desc", image1: "/img/bg-2.jpg" },
            { id: 3, title: "Product 3", category: 1, description: "Desc", image1: "/img/bg-3.jpg" },
        ] as NewArrivalInterface[],
        address: [
            { id: 1, name: "Area", value: "Sher-E-Bangla Stadium, Mirpur" },
            { id: 2, name: "City", value: "Dhaka" },
            { id: 3, name: "Phone", value: "0178346734643" },
            { id: 4, name: "Email", value: "admin@shakilfurniture.com" },
        ] as AddressInterface[],
        advantages: [
            {id: 1, title: "Returns & Warranty", desc: "Shakil Furniture provides an easy, hassle-free servicing system where we pick up your product from your home if there is any problem and get it back to you.", icon: "mdi:account-reactivate-outline"},
            {id: 2, title: "EMI Policy", desc: "To avail EMI, Place your order through Website and share your order ID in our Inbox. We will share the EMI payment link.", icon: "la:truck-loading"},
            {id: 3, title: "Free Delivery", desc: "FREE home delivery with assembling inside Dhaka within 3 days and 5-7 days anywhere in Bangladesh. Inside Dhaka City, we offer free home delivery to the ground floor through courier.", icon: "fluent-mdl2:feedback-response-solid"},
        ] as AdvantagesInt[],
        trustedCompanyLogos: [
            '10_Minute_School.png',
            'brac.png',
            'lankabangla.png',
            'shop-up.png',
            'Standard_Chartered.png',
        ] as string[],
        featuredProductList: [] as ProductInterface[],
        selectedProductId: 1 as number,
        heightProductPrice: 10000 as number,
    }),
    actions: {
        setFeaturedProducts(productList: ProductInterface[]) {
            this.featuredProductList = productList;
        },
        changeSliderItem(isLeft: boolean) {
            const findProductIndex = this.newArrivals.findIndex(((p: NewArrivalInterface) => p.id === this.selectedProductId))
            // console.log(findProductIndex);
            if (findProductIndex === 0 || findProductIndex) {
                let changedProductIndex = isLeft ? findProductIndex + 1 : findProductIndex - 1
                if (changedProductIndex < 0) {
                    changedProductIndex = this.newArrivals.length - 1
                } else if (changedProductIndex >= this.newArrivals.length) {
                    changedProductIndex = 0;
                }
                this.selectedProductId = this.newArrivals[changedProductIndex].id
                // console.log(this.selectedProductId)
            }
        }
    }
});

export default useSettingsStore;