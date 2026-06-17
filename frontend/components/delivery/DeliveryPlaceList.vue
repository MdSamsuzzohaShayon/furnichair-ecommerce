<template>
  <div class="mt-4">
    <ul>
      <li v-for="delivery in deliveryPlaceList" class="flex justify-between bg-white mb-2 p-2">
        <p>{{ delivery.place }} - ৳{{ delivery.price }}</p>
        <div class="flex gap-2">
          <Icon size="20" name="mdi:file-document-edit-outline" color="blue"
            v-on:click.prevent="updateDeliveryHandler(delivery.id)" />
          <Icon size="20" name="lucide:trash-2" color="red" v-on:click.prevent="deleteDeliveryHandler(delivery.id)" />
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import useDeliveryPlaceStore from "@/stores/DeliveryPlaceStore";

const deliveryPlaceStore = useDeliveryPlaceStore();

const { deliveryPlaceList } = storeToRefs(deliveryPlaceStore);

const updateDeliveryHandler = async (deliveryId: number) => {
  deliveryPlaceStore.setDeliveryPlaceUpdate(true);
  deliveryPlaceStore.setDeliveryPlaceUpdateId(deliveryId);
};

const deleteDeliveryHandler = async (deliveryId: number) => {
  // console.log("Delete category -> ", catId);
  // const token = useCookie('token');
  // if (!token.value) return null;
  // // @ts-ignore
  const accessToken = useCookie(ACCESS_TOKEN);

  if (!accessToken.value) {
    console.error('There is no access token');
    return;

  }
  // // http://localhost:8000/api/products/categories/4/delete/
  // const { data: catInfo, error: catError, refresh: refreshRequest, status: catStatus } = await useFetch(`${BACKEND_URL}/products/categories/${catId}/delete/`, {
  //     method: "DELETE",
  //     key: `${catId}`,
  //     headers: {
  //         "Authorization": `Bearer ${accessToken.value}`
  //     }
  // });
  // // await refreshRequest();
  // // console.log({ "Error ": catError.value, "Status": catStatus.value, "data": catInfo.value });
  // console.log(catError.value?.data);
  // if (catStatus.value === 'success') {
  //     categoryStore.deleteCategory(catId);
  // } else if (catStatus.value === 'error') {
  //     if(catError.value){
  //         // @ts-ignore
  //         elementStore.setErrorMessageList(Object.values(catError.value.data));
  //     }else{
  //         elementStore.setErrorMessageList(["Make sure to delete all the products containing this category before deleteting this!"]);
  //     }
  // }
};

onMounted(async () => {
  // Reset error list
  // elementStore.resetErrorMessageList();
  // fetchCategories
});
</script>

<style scoped></style>
