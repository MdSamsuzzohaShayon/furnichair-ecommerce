export interface UserSigninInterface {
    email: string;
    password: string;
}

export interface UserSignupInterface extends UserSigninInterface {
    first_name: string;
    last_name: string;
    email: string;
    password: string;
    confirm_password: string;
}

export interface UserAddressInterface {
    id: number;
    city: string;
    country: string;
    phone: number;
    area: string;
    user: number;
}

export interface AddressAddUpdateInterface {
    id?: number;
    city: string;
    country: string;
    phone: number | null;
    area: string;
    user: number;
}

export interface UserInfoInterface {
    id: number | null;
    email: string | null;
    first_name: string | null;
    last_name: string | null;
    is_admin: boolean | null;
    is_validated: boolean | null;
    is_staff: boolean | null;
    is_active: boolean | null;
    address: UserAddressInterface[];
}

export interface UserTokenInterface{
    access: string;
    refresh: string;
}

export interface UserRequestSuccessResInt{
    detail: string;
}

export interface WishlistInt{
    id: number;
    email: string;
    preview: boolean;
    created_at: string;
    updated_at: string;
}
