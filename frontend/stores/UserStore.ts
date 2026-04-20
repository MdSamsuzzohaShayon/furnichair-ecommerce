import { defineStore } from "pinia";
import type { UserSignupInterface, UserSigninInterface, UserInfoInterface, UserAddressInterface, AddressAddUpdateInterface, WishlistInt } from '@/types/UserType';

const useUserStore = defineStore('userStore', {
    state: () => ({
        userSignup: {
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            confirm_password: '',
        } as UserSignupInterface,
        userSignin: {
            email: '',
            password: '',
        } as UserSigninInterface,
        isAuthenticated: false,
        userInfo: {
            id: null,
            email: null,
            first_name: null,
            last_name: null,
            is_admin: null,
            is_validated: null,
            is_staff: null,
            is_active: null,
            address: [] as UserAddressInterface[],
        } as UserInfoInterface,
        userAddressAddOrUpdate: {
            city: '',
            country: 'Bangladesh',
            phone: null,
            area: '',
            user: 0,
        } as AddressAddUpdateInterface,
        userList: [] as UserInfoInterface[],        
        
        emailOfUser: '' as string, // For forget password
    }),
    actions: {
        setIsAuthenticated(isAuthenticated: boolean) {
            this.isAuthenticated = isAuthenticated;
        },
        setUserInfo(newUserInfo: UserInfoInterface) {
            this.userInfo = newUserInfo;
        },
        setUserNewAddress(newAddress: UserAddressInterface) {
            const newAddressList: UserAddressInterface[] = Array.from(this.userInfo.address)
            if (!newAddress.id) {
                newAddress.id = this.userInfo.address.length + 10;
            }
            newAddressList.push(newAddress);
            this.userInfo = {
                ...this.userInfo,
                // @ts-ignore
                address: newAddressList
            }
        },
        setUserAddressAddOrUpdate(addressId: number) {
            const findAddress = this.userInfo.address.find(address => address.id === addressId);
            if (findAddress) this.userAddressAddOrUpdate = findAddress;
        },
        async setRefreshToken(refreshToken: string) {
            const { data: newRefreshToken, error: refreshError, refresh: refreshRequest, status: refreshStatus } = await useFetch(`${BACKEND_URL}/accounts/token/refresh/`, {
                key: `${new Date().getSeconds()}`,
                method: "POST",
                body: {
                    refresh: refreshToken
                }
            });
            await refreshRequest();

            if (refreshStatus.value === 'success') {
                const token = useCookie("token", {
                    maxAge: MAX_SIGNIN_COOKIE_AGE,
                    // httpOnly: true, // On https protocal, Need to set by server 
                });
                token.value = JSON.stringify(newRefreshToken.value);
            }

        },
        async fetchUser(accessToken: string) {

            const { data: userInfo, error: userError, refresh: refreshRequest, status: userStatus } = await useFetch<UserInfoInterface>(`${BACKEND_URL}/accounts/detail/`, {
                key: `user-fetch-${new Date().getSeconds()}${new Date().getMilliseconds()}`,
                headers: {
                    "Authorization": `Bearer ${accessToken}`
                }
            });
            await refreshRequest();

            if (userStatus.value === 'success' && userInfo.value) {
                this.isAuthenticated = true;
                this.userInfo = userInfo.value;
                localStorage.setItem('userInfo', JSON.stringify(this.userInfo));
                // nuxtStorage.localStorage.setData('userInfo', JSON.stringify(this.userInfo));
                return true;
            }
            return userError;
        },
        async fetchAllUser(accessToken: string) {
            // accounts/list/
            const { data: userList, error: userError, refresh: refreshRequest, status: userStatus } = await useFetch<UserInfoInterface[]>(`${BACKEND_URL}/accounts/list/`, {
                key: `all-user-fetch-${new Date().getSeconds()}${new Date().getMilliseconds()}`,
                headers: {
                    "Authorization": `Bearer ${accessToken}`
                }
            });
            await refreshRequest();
            // console.log({ "Error ": userError.value, "Status": userStatus.value, "data": userList.value });
            if (userStatus.value === 'success' && userList.value) {
                this.userList = userList.value;
            }
        }
    },
    getters: {
        serializedUserSignup(state): UserSignupInterface | null {
            const userSignupData: UserSignupInterface = {
                first_name: '',
                last_name: '',
                email: '',
                password: '',
                confirm_password: '',
            }
            let isValid = true;
            for (const [k, v] of Object.entries(state.userSignup)) {
                if (v === '' || v === undefined || v === null) {
                    isValid = false;
                } else {
                    userSignupData[k as keyof UserSignupInterface] = v;
                }
            }
            if (userSignupData.password !== userSignupData.confirm_password) {
                isValid = false;
            }
            if (isValid) return userSignupData;
            return null;
        },
        serializedUserSignin(state): UserSigninInterface | null {
            const userSigninData: UserSigninInterface = {
                email: '',
                password: '',
            }
            let isValid = true;
            for (const [k, v] of Object.entries(state.userSignin)) {
                if (v === '' || v === undefined || v === null) {
                    isValid = false;
                } else {
                    userSigninData[k as keyof UserSigninInterface] = v;
                }
            }
            if (isValid) return userSigninData;
            return null;
        }
    }
});

export default useUserStore;