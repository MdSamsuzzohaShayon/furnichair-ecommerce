<template>
  <div>
    <!-- orderList -->
    <table class="w-full mt-4">
      <thead>
        <tr>
          <th class="p-2 text-center border border-teal-900">ID</th>
          <th class="p-2 text-center border border-teal-900">Product</th>
          <th class="p-2 text-center border border-teal-900">Status</th>
          <th class="p-2 text-center border border-teal-900">Quantity</th>
          <th class="p-2 text-center border border-teal-900">Address</th>
          <th class="p-2 text-center border border-teal-900">Total Price (৳)</th>
          <th class="p-2 text-center border border-teal-900">Perform</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in organizedOrders()">
          <td class="p-2 text-center border border-teal-900/50">{{ order.id }}</td>
          <td class="p-2 text-center border border-teal-900/50">{{ order.product }}</td>
          <td class="p-2 text-center border border-teal-900/50 capitalize">{{ order.status }}</td>
          <td class="p-2 text-center border border-teal-900/50">{{ order.quantity }}</td>
          <td class="p-2 text-center border border-teal-900/50">{{ `${order.address.area}, ${order.address.city},
            ${order.address.phone}` }}</td>
          <td class="p-2 text-center border border-teal-900/50">{{ order.total }}</td>
          <td class="p-2 text-center border border-teal-900/50">
            <p class="cursor-pointer text-red-900" v-if="order.status === 'PENDING'"
              v-on:click.prevent="cancelOrderHandler(order.id)">Cancel</p>
            <NuxtLink v-bind:to="`#`">
              <p class="cursor-pointer text-teal-900">View</p>
            </NuxtLink>
            <!-- <Icon class="pr-2" size="20" name="bytesize:eye" color="teal" /> -->
            <p v-if="userInfo.is_staff" class="cursor-pointer text-teal-900"
              v-on:click.prevent="updateOrderHandler(order.id)">Update</p>
            <!-- <Icon v-if="userInfo.is_staff" class="pr-2" size="20" name="line-md:edit" v-on:click.prevent="updateOrderHandler(order.id)"
                            color="teal" /> -->
          </td>
        </tr>
      </tbody>
    </table>
    <Pagination v-bind:limit="state.limit" v-bind:limitUpdate="limitUpdate" v-bind:listUpdate="listUpdate" />
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";

import useOrderStore from "@/stores/OrderStore";
import useProductStore from "@/stores/ProductStore";
import useUserStore from "@/stores/UserStore";
import type { OrderStatus, OrganizedOrderInterface, OrderInterface } from "@/types/ProductOrderType";


const ordersStore = useOrderStore();
const productStore = useProductStore();
const userStore = useUserStore();

const { orderList, orderPaginatedList } = storeToRefs(ordersStore);
const { userInfo } = storeToRefs(userStore);

// Pagination logic start
const state = reactive({ limit: 10 });
// Set paginated list
ordersStore.setPaginatedList(0, state.limit);
const listUpdate = (moveLeft: boolean) => {
  if (orderPaginatedList.value.length <= 0) return;
  if (moveLeft) {
    const firstItemId = orderPaginatedList.value[0].id;
    const end = orderList.value.findIndex((order) => order.id === firstItemId);
    if (end + 1 < state.limit || end - state.limit < 0) {
      ordersStore.setPaginatedList(0, state.limit);
    } else {
      ordersStore.setPaginatedList(end - state.limit, end);
    }
  } else {
    const lastItemId = orderPaginatedList.value[orderPaginatedList.value.length - 1].id;
    const start = orderList.value.findIndex((order) => order.id === lastItemId);
    if (start + state.limit >= orderList.value.length) {
      ordersStore.setPaginatedList(orderList.value.length - state.limit, orderList.value.length);
    } else {
      ordersStore.setPaginatedList(start + 1, (start + 1) + state.limit);
    }
  }
};
const limitUpdate = (limit: number) => {
  if (orderPaginatedList.value.length <= 0) return;
  state.limit = limit;
  const firstElementId = orderPaginatedList.value[0].id;
  const start = orderList.value.findIndex((order) => order.id === firstElementId);
  ordersStore.setPaginatedList(start, limit);
};
// Pagination logic end 

const cancelOrderHandler = async (oId: number | null) => {
  const accessToken = useCookie(ACCESS_TOKEN);

  if (!accessToken.value) {
    console.error('There is no access token');
    return;

  }

  const {
    data: orderData,
    error: orderError,
    refresh: orderRefresh,
    status: orderStatus,
  } = await useFetch(`${BACKEND_URL}/orders/cancel/${oId}/`, {
    key: oId + "-" + new Date().getSeconds() + "-" + new Date().getMilliseconds(),
    method: "PUT",
    headers: {
      Authorization: `Bearer ${accessToken.value}`,
    },
  });
  if (orderStatus.value === "success" && orderData.value) {
    if (oId) ordersStore.cancelAnOrder(oId);
  }
};

const updateOrderHandler = async (oId: number) => {
  // ordersStore.setOrderUpdate(true);
  // ordersStore.setOrderToUpdate(pId);
  try {
  } catch (error) {
    console.log(error);
  }
};

const organizedOrders = () => {
  const newOrderList: OrganizedOrderInterface[] = [];
  const ol = orderPaginatedList.value;
  for (let i = 0; i < ol.length; i++) {
    // product: number;
    // address: number;
    let status = "PENDING";
    if (ol[i].status === OrderStatus.COMPLETED) {
      status = "COMPLETED";
    } else if (ol[i].status === OrderStatus.SHIPPING) {
      status = "SHIPPING";
    } else if (ol[i].status === OrderStatus.CANCELED) {
      status = "CANCELED";
    }

    // const findProduct = productStore.productList.find(p => p.id === ol[i].product);
    // console.log(userInfo.value.address[i]);

    const newOrder: OrganizedOrderInterface = {
      id: ol[i].id,
      status: status,
      is_paid: ol[i].is_paid,
      product: ol[i].product.title,
      quantity: ol[i].quantity,
      // address: `${userInfo.value.address[0]?.area}, ${userInfo.value.address[0]?.city}`,
      address: ol[i].address,
      total: ol[i].total,
    };
    newOrderList.push(newOrder);
  }
  return newOrderList;
};
</script>

<style scoped></style>
