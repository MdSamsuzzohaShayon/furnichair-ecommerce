<template>
  <div class="mt-4">
    <ul>
      <li v-for="cat in categoryList" class="flex justify-between bg-white mb-2 p-2">
        <p>{{ cat.name }} - ৳{{ cat.shipping_charge }}</p>
        <div class="felx gap-2">
          <Icon size="20" name="mdi:file-document-edit-outline" color="blue" v-on:click.prevent="updateCategoryHandler(cat.id)" />
          <Icon size="20" name="lucide:trash-2" color="red" v-on:click.prevent="deleteCategoryHandler(cat.id)" />
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import useCategoryStore from "@/stores/CategoryStore";
import useElementStore from "@/stores/ElementsStore";

const categoryStore = useCategoryStore();
const elementStore = useElementStore();

const { categoryList } = storeToRefs(categoryStore);

const updateCategoryHandler = async (catId: number) => {
  categoryStore.setCategoryUpdateId(catId);
  categoryStore.setCategoryUpdate(true);
  categoryStore.setCategoryAddUpdate(catId);
};

const deleteCategoryHandler = async (catId: number) => {
  const accessToken = useCookie(ACCESS_TOKEN);

  if(!accessToken.value){
    console.error('There is no access token');
    return;
    
  }

  const {
    data: catInfo,
    error: catError,
    refresh: refreshRequest,
    status: catStatus,
  } = await useFetch(`${BACKEND_URL}/products/categories/${catId}/delete/`, {
    method: "DELETE",
    key: `${catId}`,
    headers: {
      Authorization: `Bearer ${accessToken.value}`,
    },
  });
  // await refreshRequest();
  // console.log({ "Error ": catError.value, "Status": catStatus.value, "data": catInfo.value });
  console.log(catError.value?.data);

  if (catStatus.value === "success") {
    categoryStore.deleteCategory(catId);
  } else if (catStatus.value === "error") {
    if (catError.value) {
      // @ts-ignore
      elementStore.setErrorMessageList(Object.values(catError.value.data));
    } else {
      elementStore.setErrorMessageList(["Make sure to delete all the products containing this category before deleteting this!"]);
    }
  }
};

onMounted(async () => {
  // Reset error list
  elementStore.resetErrorMessageList();
  // fetchCategories
});
</script>

<style scoped></style>
