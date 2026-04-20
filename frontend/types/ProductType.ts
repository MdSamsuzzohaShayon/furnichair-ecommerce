import type { ProductCategoryInterface } from "./ProductCategoryType";

export interface ProductBaseInterface {
  id: number;
  title: string;
  price: number;
  discount_price: number;
  total_stock: number;
  description: string;
  category: ProductCategoryInterface;
}

export interface ProductAddUpdateInterface {
  id?: number | null;
  title: string;
  price: number | null;
  discount_price: number | null;
  total_stock: number | null;
  description: string;
  category: number | null;
}

export interface ProductInterface extends ProductBaseInterface {
  image1: string;
  image2: string | null;
  image3: string | null;
  image4: string | null;
  created_at: string;
}

export interface ProductFilterInterface {
  title: string | null;
  price: string | null;
  total_stock: string | null;
  category: number | null;
}

export interface ProductFilterOptionalInterface {
  title?: string;
  price?: number;
  total_stock?: number;
  category?: number;
}

export interface CartItemInterface {
  id: string;
  pId: number;
  qty: number;
}
