<template>
    <main class="flex items-start justify-center w-screen relative min-h-screen">
        <HeaderAdmin/>
        <div class="w-full relative lg:p-[50px] pt-[100px] px-[20px]">
            <div class="w-full flex items-center justify-between mb-[50px] relative">
                <h2 class="text-2xl font-bold text-gray-800">
                    Liste des salles
                </h2>
                <button @click="toggleAjout()" class="bg-gray-800 font-bold text-sm text-[#34D399] p-[10px] rounded-[5px]">Ajouter</button>
            </div>
            <div class="w-full flex flex-col items-center justify-center relative">
                <div class="w-full flex items-center justify-between bg-gray-100 relative">
                    <div class="text-gray-800 lg:flex hidden text-sm font-bold w-[50px] border-gray-800 border-l-[0.5px] border-r-[0.5px] p-[10px]">
                        ID
                    </div>
                    <div class="text-gray-800 text-sm font-bold w-[30%] lg:w-[20%] border-gray-800 border-l-[0.5px] border-r-[0.5px] p-[10px]">
                        Capacité
                    </div>
                    <div class="text-gray-800 text-sm font-bold w-[35%] lg:w-[40%] border-gray-800 border-l-[0.5px] border-r-[0.5px] p-[10px]">
                        <span class="md:flex hidden">Heure d'ouverture</span><span class="md:hidden">Début</span>
                    </div>
                    <div class="text-gray-800 text-sm font-bold w-[35%] lg:w-[calc(40%-50px)] border-gray-800 border-l-[0.5px] border-r-[0.5px] p-[10px]">
                        <span class="md:flex hidden">Heure de Fermeture</span><span class="md:hidden">Fin</span>
                    </div>
                </div>
                <div class="h-[100px] w-full flex items-center justify-center text-sm font-bold text-gray-800 border-[0.5px] border-t-0 border-gray-800">
                    Aucune salle disponible !
                </div>
            </div>
        </div>
        <div :class="{'translate-x-0': isAjout, 'translate-x-[120%]': !isAjout}" class="w-[calc(100%-40px)] max-w-[400px] duration-300 lg:h-[calc(100vh-40px)] h-[calc(100vh-110px)] lg:top-[20px] top-[90px] right-[20px] bg-white rounded-[20px] p-[20px] fixed shadow-4xl">
            <div class="flex items-center justify-between pb-[15px] border-b border-gray-200">
                <h3 class="text-sm font-bold text-gray-800">Ajouter une salle</h3>
                <button @click="toggleAjout()" class="w-[30px] h-[30px] rounded-[50%] bg-gray-100 flex items-center justify-center relative">
                    <i class="fa-solid fa-xmark text-gray-800"></i>
                </button>
            </div>
        </div>
    </main>
</template>

<script setup>
import HeaderAdmin from '@/components/HeaderAdmin.vue';
import { ref } from 'vue'

const isAjout = ref(false)

const toggleAjout = () => {
    isAjout.value = !isAjout.value
}
</script>

<style>

</style>