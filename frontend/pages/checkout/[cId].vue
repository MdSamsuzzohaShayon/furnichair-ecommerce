<template>
  <div class="container mx-auto px-2">
    <h1>Checkout</h1>
    <h2>Check if payment is completed or not.</h2>
    <p>Pay via bkash</p>
    <p>If payment is completed delete this from cart</p>
    <p>And add a order in order section</p>
    <p class="bg-teal-200">Select shipping address</p>
    <div class="shipping" v-if="userInfo.address.length > 0">
      <p>Phone: {{ userInfo.address[0].phone }}</p>
      <p>Area: {{ userInfo.address[0].area }}</p>
      <p>City: {{ userInfo.address[0].city }}</p>
      <button type="button" class="bg-teal-900 text-teal-100 p-2" v-on:click="addAddressHandler">Edit</button>
    </div>
    <!-- deliveryPlaceList -->
    <div class="input-group w-full">
      <label for="delivery-place" class="text-teal-950/50">Districe</label>
      <select id="delivery-place" v-on:change.prevent="deliveryPlaceChangeHandler"
        class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50">
        <option v-for="delivery in deliveryPlaceList" v-bind:value="delivery.id">{{ delivery.place }}</option>
      </select>
    </div>
    <br />
    <p>Quantity: {{ state.productQuantity }}</p>
    <p>Item Total: ৳ {{ state.itemTotal }}</p>
    <p>Delivery Fee: ৳ {{ state.shipping_charge + state.deliveryCityPrice }}</p>
    <p>Total Payment: ৳ {{ state.totalPayment }}</p>
    <button class="p-2 bg-teal-900 text-teal-100 mr-2" v-on:click="payAndOrderHandler">Cash on delivery</button>
    <button class="p-2 bg-teal-900 text-teal-100" v-on:click="payAndOrderHandler">Pay via BKash</button>
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import useProductStore from "../../stores/ProductStore";
import useElementsStore from "../../stores/ElementsStore";
import useUserStore from "../../stores/UserStore";
import userOrderStore from "../../stores/OrderStore";
import useDeliveryPlaceStore from "../../stores/DeliveryPlaceStore";
import { OrderInterface } from "../../types/ProductOrderType";

const state = reactive({
  itemTotal: 0,
  shipping_charge: 0, //from category
  cityOfUser: '',
  deliveryCityPrice: 0,
  productQuantity: 1,
  totalPayment: 0
});

const productStore = useProductStore();
const elementsStore = useElementsStore();
const userStore = useUserStore();
const orderStore = userOrderStore();
const deliveryPlaceStore = useDeliveryPlaceStore();

productStore.fetchCartFromLocalStorage();

const { cId } = useRoute().params;

const { userInfo } = storeToRefs(userStore);
const { deliveryPlaceList } = storeToRefs(deliveryPlaceStore);
const { productList } = storeToRefs(productStore);
// console.log(cId);

const cart = productStore.getCartById(cId);
const initialValueSet = () => {
  if (cart?.pId) {
    const findProduct = productList.value.find((p) => p.id === cart.pId);
    if (findProduct) {
      // @ts-ignore
      state.itemTotal = findProduct.discount_price ? parseInt(findProduct.discount_price, 10) : parseInt(findProduct.price, 10);
      state.shipping_charge = findProduct.category.shipping_charge;

      state.totalPayment = state.itemTotal + ((state.shipping_charge + state.deliveryCityPrice) * state.productQuantity);
      deliveryPlaceStore.fetchAllPlaces()
    }
  }
  // fetchOrders
}

initialValueSet();

const deliveryPlaceChangeHandler = (e: Event) => {
  // console.log(e.target.value);
  const optionEl = e.target as HTMLSelectElement;
  const findPlace = deliveryPlaceList.value.find((delivery) => delivery.id === parseInt(optionEl.value, 10));
  if (!findPlace) return;
  state.deliveryCityPrice = findPlace.price;
}

const addAddressHandler = (e: Event) => { };

const payAndOrderHandler = async (e: Event) => {
  e.preventDefault();

  // Redirect to order page
  const accessToken = useCookie(ACCESS_TOKEN);
  if (!accessToken.value) {
    console.error('There is no access token');
    return;

  }
  if (!cart) return elementsStore.setErrorMessageList(["Product not found!"]);
  const { data: orderData, status: orderStatus } = await useFetch<OrderInterface>(`${BACKEND_URL}/orders/new/`, {
    key: cId,
    method: "POST",
    body: {
      product: cart.pId,
      quantity: cart.qty,
      address: userInfo.value.address[0].id,
    },
    headers: {
      Authorization: `Bearer ${accessToken.value}`,
    },
  });
  if (orderStatus.value === "success" && orderData.value) {
    orderStore.addNewOrder(orderData.value);
    navigateTo("/user/dashboard/");
  } else {
    elementsStore.setErrorMessageList(["Invalid cart item!"]);
  }
};
</script>

<style scoped></style>
