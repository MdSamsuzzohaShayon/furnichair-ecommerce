import { defineStore } from "pinia";
import type { OrderInterface, OrderStatus } from "@/types/ProductOrderType";

const useOrderStore = defineStore('orderStore', {
    state: () => ({
        orderList: [] as OrderInterface[],
        orderPaginatedList: [] as OrderInterface[],
    }),
    actions: {
        addNewOrder(newOrder: OrderInterface){
            this.orderList.push(newOrder);
        },
        cancelAnOrder(orderId: number){
            const findOrderIndex = this.orderList.findIndex((order)=> order.id == orderId);
            if(findOrderIndex){
                const orderObj = {...this.orderList[findOrderIndex]};
                orderObj.status = OrderStatus.CANCELED;
                this.orderList[findOrderIndex] = orderObj;
            }
        },
        deleteOrder(catId: number) {
            this.orderList = this.orderList.filter((c: OrderInterface) => c.id !== catId);
        },
        setPaginatedList(start: number, limit: number){
            this.orderPaginatedList = this.orderList.slice(start, limit);
        },
        async fetchOrders(access: string) {
            const { data: productOrders, refresh: refreshRequest } = await useFetch<OrderInterface[]>(`${BACKEND_URL}/orders/user/`, {
                key: `order-user-${new Date().getSeconds()}-${new Date().getMilliseconds()}`,
                headers: {
                    "Authorization": "Bearer " + access
                }
            });
            await refreshRequest();
            // console.log(productOrders.value);


            if (productOrders.value) {
                this.orderList = productOrders.value
            }
        },
        async fetchAllOrders(access: string) {
            const { data: productOrders, refresh: refreshRequest } = await useFetch<OrderInterface[]>(`${BACKEND_URL}/orders/list/`, {
                key: `order-list-${new Date().getSeconds()}-${new Date().getMilliseconds()}`,
                headers: {
                    "Authorization": "Bearer " + access
                }
            });
            await refreshRequest();
            if (productOrders.value) {
                this.orderList = productOrders.value
            }
        },
    },
    getters: {
    }
});


export default useOrderStore;