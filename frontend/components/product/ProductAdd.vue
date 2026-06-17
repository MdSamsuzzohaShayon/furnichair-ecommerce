<template>
    <div class="container mx-auto px-2">
        <!-- <h3>{{ productUpdate ? 'Product update' : 'Product add' }}</h3> -->
        <form class="flex flex-col gap-4 mt-4" v-on:submit.prevent="productAddHandler">
            <div class="input-group w-full">
                <input v-bind:required="productUpdate === false ? true : false" type="text" id="product-title"
                    class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                    placeholder="Title" v-model="productUpdateAdd.title">
            </div>
            <div class="input-group w-full">
                <input v-bind:required="productUpdate === false ? true : false" type="number" id="product-price"
                    class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50 remove-arrow"
                    placeholder="Price" v-model="productUpdateAdd.price">
            </div>
            <div class="input-group w-full">
                <input v-bind:required="productUpdate === false ? true : false" type="number"
                    id="product-discount_price"
                    class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50 remove-arrow"
                    placeholder="Discount Price" v-model="productUpdateAdd.discount_price">
            </div>
            <div class="input-group w-full">
                <input v-bind:required="productUpdate === false ? true : false" type="number" id="product-total_stock"
                    class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50 remove-arrow"
                    placeholder="Total Stock" v-model="productUpdateAdd.total_stock">
            </div>
            <div class="input-group w-full">
                <textarea v-bind:required="productUpdate === false ? true : false" type="number"
                    id="product-description"
                    class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                    placeholder="Description" v-model="productUpdateAdd.description" cols="3" />
            </div>

            <!-- Category  -->
            <div class="input-group w-full">
                <label for="product-category" class="text-teal-950/50">Category</label>
                <select id="product-category" v-model="productUpdateAdd.category"
                    class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50">
                    <option v-for="category in categoryList" v-bind:value="category.id">{{ category.name }}</option>
                </select>
            </div>

            <!-- images  -->
            <div class="input-group w-full">
                <label for="product-image1"
                    class="w-full bg-white text-teal-950/50  px-3 py-2 border border-teal-950/25 block"> <span>
                        <Icon name="ph:image" size="20" />
                    </span> {{ state.image1Name !== '' ? state.image1Name : 'Image 1' }}</label>
                <input v-bind:required="productUpdate === false ? true : false" type="file" id="product-image1"
                    name="image1file" ref="uploadImage1" class="hidden" v-on:input="uploadFileChangeHandler">
            </div>
            <div class="input-group w-full">
                <label for="product-image2"
                    class="w-full bg-white text-teal-950/50  px-3 py-2 border border-teal-950/25 block"> <span>
                        <Icon name="ph:image" size="20" />
                    </span> {{ state.image2Name !== '' ? state.image2Name : 'Image 2' }}</label>
                <input type="file" id="product-image2" name="image2file" ref="uploadImage2" class="hidden"
                    v-on:input="uploadFileChangeHandler">
            </div>
            <div class="input-group w-full">
                <label for="product-image3"
                    class="w-full bg-white text-teal-950/50  px-3 py-2 border border-teal-950/25 block"> <span>
                        <Icon name="ph:image" size="20" />
                    </span> {{ state.image3Name !== '' ? state.image3Name : 'Image 3' }}</label>
                <input type="file" id="product-image3" name="image3file" ref="uploadImage3" class="hidden"
                    v-on:input="uploadFileChangeHandler">
            </div>
            <div class="input-group w-full">
                <label for="product-image4"
                    class="w-full bg-white text-teal-950/50  px-3 py-2 border border-teal-950/25 block"> <span>
                        <Icon name="ph:image" size="20" />
                    </span> {{ state.image4Name !== '' ? state.image4Name : 'Image 4' }}</label>
                <input type="file" id="product-image4" name="image4file" ref="uploadImage4" class="hidden"
                    v-on:input="uploadFileChangeHandler">
            </div>
            <!-- <div class="input-group w-full">
                <input v-bind:required="productUpdate === false ? true : false" type="file" id="product-image4"
                    name="image4" ref="uploadImage4"
                    class="file:bg-white file:text-teal-950/50 file:outline-0 file:px-3 file:py-2 file:border-0 file:border-teal-950/25 w-full placeholder:text-teal-950/50  bg-white text-teal-950/50 outline-0 border border-teal-950/25 w-full placeholder:text-teal-950/50"
                    placeholder="Image 1" v-on:change="uploadFileChangeHandler">
            </div> -->


            <!-- Submit  -->
            <div class="input-group w-full">
                <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold"
                    type="submit">
                    {{ productUpdate ? 'Update' : 'Add' }}</button>
                <button class="bg-red-900 text-red-50 border-1 border-red-950 px-5 py-2 w-full font-bold mt-4"
                    v-on:click.prevent="cancelHandler"> Cancel</button>
            </div>
        </form>
        <p class="text-red-900 px-4 py-2 capitalize" v-for="message in errorMessageList">{{ message }}</p>
        <p class="text-teal-900 px-4 py-2 capitalize" v-for="message in successMessageList">{{ message }}</p>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useElementStore from '@/stores/ElementsStore';
