<template>
    <div :class="{'translate-x-0': isMenu, 'translate-x-[-100%]': !isMenu}" class="h-screen lg:translate-x-0 duration-300 lg:w-[25%] lg:sticky bottom-0 fixed z-50 left-0 top-0 w-[70%] min-w-[25%] bg-gray-800 p-[20px]">
        <div class="flex items-center justify-start w-full relative my-[20px] px-[20px] text-2xl font-bold text-white">
            <svg class="mr-[5px] text-[#34D399]" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 20 20"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M3.33 8L10 12l10-6l-10-6L0 6h10v2zM0 8v8l2-2.22V9.2zm10 12l-5-3l-2-1.2v-6l7 4.2l7-4.2v6z"/></svg>
            SmartExam
        </div>
        <ul class="w-full flex flex-col items-center justify-center mt-[50px] relative">
            <li @click="goToDashboardPage()" class="my-[10px] rounded-[5px] cursor-pointer p-[10px] px-[20px] flex justify-start items-center w-full hover:bg-[#34D399] hover:text-gray-800 duration-200 text-gray-200 text-base font-semibold" :class="{'text-gray-800 bg-[#34D399]': $route.path == '/dashboard'}">
                <svg class="mr-[5px]" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M14 9q-.425 0-.712-.288T13 8V4q0-.425.288-.712T14 3h6q.425 0 .713.288T21 4v4q0 .425-.288.713T20 9zM4 13q-.425 0-.712-.288T3 12V4q0-.425.288-.712T4 3h6q.425 0 .713.288T11 4v8q0 .425-.288.713T10 13zm10 8q-.425 0-.712-.288T13 20v-8q0-.425.288-.712T14 11h6q.425 0 .713.288T21 12v8q0 .425-.288.713T20 21zM4 21q-.425 0-.712-.288T3 20v-4q0-.425.288-.712T4 15h6q.425 0 .713.288T11 16v4q0 .425-.288.713T10 21z"/></svg>
                Tableau de bord
            </li>
            <li @click="goToExamensPage()" class="my-[10px] rounded-[5px] cursor-pointer p-[10px] px-[20px] flex justify-start items-center w-full hover:bg-[#34D399] hover:text-gray-800 duration-200 text-gray-200 text-base font-semibold" :class="{'text-gray-800 bg-[#34D399]': $route.path == '/examens'}">
                <svg class="mr-[5px]" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 48 48"><!-- Icon from All by undefined - undefined --><path fill="currentColor" fill-rule="evenodd" d="M39 13a3 3 0 0 0-3 3v2h6v-2a3 3 0 0 0-3-3m3 7h-6v16.5l3 4.5l3-4.5zM6 9v30a3 3 0 0 0 3 3h22a3 3 0 0 0 3-3V9a3 3 0 0 0-3-3H9a3 3 0 0 0-3 3m14 6a1 1 0 0 1 1-1h8a1 1 0 1 1 0 2h-8a1 1 0 0 1-1-1m1 3a1 1 0 1 0 0 2h8a1 1 0 1 0 0-2zm-1 10a1 1 0 0 1 1-1h8a1 1 0 1 1 0 2h-8a1 1 0 0 1-1-1m1 3a1 1 0 1 0 0 2h8a1 1 0 1 0 0-2zm-9-3v3h3v-3zm-1-2h5a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1h-5a1 1 0 0 1-1-1v-5a1 1 0 0 1 1-1m6.707-10.293a1 1 0 0 0-1.414-1.414L13 17.586l-1.293-1.293a1 1 0 0 0-1.414 1.414L13 20.414z" clip-rule="evenodd"/></svg>
                Liste des examens
            </li>
            <li @click="goToSallesPage()" class="my-[10px] rounded-[5px] cursor-pointer p-[10px] px-[20px] flex justify-start items-center w-full hover:bg-[#34D399] hover:text-gray-800 duration-200 text-gray-200 text-base font-semibold" :class="{'text-gray-800 bg-[#34D399]': $route.path == '/salles'}">
                <svg class="mr-[5px]" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M14 6v15H3v-2h2V3h9v1h5v15h2v2h-4V6zm-4 5v2h2v-2z"/></svg>
                Liste des salles
            </li>
            <li class="my-[10px] rounded-[5px] cursor-pointer p-[10px] px-[20px] flex justify-start items-center w-full hover:bg-[#34D399] hover:text-gray-800 duration-200 text-gray-200 text-base font-semibold">
                <svg class="mr-[5px]" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><g fill="none"><path d="m12.594 23.258l-.012.002l-.071.035l-.02.004l-.014-.004l-.071-.036q-.016-.004-.024.006l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427q-.004-.016-.016-.018m.264-.113l-.014.002l-.184.093l-.01.01l-.003.011l.018.43l.005.012l.008.008l.201.092q.019.005.029-.008l.004-.014l-.034-.614q-.005-.019-.02-.022m-.715.002a.02.02 0 0 0-.027.006l-.006.014l-.034.614q.001.018.017.024l.015-.002l.201-.093l.01-.008l.003-.011l.018-.43l-.003-.012l-.01-.01z"/><path fill="currentColor" d="M3 5c0-1.087.893-2.04 2.062-1.967a17 17 0 0 1 15.905 15.905C21.04 20.107 20.087 21 19 21H5a2 2 0 0 1-2-2z"/></g></svg>
                Filières & Promotions
            </li>
        </ul>

        <div class="w-full p-[20px] absolute bottom-0 left-0">
            <div class="my-[10px] rounded-[5px] cursor-pointer p-[10px] px-[20px] flex justify-start items-center w-full hover:bg-[#34D399] hover:text-gray-800 duration-200 text-gray-200 text-base font-semibold">
                <svg class="mr-[5px]" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><g fill="none"><path fill="currentColor" d="m2 12l-.78-.625l-.5.625l.5.625zm9 1a1 1 0 1 0 0-2zM5.22 6.375l-4 5l1.56 1.25l4-5zm-4 6.25l4 5l1.56-1.25l-4-5zM2 13h9v-2H2z"/><path stroke="currentColor" stroke-width="2" d="M10 8.132v-.743c0-1.619 0-2.428.474-2.987s1.272-.693 2.868-.96l1.672-.278c3.243-.54 4.864-.81 5.925.088C22 4.151 22 5.795 22 9.082v5.835c0 3.288 0 4.932-1.06 5.83c-1.062.9-2.683.63-5.926.089l-1.672-.279c-1.596-.266-2.394-.399-2.868-.958C10 19.039 10 18.229 10 16.61v-.545"/></g></svg>
                Se déconnecter
            </div>
        </div>
    </div>
    <div class="w-full lg:hidden fixed top-0 left-0 z-40 bg-white shadow-4xl h-[70px] flex items-center justify-center">
        <div class="container px-[20px] w-full flex items-center justify-between relative ">
            <h2 v-if="$route.path == '/dashboard'" class="text-sm font-bold text-gray-800">Tableau de bord</h2>
            <h2 v-if="$route.path == '/examens'" class="text-sm font-bold text-gray-800">Liste des examens</h2>
            <h2 v-if="$route.path == '/salles'" class="text-sm font-bold text-gray-800">Liste des salles</h2>
            <div class="text-3xl cursor-pointer flex lg:hidden text-gray-800" @click="toggleAdmin()">
                <i v-if="isMenu" class="fa-solid fa-xmark"></i>
                <i v-else class="fa-solid fa-bars"></i>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const isMenu = ref(false)
const router = useRouter()

const toggleAdmin = () => {
    isMenu.value = !isMenu.value
}

function goToDashboardPage () {
    router.push('/dashboard')
}
function goToExamensPage () {
    router.push('/examens')
}
function goToSallesPage () {
    router.push('/salles')
}
</script>

<style>

</style>