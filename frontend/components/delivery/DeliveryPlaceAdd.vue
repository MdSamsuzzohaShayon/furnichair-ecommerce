<template>
  <div>
    <form class="flex flex-col gap-4 mt-4" v-on:submit.prevent="deliveryPlaceAddUpdateHandler">
      <div class="input-group w-full">
        <input v-bind:required="deliveryPlaceUpdate === false ? true : false" type="text" id="deliveryPlace-name"
          class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
          placeholder="District" v-model="deliveryPlaceAdd.place" />
      </div>
      <div class="input-group w-full">
        <input v-bind:required="deliveryPlaceUpdate === false ? true : false" type="number" id="delivery-price"
          class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50 remove-arrow"
          placeholder="Price" v-model="deliveryPlaceAdd.price" />
      </div>
      <!-- Submit  -->
      <div class="input-group w-full">
        <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold" type="submit">
          {{ deliveryPlaceUpdate ? "Update" : "Add" }}
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
import useDeliveryStore from "@/stores/DeliveryPlaceStore";
import type { ProductCategoryInterface } from "@/types/ProductCategoryType";

const elementStore = useElementStore();
const deliveryPlaceStore = useDeliveryStore();

const { deliveryPlaceAdd, deliveryPlaceUpdate, deliveryPlaceUpdateId } = storeToRefs(deliveryPlaceStore);
const { errorMessageList, successMessageList } = storeToRefs(elementStore);

const deliveryPlaceAddUpdateHandler = async (e: Event) => {
  elementStore.resetErrorMessageList();
  elementStore.resetSuccessMessageList();
  const accessToken = useCookie(ACCESS_TOKEN);

  if (!accessToken.value) {
    console.error('There is no access token');
    return;

  }
  let resStatus = null,
    resError = null;
  if (deliveryPlaceUpdate.value) {
    const { data, pending, error, refresh, status } = await useFetch<ProductCategoryInterface>(
      `${BACKEND_URL}/products/delivery/${deliveryPlaceUpdateId.value}/update/`,
      {
        method: "PUT",
        body: deliveryPlaceAdd.value,
        headers: {
          Authorization: `Bearer ${accessToken.value}`,
        },
      }
    );
    resStatus = status;
    resError = error;
  } else {
    deliveryPlaceStore.addDeliveryPlace();
    const { data, pending, error, refresh, status } = await useFetch<ProductCategoryInterface>(`${BACKEND_URL}/products/charge/new/`, {
      method: "POST",
      body: deliveryPlaceAdd.value,
      headers: {
        Authorization: `Bearer ${accessToken.value}`,
      },
    });
    resStatus = status;
    resError = error;
  }
  if (deliveryPlaceAdd.value.place && deliveryPlaceAdd.value.price) {
    if (resStatus.value === "success") {
      // Add a deliveryPlace to deliveryPlace list
      const formElement = e.target as HTMLFormElement;
      formElement.reset();
    } else {
      elementStore.setErrorMessageList([JSON.stringify(resStatus.value)]);
    }
  }
};
</script>

<style scoped></style>
