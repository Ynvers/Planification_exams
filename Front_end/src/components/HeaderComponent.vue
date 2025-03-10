<template>
    <header class="w-full h-[70px] z-50 bg-gray-800 fixed top flex items-center justify-center">
        <div class="container px-[20px] lg:max-w-[1024px] relative w-full flex items-center justify-between">
            <div class="flex items-center justify-start relative text-2xl font-bold text-white">
                <svg class="mr-[5px] text-[#34D399]" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 20 20"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M3.33 8L10 12l10-6l-10-6L0 6h10v2zM0 8v8l2-2.22V9.2zm10 12l-5-3l-2-1.2v-6l7 4.2l7-4.2v6z"/></svg>
                SmartExam
            </div>
            <ul class="flex items-center justify-center relative">
                <li class="text-sm font-semibold text-gray-200 mx-[10px]">Accueil</li>
                <li class="text-sm font-semibold text-gray-200 mx-[10px]">A propos</li>
                <li class="text-sm font-semibold text-gray-200 mx-[10px]">Services</li>
                <li class="text-sm font-semibold text-gray-200 mx-[10px]">Contact</li>
            </ul>
            <div class="flex items-center justify-center">
                <div class="text-sm font-semibold text-gray-200 mx-[10px]">
                    F.A.Q
                </div>
                <button @click="goToLoginPage()" class="bg-[#34D399] text-gray-800 font-bold text-sm rounded-[5px] p-[10px] ml-[10px]">
                    Se connecter
                </button>
            </div>
        </div>
    </header>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()

function goToLoginPage () {
    router.push('/login')
}
</script>

<style>

</style>