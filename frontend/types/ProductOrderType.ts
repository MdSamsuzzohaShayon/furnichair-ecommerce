import type { UserAddressInterface } from "./UserType";
import type { ProductInterface } from './ProductType';

export enum OrderStatus {
    PENDING = "PG",
    SHIPPING = "SG",
    COMPLETED = "CD",
    CANCELED = "CL",
}

export interface OrderInterface {
    id: number;
    status: OrderStatus.PENDING | OrderStatus.SHIPPING | OrderStatus.COMPLETED | OrderStatus.CANCELED;
    is_paid: boolean;
    product: ProductInterface;
    address: UserAddressInterface;
    quantity: number;
    total: number;
}

export interface OrganizedOrderInterface {
    id: number;
    status: string;
    is_paid: boolean;
    product: string;
    address: UserAddressInterface;
    quantity: number;
    total: number;
}
