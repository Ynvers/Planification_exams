<template>
    <main class="flex items-start justify-center w-screen relative min-h-screen">
        <HeaderAdmin/>
        <div class="w-full relative lg:p-[50px] px-[20px] pt-[100px]">
            <h1 class="lg:text-5xl text-4xl font-bold text-gray-800">Salut, Mickaël !</h1>
            <p class="text-gray-500 mb-[25px]">
                Ici vous trouverez un récapitulatif de vos activités sur la plateforme ! Bonne planification à vous 
            </p>
            <div class="w-full flex md:flex-row flex-col items-center justify-between relative">
                <div class="md:w-[calc(100%/3-15px)] w-full my-[10px] lg:my-0 h-[180px] bg-[#34D399] rounded-[10px] p-[20px] shadow-7xl">
                    <h2 class="text-2xl font-bold text-gray-800 mb-[20px]">Planification d'Examens</h2>
                    <div class="hidden justify-between relative items-center mb-[10px] w-full">
                        <div class="flex flex-col items-center justify-start text-[10px] font-semibold text-gray-800">
                            <i class="fa-solid fa-clock-rotate-left text-xs"></i>
                            <span class="text-gray-800 font-bold text-xs">7</span>
                            <span>Planification réalisé</span>
                        </div>
                        <div class="flex flex-col items-center justify-start text-[10px] font-semibold text-gray-800">
                            <i class="fa-solid fa-bug text-xs"></i>
                            <span class="text-gray-800 font-bold text-xs">11%</span>
                            <span>Taux de chevauchements</span>
                        </div>
                    </div>
                    <button class="w-full p-[10px] rounded-[5px] text-sm font-bold text-gray-800 bg-white">
                        Faire une planification
                    </button>
                </div>
                <div class="md:w-[calc((100%-100%/3)-15px)] w-full my-[10px] lg:my-0 h-[180px] rounded-[10px] p-[20px] shadow-7xl"></div>
            </div>
        </div>
    </main>
</template>

<script setup>
import HeaderAdmin from '@/components/HeaderAdmin.vue';
</script>

<style>

</style>