import useProductStore from '@/stores/ProductStore';
import useCategoryStore from '@/stores/CategoryStore';
import type { ProductInterface } from '@/types/ProductType';
import { BACKEND_URL } from '@/utils/keys';

const uploadImage1 = ref(null);
const uploadImage2 = ref(null);
const uploadImage3 = ref(null);
const uploadImage4 = ref(null);
const state = reactive({
    image1Name: '',
    image2Name: '',
    image3Name: '',
    image4Name: '',
});

const elementStore = useElementStore();
const productStore = useProductStore();
const categoryStore = useCategoryStore();

const { errorMessageList, successMessageList } = storeToRefs(elementStore);
const { productUpdateAdd, productUpdate } = storeToRefs(productStore);
const { categoryList } = storeToRefs(categoryStore);

// Form data
const formData = new FormData();


const uploadFileChangeHandler = (e: Event) => {
    const fileInput = e.target as HTMLInputElement;
    // @ts-ignore
    state[`${fileInput.name}Name`] = fileInput.files[0].name;
    if (fileInput.files) {
        formData.set(fileInput.name, fileInput.files[0]);
    }
}

const cancelHandler = (e: Event) => {
    elementStore.setShowProductList(true);
}

const productAddHandler = async (e: Event) => {
    elementStore.resetErrorMessageList();
    elementStore.resetSuccessMessageList();

    const newObj: any = { ...productUpdateAdd.value };
    if (newObj.image1) delete newObj.image1;
    if (newObj.image2) delete newObj.image2;
    if (newObj.image3) delete newObj.image3;
    if (newObj.image4) delete newObj.image4;

    for (const [k, v] of Object.entries(newObj)) {
        // @ts-ignore
        formData.set(k, v);
    }
    // @ts-ignore
    // for (const pair of formData.entries()) {
    //     console.log(`${pair[0]}, ${pair[1]}`);
    // }

    const accessToken = useCookie(ACCESS_TOKEN);

    if (!accessToken.value) {
        console.error('There is no access token');
        return;

    }

    // if(!userInfo.value.address){
    //     console.error("No address found");

    //     return;
    // }

    // /products/1/update/ 
    let url = `${BACKEND_URL}/products/new/`;
    let method: "POST" | "PUT" = "POST"
    if (productUpdate.value === true) {
        url = `${BACKEND_URL}/products/${productUpdateAdd.value.id}/update/`;
        method = 'PUT';
    }
    const { data, pending, error, refresh, status } = await useFetch<ProductInterface>(url, {
        method: method,
        body: formData,
        headers: {
            "Authorization": `Bearer ${accessToken.value}`
        }
    });
    // console.log({ data: data.value, pending: pending.value, error: error.value, refresh: refresh, status: status.value });
    if (status.value === 'success' && data.value) {
        // Add a product to product list
        if (productUpdate.value === true && productUpdateAdd.value.id) {
            productStore.setUpdateProduct(productUpdateAdd.value.id);
        } else {
            productStore.addNewProduct(data.value);
        }
        const formElement = e.target as HTMLFormElement;
        formElement.reset();
        productStore.resetProductUpdateAdd();
    } else {
        elementStore.setErrorMessageList([JSON.stringify(error.value)]);
    }
}
</script>

<style scoped></style>