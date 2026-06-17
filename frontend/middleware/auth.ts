import { ACCESS_TOKEN } from "~/utils/constant";

export default defineNuxtRouteMiddleware((to, from) => {
    const token = useCookie(ACCESS_TOKEN);
    
    

    // skip middleware on server
    // if (process.server) return

    // if (to.params.id === '1') {
    //     return abortNavigation()
    // }
    
    // In a real app you would probably not redirect every route to `/`
    // however it is important to check `to.path` before redirecting or you
    // might get an infinite redirect loop
    // if (to.path === '/user/dashboard') {
    //     return navigateTo('/')
    // }

    
    if(to.path === '/user/signin' || to.path === '/user/signin/' || to.path === '/user/signup' || to.path === '/user/signup/'){
        if(token.value){
            return navigateTo('/user/dashboard/');
        }
    }else if(to.path === '/admin/signin' || to.path === '/admin/signin/'){
        if(token.value){
            return navigateTo('/admin/');
        }
    }else if(to.path === '/admin' || to.path === '/admin/'){
        if(!token.value){
            return navigateTo('/admin/signin/');
        }
    }else if(to.path === '/user/dashboard' || to.path === '/user/dashboard/'){
        if(!token.value){
            return navigateTo('/user/signin/');
        }
    }
});