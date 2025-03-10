<template>
    <HeaderComponent/>
    <section class="pt-[120px] py-[50px] h-[600px] bg-gray-800 flex items-start justify-center relative">
        <div class="container lg:max-w-[1024px] px-[20px] w-full relative flex items-center justify-between ">
            <div class="w-[calc(70%-10px)]">
                <h1 class="text-5xl capitalize text-white font-bold">
                    Optimisez la <span class="text-[#34D399]">Planification</span> de vos <span class="text-[#34D399]">Examens</span> avec <span class="text-[#34D399]">SmartExam</span>
                </h1>
            </div>
            <div class="w-[calc(30%-10px)] pl-[50px] border-l border-[#34D399]">
                <p class="text-gray-200 text-sm">
                    Gagnez du temps et réduisez les conflits d’horaires grâce à SmartExam, 
                    la solution intelligente qui automatise la planification des examens. 
                    Simplifiez l'organisation, évitez les chevauchements et assurez une 
                    répartition équilibrée des épreuves en quelques clics.
                </p>
                <ul class="flex items-center justify-between mt-[25px]">
                    <li class="flex flex-col justify-center items-center">
                        <svg class="text-[#34D399]" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 16 16"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M4.5 2A2.5 2.5 0 0 0 2 4.5v7A2.5 2.5 0 0 0 4.5 14h7a2.5 2.5 0 0 0 2.5-2.5v-7A2.5 2.5 0 0 0 11.5 2zM3 4.5A1.5 1.5 0 0 1 4.5 3h3v4.5H3zm0 4h4.5V13h-3A1.5 1.5 0 0 1 3 11.5zm5.5-1V3h3A1.5 1.5 0 0 1 13 4.5v3zm3.604 2.146a.5.5 0 0 1 0 .708l-1.5 1.5a.5.5 0 0 1-.708 0l-.75-.75a.5.5 0 0 1 .708-.708l.396.397l1.146-1.147a.5.5 0 0 1 .708 0"/></svg>
                        <span class="text-xs text-white text-center mt-[10px]">Simplicité d'utilisation</span>
                    </li>
                    <li class="flex flex-col justify-center items-center">
                        <svg class="text-[#34D399]" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M12 19.9q2.425-.75 4.05-2.962T17.95 12H12V4.125l-6 2.25v5.175q0 .175.05.45H12zm0 2q-.175 0-.325-.025t-.3-.075Q8 20.675 6 17.638T4 11.1V6.375q0-.625.363-1.125t.937-.725l6-2.25q.35-.125.7-.125t.7.125l6 2.25q.575.225.938.725T20 6.375V11.1q0 3.5-2 6.538T12.625 21.8q-.15.05-.3.075T12 21.9"/></svg>
                        <span class="text-xs text-white text-center mt-[10px]">Précision et fiabilité</span>
                    </li>
                    <li class="flex flex-col justify-center items-center">
                        <svg class="text-[#34D399]" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="m10.45 14.55l1.325 2.95q.075.15.225.15t.225-.15l1.325-2.95l2.95-1.325q.15-.075.15-.225t-.15-.225l-2.95-1.325l-1.325-2.95q-.075-.15-.225-.15t-.225.15l-1.325 2.95l-2.95 1.325q-.15.075-.15.225t.15.225l2.95 1.325ZM10 3q-.425 0-.712-.288T9 2q0-.425.288-.713T10 1h4q.425 0 .713.288T15 2q0 .425-.288.713T14 3h-4Zm2 19q-1.85 0-3.487-.713T5.65 19.35q-1.225-1.225-1.938-2.863T3 13q0-1.85.713-3.488T5.65 6.65q1.225-1.225 2.863-1.938T12 4q1.55 0 2.975.5t2.675 1.45l.7-.7q.275-.275.7-.275t.7.275q.275.275.275.7t-.275.7l-.7.7Q20 8.6 20.5 10.025T21 13q0 1.85-.713 3.488T18.35 19.35q-1.225 1.225-2.863 1.938T12 22Z"/></svg>
                        <span class="text-xs text-white text-center mt-[10px]">Gain de temps</span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="w-[80%] max-w-[850px] rounded-[20px] bg-white absolute bottom-[-150px] shadow-4xl h-[300px] left-[50%] translate-x-[-50%] flex items-center justify-center overflow-hidden">
            <img src="../assets/images/cta.jpg" alt="" class="absolute h-full w-full object-cover">
            <div class="w-full h-full absolute bg-gray-800/60 flex flex-col justify-center items-center">
                <svg class="text-[#34D399] mb-[10px]" xmlns="http://www.w3.org/2000/svg" width="42" height="42" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><g fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.95 16.264s-1.703 2.54-.707 3.535c.995.996 3.535-.707 3.535-.707"/><path fill="currentColor" fill-rule="evenodd" d="M20.506 3.536a1 1 0 0 1 .268.928l-.317 1.402a9 9 0 0 1-2.414 4.375l-4.644 4.644c1.027 1.272 1.36 2.48 1.1 3.632c-.271 1.2-1.16 2.086-1.712 2.637l-.06.06a1 1 0 0 1-1.564-.193L9.17 17.696a1 1 0 0 0-.15-.192l-2.57-2.568l-.76-.456l3.459-3.843l.007.005L13.8 6a9 9 0 0 1 4.376-2.414l1.402-.318a1 1 0 0 1 .928.269zM8.322 10.062c-.969-.565-1.9-.722-2.797-.52c-1.2.272-2.086 1.16-2.637 1.713l-.06.059a1 1 0 0 0 .193 1.564l1.796 1.078z" clip-rule="evenodd"/></g></svg>
                <button class="bg-[#34D399] text-gray-800 font-bold text-sm p-[10px] rounded-[5px] relative ">
                    Essayez SmartExam dès maintenant !
                </button>
            </div>
        </div>
    </section>
</template>

<script setup>
import HeaderComponent from '@/components/HeaderComponent.vue'
</script>

<style>

</style>