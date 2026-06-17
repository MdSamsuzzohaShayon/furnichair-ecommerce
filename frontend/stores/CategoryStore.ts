import { defineStore } from "pinia";
import type { ProductCategoryInterface } from "@/types/ProductCategoryType";

const useCategoryStore = defineStore("categoryStore", {
  state: () => ({
    categoryList: [] as ProductCategoryInterface[],
    currentCategory: {} as ProductCategoryInterface,
    categoryUpdate: false as boolean,
    categoryUpdateId: null as null | number,
    categoryAddUpdate: {} as ProductCategoryInterface,
  }),
  actions: {
    setCategoryUpdateId(catId: number) {
      this.categoryUpdateId = catId;
    },
    setCategoryAddUpdate(catId: number) {
      const findCat = this.categoryList.find((cat) => cat.id === catId);

      if (!findCat) return;
      // @ts-ignore
      this.categoryAddUpdate = { id: findCat.id, name: findCat.name, shipping_charge: findCat.shipping_charge };
    },
    setUpdateSpecificCategory(){
      const findItemIndex = this.categoryList.findIndex((c: ProductCategoryInterface) => c.id !== this.categoryUpdateId);
      if(findItemIndex){
        this.categoryList[findItemIndex] = this.categoryAddUpdate;
      }
    },
    setCategoryUpdate(update: boolean) {
      this.categoryUpdate = update;
    },
    addNewCategory(newCategory: ProductCategoryInterface) {
      this.categoryList.push(newCategory);
    },
    deleteCategory(catId: number) {
      this.categoryList = this.categoryList.filter((c: ProductCategoryInterface) => c.id !== catId);
    },
    setCurrentCategory(catId: number) {
      const findItem = this.categoryList.find((c: ProductCategoryInterface) => c.id !== catId);
      if (findItem) {
        this.currentCategory = findItem;
      }
    },
    async fetchCategories() {
      const { data: productCategories, refresh: refreshRequest } = await useFetch<ProductCategoryInterface[]>(`${BACKEND_URL}/products/categories/list/`);
      await refreshRequest();
      if (productCategories.value) {
        this.categoryList = productCategories.value;
      }
    },
  },
});

export default useCategoryStore;
