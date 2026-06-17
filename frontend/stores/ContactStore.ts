import { defineStore } from "pinia";
import type { WillContactInterface, ContactFetchedInterface } from "@/types/ContactType";

const useContactStore = defineStore('contactStore', {
    state: () => ({
        willContact: {
            name: '',
            email: '',
            message: ''
        } as WillContactInterface,
        contactList: [] as ContactFetchedInterface[],
    }),
    actions: {
        previewAContact(catId: number) {
            // make preview true
        },
        async fetchContacts(accessToken: string) {

            if (!accessToken) {
                console.error('There is no access token');
                return;

            }
            const { data: contactData, refresh: refreshRequest, status: contactStatus } = await useFetch<ContactFetchedInterface[]>(`${BACKEND_URL}/contacts/list/`, {
                key: `contacts-${new Date().getSeconds()}-${new Date().getMilliseconds()}`,
                headers: {
                    "Authorization": "Bearer " + accessToken
                }
            });
            if (contactStatus.value === 'success' && contactData.value) {
                this.contactList = contactData.value;
            }
        },
    },
    getters: {
    }
});


export default useContactStore;