<template>
    <div class="w-full h-screen flex items-center justify-center relative p-[20px] bg-gray-200">
        <div class="w-full h-auto max-w-[550px] max-h-[calc(100%-100px)] bg-white rounded-[10px] p-[20px] md:px-[50px] flex items-center justify-center flex-col">
            <h2 class="md:text-3xl text-2xl font-bold text-gray-800 text-center">
                Bienvenue sur SmartExam
            </h2>
            <p class="text-sm font-semibold text-gray-500">
                Enregistrez vous maintenant !
            </p>
            <form class="w-full relative mt-[25px]">
                <div class="w-full my-[15px] relative">
                    <label for="" class="text-sm font-bold text-gray-800 mb-[5px]">Email <span class="text-red-600">*</span></label>
                    <input type="text" class="w-full p-[10px] rounded-[5px] text-sm outline-none border border-gray-200" placeholder="Ex: alain@gmail.com">
                </div>
                <div class="w-full relative md:flex items-center justify-between">
                    <div class="md:w-[calc(50%-15px)] w-full my-[15px] relative">
                        <label for="" class="text-sm font-bold text-gray-800 mb-[5px]">Mot de passe <span class="text-red-600">*</span></label>
                        <input type="password" class="w-full p-[10px] rounded-[5px] text-sm outline-none border border-gray-200" placeholder="************">
                    </div>
                    <div class="md:w-[calc(50%-15px)] w-full my-[15px] relative">
                        <label for="" class="text-sm font-bold text-gray-800 mb-[5px]">Confirmer le Mot de passe <span class="text-red-600">*</span></label>
                        <input type="password" class="w-full p-[10px] rounded-[5px] text-sm outline-none border border-gray-200" placeholder="************">
                    </div>
                </div>
                <div class="w-full my-[20px] relative">
                    <button type="submit" class="w-full p-[10px] text-sm font-bold rounded-[5px] bg-[#34D399] text-gray-800 ">
                        S'inscrire
                    </button>
                </div>
            </form>
            <p class="text-xs font-bold text-gray-600">
                Vous avez déjà un compte ? 
                <button @click="goToLoginPage()" class="text-[#34D399] hover:underline duration-200">
                    Se connecter
                </button>
            </p>
        </div>
    </div>
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