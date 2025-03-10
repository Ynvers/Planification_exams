<template>
    <header class="w-full h-[70px] z-50 bg-gray-800 fixed top-0 flex items-center justify-center">
        <div class="container px-[20px] lg:max-w-[1024px] relative w-full flex items-center justify-between">
            <div class="flex items-center justify-start relative text-2xl font-bold text-white">
                <svg class="mr-[5px] text-[#34D399]" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 20 20"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M3.33 8L10 12l10-6l-10-6L0 6h10v2zM0 8v8l2-2.22V9.2zm10 12l-5-3l-2-1.2v-6l7 4.2l7-4.2v6z"/></svg>
                SmartExam
            </div>
            <div class="text-3xl cursor-pointer flex lg:hidden text-white" @click="toggleMenu()">
                <i v-if="isOpen" class="fa-solid fa-xmark"></i>
                <i v-else class="fa-solid fa-bars"></i>
            </div>
            <nav :class="{'translate-x-0': isOpen, 'translate-x-[-100%]': !isOpen}" class="lg:w-[70%] lg:translate-x-0 duration-300 fixed lg:static bg-gray-700 lg:bg-transparent w-screen h-[calc(100vh-70px)] lg:h-auto lg:flex justify-between items-center top-[70px] left-0">
                <ul class="flex flex-col lg:flex-row items-center justify-center relative">
                    <li class="lg:text-sm text-3xl w-full lg:w-auto font-semibold text-gray-200 lg:mx-[10px] my-[15px] px-[20px] lg:px-0 py-[10px] lg:py-0 lg:my-0 flex items-center justify-between">Accueil <i class="fa-solid fa-chevron-right lg:hidden"></i></li>
                    <li class="lg:text-sm text-3xl w-full lg:w-auto font-semibold text-gray-200 lg:mx-[10px] my-[15px] px-[20px] lg:px-0 py-[10px] lg:py-0 lg:my-0 flex items-center justify-between">A propos <i class="fa-solid fa-chevron-right lg:hidden"></i></li>
                    <li class="lg:text-sm text-3xl w-full lg:w-auto font-semibold text-gray-200 lg:mx-[10px] my-[15px] px-[20px] lg:px-0 py-[10px] lg:py-0 lg:my-0 flex items-center justify-between">Services <i class="fa-solid fa-chevron-right lg:hidden"></i></li>
                    <li class="lg:text-sm text-3xl w-full lg:w-auto font-semibold text-gray-200 lg:mx-[10px] my-[15px] px-[20px] lg:px-0 py-[10px] lg:py-0 lg:my-0 flex items-center justify-between">Contact <i class="fa-solid fa-chevron-right lg:hidden"></i></li>
                </ul>
                <div class="flex w-full lg:w-auto flex-col lg:flex-row absolute lg:static bottom-[20px] px-[20px] lg:px-0 items-center justify-center">
                    <div class="lg:text-sm text-3xl w-full lg:w-auto font-semibold text-gray-200 lg:mx-[10px] my-[15px] lg:px-0 py-[10px] lg:py-0 lg:my-0">
                        F.A.Q
                    </div>
                    <button @click="goToLoginPage()" class="bg-[#34D399] w-full lg:w-auto text-gray-800 font-bold text-sm rounded-[5px] p-[10px] ml-[10px]">
                        Se connecter
                    </button>
                </div>
            </nav>
        </div>
    </header>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue'

const router = useRouter()
const isOpen = ref(false)

const toggleMenu = () => {
    isOpen.value = !isOpen.value
}

function goToLoginPage () {
    router.push('/login')
}
</script>

<style>

</style>