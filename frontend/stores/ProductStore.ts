// const { data: products } = await useFetch('http://localhost:8000/api/products/');
import { defineStore } from "pinia";
import type { ProductInterface, ProductFilterInterface, ProductFilterOptionalInterface, ProductAddUpdateInterface, CartItemInterface } from '@/types/ProductType';


const initialProductUpdateAdd: ProductAddUpdateInterface = {
    title: '',
    price: null,
    discount_price: null,
    total_stock: null,
    description: '',
    category: 1,
};

const useProductStore = defineStore('productStore', {
    state: () => ({
        productList: [] as ProductInterface[],
        productFilter: {
            title: null,
            price: '1200',
            total_stock: null,
            category: null
        } as ProductFilterInterface,
        productUpdateAdd: initialProductUpdateAdd as ProductAddUpdateInterface,
        productSingle: {} as ProductInterface,
        productUpdate: false as boolean,
        // selectProductToUpdate: {} as ProductInterface,
        // productPropsToUpdate: {}

        // Cart
        cartList: [] as CartItemInterface[]
    }),
    actions: {
        setProductUpdate(update: boolean) {
            this.productUpdate = update;
        },
        setProductToUpdate(pId: number) {
            const findProduct = this.productList.find((p: ProductInterface) => p.id === pId);
            if (findProduct) {
                // @ts-ignore
                this.productUpdateAdd = findProduct;
            }
        },
        resetProductUpdateAdd() {
            this.productUpdateAdd = initialProductUpdateAdd;
        },
        addNewProduct(newProduct: ProductInterface) {
            this.productList.push(newProduct);
        },
        setUpdateProduct(pId: number) {
            const findProductIndex = this.productList.findIndex((p: ProductInterface) => p.id === pId);
            // When specific item is not found
            if (findProductIndex === -1) {
                return;
            }
            // update object
            const updatedObj = { ...this.productList[findProductIndex], ...this.productUpdateAdd };
            // @ts-ignore
            this.productList[findProductIndex] = updatedObj;
        },
        addItemToCart(cartItem: CartItemInterface) {
            const prevCart = window.localStorage.getItem("cart");
            let cartObj = []
            if (prevCart) {
                cartObj = JSON.parse(prevCart);
            }
            cartObj.push(cartItem);
            window.localStorage.setItem('cart', JSON.stringify(cartObj));
            this.cartList = cartObj;
        },
        removeItemFromCart(cId: string) {
            const prevCart = window.localStorage.getItem("cart");
            let cartObj: CartItemInterface[] = []
            if (prevCart) {
                cartObj = JSON.parse(prevCart);
            }
            cartObj = cartObj.filter((c: CartItemInterface) => c.id !== cId);
            window.localStorage.setItem('cart', JSON.stringify(cartObj));
            this.cartList = cartObj;
        },
        fetchCartFromLocalStorage() {
            const prevCart = window.localStorage.getItem('cart');
            if (prevCart) {
                this.cartList = JSON.parse(prevCart);
            }
        },
        async fetchSingleProduct(pId: number) {
            let url = `${BACKEND_URL}/products/${pId}`;
            const { data: products, status: productStatus, refresh: refreshFetch } = await useFetch<ProductInterface>(url, { key: pId + "" });
            if (productStatus.value === 'success' && products.value) {
                this.productSingle = products.value;
            } else {
                // @ts-ignore
                throw createError({ statusCode: 404, statusMessage: "Product not found", fetal: true });
            }
        },
        async fetchProducts(q: string | null = null) {
            let url = `${BACKEND_URL}/products/`;
            if (q !== null && q !== '') {
                url += `?search=${q}`;
            }
            const { data: products, status: productStatus, refresh: refreshFetch } = await useFetch<ProductInterface[]>(url);
            await refreshFetch();
            if (productStatus.value === 'success' && products.value) {
                this.productList = products.value;
            }
        },
        async fetchFilteredProducts(url: string) {
            const { data: products } = await useFetch<ProductInterface[]>(url);
            if (products.value) {
                this.productList = products.value;
            }
        },

        async fetchProductsByCategory(catId: number) {
            const { data: products } = await useFetch<ProductInterface[]>(`${BACKEND_URL}/products/categories/${catId}`);
            if (products.value) {
                this.productList = products.value;
            }
        },
    },
    getters: {
        getCartById(state) {
            // return (userId) => state.users.find((user) => user.id === userId)
            return (cId: string) => state.cartList.find((c) => c.id === cId);
        },
        sereliazedProductFilter(state): ProductFilterOptionalInterface {
            const newObj: ProductFilterOptionalInterface = {}
            // state.productFilter
            if (state.productFilter.title && state.productFilter.title !== 'null' && state.productFilter.title !== '') {
                newObj.title = state.productFilter.title.toString();
            }
            if (state.productFilter.price && state.productFilter.price !== 'null' && state.productFilter.price !== '') {
                newObj.price = parseInt(state.productFilter.price, 10);
            }
            if (state.productFilter.total_stock !== null || state.productFilter.total_stock !== 'null' || state.productFilter.total_stock !== '') {
                if (state.productFilter.total_stock === '1') {
                    newObj.total_stock = 1;
                } else if (state.productFilter.total_stock === '0') {
                    newObj.total_stock = 0
                }
            }
            return newObj;
        }
    }
});


export default useProductStore;