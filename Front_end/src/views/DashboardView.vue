<template>
    <main class="flex items-start justify-center w-screen relative min-h-screen">
        <HeaderAdmin/>
        <div class="w-full relative p-[50px]">
            <div class="w-full flex items-center justify-between relative">
                <div class="w-[calc(100%/3-15px)] h-[180px] rounded-[10px] p-[20px] shadow-7xl"></div>
                <div class="w-[calc(100%/3-15px)] h-[180px] rounded-[10px] p-[20px] shadow-7xl"></div>
                <div class="w-[calc(100%/3-15px)] h-[180px] rounded-[10px] p-[20px] shadow-7xl"></div>
            </div>
        </div>
    </main>
</template>

<script setup>
import HeaderAdmin from '@/components/HeaderAdmin.vue';
</script>

<style>

</style>