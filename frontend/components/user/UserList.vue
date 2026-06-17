<template>
    <div>
        <table class="table-auto w-full mt-4">
            <thead >
                <tr>
                    <th class="p-2 text-center border border-teal-900" >ID</th>
                    <th class="p-2 text-center border border-teal-900" >Name</th>
                    <th class="p-2 text-center border border-teal-900" >Phone</th>
                    <th class="p-2 text-center border border-teal-900" >Email</th>
                    <th class="p-2 text-center border border-teal-900" >Address</th>
                    <th class="p-2 text-center border border-teal-900" >Verified</th>
                    <th class="p-2 text-center border border-teal-900" >Admin</th>
                    <th class="p-2 text-center border border-teal-900" >#</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in userList">
                    <td class="p-2 text-center border border-teal-900/50">{{ user.id }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ user?.first_name + " " + user?.last_name }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ user?.address.length > 0 ? user?.address[0].phone : '' }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ user?.email }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ user?.address.length > 0 ? user.address[0].area + ", " + user.address[0].city : '' }}</td>
                    <td class="p-2 text-center border border-teal-900/50">
                        <Icon name="line-md:confirm" size="10" v-if="user.is_active" />
                    </td>
                    <td class="p-2 text-center border border-teal-900/50">
                        <Icon name="line-md:confirm" size="10" v-if="user.is_admin || user.is_staff" />
                    </td>
                    <td class="p-2 text-center border border-teal-900/50">
                        <Icon size="20" name="lucide:trash-2" color="red" v-on:click.prevent="deleteUserHandler(user.id)" />
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useUserStore from '@/stores/UserStore';

const userStore = useUserStore();

const { userList } = storeToRefs(userStore);

const deleteUserHandler = (uId: number | null) => {
    console.log("Delete user -> ", uId);
}
</script>

<style scoped></style>