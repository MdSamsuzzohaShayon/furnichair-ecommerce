<template>
  <div>
    <form class="flex flex-col gap-4 mt-4" v-on:submit.prevent="categoryAddUpdateHandler">
      <div class="input-group w-full">
        <input
          v-bind:required="categoryUpdate === false ? true : false"
          type="text"
          id="category-name"
          class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
          placeholder="Name"
          v-model="categoryAddUpdate.name"
        />
      </div>
      <div class="input-group w-full">
        <input
          v-bind:required="categoryUpdate === false ? true : false"
          type="number"
          id="category-shipping_charge"
          class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50 remove-arrow"
          placeholder="Shipping Charge"
          v-model="categoryAddUpdate.shipping_charge"
        />
      </div>
      <div class="input-group w-full">
        <label for="category-image" class="w-full bg-white text-teal-950/50 px-3 py-2 border border-teal-950/25 block">
          <span>
            <Icon name="ph:image" size="20" />
          </span>
          {{ state.imageName !== "" ? state.imageName : "Image" }}</label
        >
        <input
          v-bind:required="categoryUpdate === false ? true : false"
          type="file"
          id="category-image"
          name="image"
          ref="uploadFile"
          class="hidden"
          v-on:input="uploadFileChangeHandler"
        />
      </div>
      <!-- Submit  -->
      <div class="input-group w-full">
        <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold" type="submit">
          {{ categoryUpdate ? "Update" : "Add" }}
        </button>
      </div>
    </form>
    <p class="text-red-900 px-4 py-2 capitalize" v-for="message in errorMessageList">{{ message }}</p>
    <p class="text-teal-900 px-4 py-2 capitalize" v-for="message in successMessageList">{{ message }}</p>
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import useElementStore from "@/stores/ElementsStore";
import useCategoryStore from "@/stores/CategoryStore";
import type { ProductCategoryInterface } from "@/types/ProductCategoryType";

const uploadFile = ref(null);
const state = reactive({
  imageName: "",
});

const elementStore = useElementStore();
const categoryStore = useCategoryStore();

const { errorMessageList, successMessageList } = storeToRefs(elementStore);
const { categoryUpdate, categoryAddUpdate, categoryUpdateId } = storeToRefs(categoryStore);

const formData = new FormData();
const uploadFileChangeHandler = (e: Event) => {
  const fileInput = e.target as HTMLInputElement;
  // @ts-ignore
  state[`${fileInput.name}Name`] = fileInput.files[0].name;
  if (fileInput.files && fileInput.files.length > 0) {
    formData.set("categoryimage", fileInput.files[0] as Blob);
  }
};

const categoryAddUpdateHandler = async (e: Event) => {
  elementStore.resetErrorMessageList();
  elementStore.resetSuccessMessageList();
  const accessToken = useCookie(ACCESS_TOKEN);

  if(!accessToken.value){
    console.error('There is no access token');
    return;
    
  }


  let resStatus = null,
    resError = null;
    
  if (categoryUpdate && categoryUpdate.value) {
    if (categoryAddUpdate.value.name) formData.set("name", categoryAddUpdate.value.name);
    if (categoryAddUpdate.value.shipping_charge) formData.set("shipping_charge", categoryAddUpdate.value.shipping_charge.toString());
    const { data, pending, error, refresh, status } = await useFetch<ProductCategoryInterface>(
      `${BACKEND_URL}/products/categories/${categoryUpdateId.value}/update/`,
      {
        method: "PUT",
        body: formData,
        headers: {
          Authorization: `Bearer ${accessToken.value}`,
        },
      }
    );
    categoryStore.setUpdateSpecificCategory();
    resError = error;
    resStatus = status;
  } else {
    if (categoryAddUpdate.value.name && uploadFile.value && categoryAddUpdate.value.shipping_charge) {
      formData.set("name", categoryAddUpdate.value.name);
      formData.set("shipping_charge", categoryAddUpdate.value.shipping_charge.toString());
      const { data, pending, error, refresh, status } = await useFetch<ProductCategoryInterface>(`${BACKEND_URL}/products/categories/new/`, {
        method: "POST",
        body: formData,
        headers: {
          Authorization: `Bearer ${accessToken.value}`,
        },
      });
      if (data.value) categoryStore.addNewCategory(data.value);
      resError = error;
      resStatus = status;
    }
  }

  if (resStatus?.value === "success") {
    // console.log(data.value);
    // Add a category to category list
    const formElement = e.target as HTMLFormElement;
    formElement.reset();
  } else {
    elementStore.setErrorMessageList([JSON.stringify(resError?.value)]);
  }
};
</script>

<style scoped></style>
