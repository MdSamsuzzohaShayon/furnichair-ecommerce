
interface IDocument {
    id: number;
    created_at: string;
}

export interface IProduct extends IDocument {
    title: string;
    price: number;
    discount_price: number;
    total_stock: number;
    description: string;
    category: ICategory;
    image1: string;
    image2: string | null;
    image3: string | null;
    image4: string | null;
}

export interface ICategory {
    id: number;
    name: string;
    image: string;
    created_at: string;
    lft: number;
    rght: number;
    tree_id: number;
    level: number;
    parent: null | number;
    shipping_charge: number;
}



