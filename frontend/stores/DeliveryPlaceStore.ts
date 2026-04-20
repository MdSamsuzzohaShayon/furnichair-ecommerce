import { defineStore } from "pinia";
import type { DeliveryPlaceInt } from "@/types/DeliveryPlaceType";

const useDeliveryPlaceStore = defineStore("deliveryPlace", {
  state: () => ({
    currentDeliveryPlace: {} as DeliveryPlaceInt,
    deliveryPlaceList: [] as DeliveryPlaceInt[],
    deliveryPlaceAdd: {} as DeliveryPlaceInt,
    deliveryPlaceUpdate: false as boolean,
    deliveryPlaceUpdateId: null as null | number,
  }),
  actions: {
    setDeliveryPlaceUpdate(update: boolean) {
      this.deliveryPlaceUpdate = update;
    },
    setDeliveryPlaceUpdateId(deliveryId: number) {
      const findDelivery = this.deliveryPlaceList.find((delivery) => delivery.id === deliveryId);
      if (!findDelivery) return;
      this.deliveryPlaceUpdateId = deliveryId;
      this.deliveryPlaceAdd = findDelivery;
    },
    addDeliveryPlace() {
      this.deliveryPlaceList.push({
        id: this.deliveryPlaceList[this.deliveryPlaceList.length - 1].id + 1,
        place: this.deliveryPlaceAdd.place,
        price: this.deliveryPlaceAdd.price,
      });
    },
    async fetchAllPlaces() {
      const { data: placeData, refresh: refreshRequest } = await useFetch<DeliveryPlaceInt[]>(`${BACKEND_URL}/products/delivery/list/`, {
        key: `delivery-list-${new Date().getSeconds()}-${new Date().getMilliseconds()}`,
        headers: {
          "Content-Type": "application/json",
        },
      });
      await refreshRequest();
      if (placeData.value) {
        // console.log(placeData.value);

        this.deliveryPlaceList = placeData.value;
      }
    },
  },
});

export default useDeliveryPlaceStore;
