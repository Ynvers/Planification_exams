<template>
    <HeaderComponent/>
    <section class="pt-[120px] py-[50px] lg:h-[600px] h-auto bg-gray-800 flex items-start justify-center relative">
        <div class="container lg:max-w-[1024px] px-[20px] w-full relative flex lg:flex-row flex-col items-center justify-between ">
            <div class="lg:w-[calc(70%-10px)] w-full mb-[15px] lg:mb-0">
                <h1 class="text-5xl capitalize text-white font-bold">
                    Optimisez la <span class="text-[#34D399]">Planification</span> de vos <span class="text-[#34D399]">Examens</span> avec <span class="text-[#34D399]">SmartExam</span>
                </h1>
            </div>
            <div class="lg:w-[calc(30%-10px)] w-full mt-[15px] lg:mt-0 lg:pl-[50px] pl-[20px] border-l border-[#34D399]">
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
        <div class="w-[80%] lg:flex max-w-[850px] rounded-[20px] bg-white absolute bottom-[-150px] shadow-4xl h-[300px] left-[50%] translate-x-[-50%] hidden items-center justify-center overflow-hidden">
            <img src="../assets/images/cta.jpg" alt="" class="absolute h-full w-full object-cover">
            <div class="w-full h-full absolute bg-gray-800/60 flex flex-col justify-center items-center">
                <svg class="text-[#34D399] mb-[10px]" xmlns="http://www.w3.org/2000/svg" width="42" height="42" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><g fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.95 16.264s-1.703 2.54-.707 3.535c.995.996 3.535-.707 3.535-.707"/><path fill="currentColor" fill-rule="evenodd" d="M20.506 3.536a1 1 0 0 1 .268.928l-.317 1.402a9 9 0 0 1-2.414 4.375l-4.644 4.644c1.027 1.272 1.36 2.48 1.1 3.632c-.271 1.2-1.16 2.086-1.712 2.637l-.06.06a1 1 0 0 1-1.564-.193L9.17 17.696a1 1 0 0 0-.15-.192l-2.57-2.568l-.76-.456l3.459-3.843l.007.005L13.8 6a9 9 0 0 1 4.376-2.414l1.402-.318a1 1 0 0 1 .928.269zM8.322 10.062c-.969-.565-1.9-.722-2.797-.52c-1.2.272-2.086 1.16-2.637 1.713l-.06.059a1 1 0 0 0 .193 1.564l1.796 1.078z" clip-rule="evenodd"/></g></svg>
                <button @click="goToRegisterPage()" class="bg-[#34D399] text-gray-800 font-bold text-sm p-[10px] rounded-[5px] relative ">
                    Essayez SmartExam dès maintenant !
                </button>
            </div>
        </div>
    </section>
    <section class="w-full flex items-center justify-center relative pb-[50px] pt-[50px] lg:pt-0 lg:mt-[220px]">
        <div class="container px-[20px] lg:max-w-[1024px] relative flex flex-wrap justify-between items-center">
            <div class="md:w-[calc(100%/4-20px)] w-[calc(50%-20px)] lg:h-[150px] h-[100px] relative flex items-center justify-center p-[20px]">
                <img src="../assets/images/uac.jpg" alt="" class="grayscale w-full h-full absolute object-contain">
            </div>
                
            <div class="md:w-[calc(100%/4-20px)] w-[calc(50%-20px)] lg:h-[150px] h-[100px] relative flex items-center justify-center p-[20px]">
                <img src="../assets/images/num.jpg" alt="" class="grayscale w-full h-full absolute object-contain">
            </div>
                
            <div class="md:w-[calc(100%/4-20px)] w-[calc(50%-20px)] lg:h-[150px] h-[100px] relative flex items-center justify-center p-[20px]">
                <img src="../assets/images/gouv.jpg" alt="" class="grayscale w-full h-full absolute object-contain">
            </div>
                
            <div class="md:w-[calc(100%/4-20px)] w-[calc(50%-20px)] lg:h-[150px] h-[100px] relative flex items-center justify-center p-[20px]">
                <img src="../assets/images/ifri.png" alt="" class="grayscale w-full h-full absolute object-contain">
            </div>
                
        </div>
    </section>
    <section class="w-full flex items-center justify-center relative py-[50px]">
        <div class="container lg:max-w-[1024px] w-full px-[20px] relative flex lg:flex-row flex-col items-center justify-between">
            <div class="lg:w-[calc(50%-10px)] w-full mb-[15px] lg:mb-0">
                <div class="w-full h-[300px] rounded-[20px] flex items-center justify-center relative overflow-hidden">
                    <img src="../assets/images/about.jpg" alt="" class="absolute h-full w-full object-cover">
                    <div class="w-full h-full absolute bg-gray-800/50"></div>
                </div>
            </div>
            <div class="lg:w-[calc(50%-10px)] w-full mt-[15px] lg:mt-0">
                <h2 class="text-[#34D399] font-bold text-sm uppercase">À propos</h2>
                <p class="text-4xl font-bold text-gray-800 mb-[20px]">
                    Pourquoi SmartExam ?
                </p>
                <p class="text-sm text-gray-600 font-semibold">
                    Chez SmartExam, nous croyons que la gestion des examens ne doit 
                    pas être un casse-tête. Conçu pour les établissements scolaires, 
                    universités et organismes d’examen, notre outil utilise des algorithmes 
                    avancés pour organiser les sessions de manière optimale.
                </p>
                <ul class="mt-[20px]">
                    <li class="my-[10px] font-bold text-base flex items-center justify-start relative">
                        <svg class="text-green-600 mr-[5px]" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="m9.55 15.15l8.475-8.475q.3-.3.7-.3t.7.3t.3.713t-.3.712l-9.175 9.2q-.3.3-.7.3t-.7-.3L4.55 13q-.3-.3-.288-.712t.313-.713t.713-.3t.712.3z"/></svg>
                        Planification rapide et efficace
                    </li>
                    <li class="my-[10px] font-bold text-base flex items-center justify-start relative">
                        <svg class="text-green-600 mr-[5px]" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="m9.55 15.15l8.475-8.475q.3-.3.7-.3t.7.3t.3.713t-.3.712l-9.175 9.2q-.3.3-.7.3t-.7-.3L4.55 13q-.3-.3-.288-.712t.313-.713t.713-.3t.712.3z"/></svg>
                        Évitez les conflits d’horaires
                    </li>
                    <li class="my-[10px] font-bold text-base flex items-center justify-start relative">
                        <svg class="text-green-600 mr-[5px]" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="m9.55 15.15l8.475-8.475q.3-.3.7-.3t.7.3t.3.713t-.3.712l-9.175 9.2q-.3.3-.7.3t-.7-.3L4.55 13q-.3-.3-.288-.712t.313-.713t.713-.3t.712.3z"/></svg>
                        Optimisé pour les universités et écoles
                    </li>
                </ul>
            </div>
        </div>
    </section>
    <section class="w-full flex items-center justify-center relative py-[50px] my-[50px] bg-gray-800">
        <div class="container lg:max-w-[1024px] px-[20px] w-full relative flex items-center justify-center flex-col">
            <h2 class="text-[#34D399] font-bold text-sm uppercase">Services</h2>
            <p class="text-4xl font-bold text-white max-w-[650px] mb-[50px] text-center">
                Nos solutions pour une planification sans stress
            </p>
            <ul>
                <li class="text-xl text-white py-[20px] border-t-[0.5px] border-b-[0.5px] relative flex items-center justify-between">
                    <p>
                        <span class="font-bold">Planification automatisée – </span> Générez des emplois du temps d'examens optimisés en quelques secondes.
                    </p>
                    <div class="w-[30px] h-[30px] rounded-[50%] border border-white text-white ml-[20px] min-w-[30px] flex items-center justify-center">
                        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M12.525 18.025q-.5.325-1.012.038T11 17.175V13H3q-.425 0-.712-.288T2 12t.288-.712T3 11h8V6.825q0-.6.513-.888t1.012.038l8.15 5.175q.475.3.475.85t-.475.85z"/></svg>
                    </div>
                </li>
                <li class="text-xl text-white py-[20px] border-t-[0.5px] border-b-[0.5px] relative flex items-center justify-between">
                    <p>
                        <span class="font-bold">Évitez les conflits –</span> SmartExam détecte et ajuste automatiquement les chevauchements d'épreuves.
                    </p>
                    <div class="w-[30px] h-[30px] rounded-[50%] border border-white text-white ml-[20px] min-w-[30px] flex items-center justify-center">
                        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M12.525 18.025q-.5.325-1.012.038T11 17.175V13H3q-.425 0-.712-.288T2 12t.288-.712T3 11h8V6.825q0-.6.513-.888t1.012.038l8.15 5.175q.475.3.475.85t-.475.85z"/></svg>
                    </div>
                </li>
                <li class="text-xl text-white py-[20px] border-t-[0.5px] border-b-[0.5px] relative flex items-center justify-between">
                    <p>
                        <span class="font-bold">Personnalisation avancée –</span> Adaptez les paramètres selon les besoins de votre établissement.
                    </p>
                    <div class="w-[30px] h-[30px] rounded-[50%] border border-white text-white ml-[20px] min-w-[30px] flex items-center justify-center">
                        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M12.525 18.025q-.5.325-1.012.038T11 17.175V13H3q-.425 0-.712-.288T2 12t.288-.712T3 11h8V6.825q0-.6.513-.888t1.012.038l8.15 5.175q.475.3.475.85t-.475.85z"/></svg>
                    </div>
                </li>
                <li class="text-xl text-white py-[20px] border-t-[0.5px] border-b-[0.5px] relative flex items-center justify-between">
                    <p>
                        <span class="font-bold">Tableaux de bord et suivi –</span> Accédez à des statistiques et rapports détaillés.
                    </p>
                    <div class="w-[30px] h-[30px] rounded-[50%] border border-white text-white ml-[20px] min-w-[30px] flex items-center justify-center">
                        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M12.525 18.025q-.5.325-1.012.038T11 17.175V13H3q-.425 0-.712-.288T2 12t.288-.712T3 11h8V6.825q0-.6.513-.888t1.012.038l8.15 5.175q.475.3.475.85t-.475.85z"/></svg>
                    </div>
                </li>
                <li class="text-xl text-white py-[20px] border-t-[0.5px] border-b-[0.5px] relative flex items-center justify-between">
                    <p><span class="font-bold">Notifications et rappels –</span> Informez étudiants et enseignants en temps réel.</p>
                    <div class="w-[30px] h-[30px] rounded-[50%] border border-white text-white ml-[20px] min-w-[30px] flex items-center justify-center">
                        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M12.525 18.025q-.5.325-1.012.038T11 17.175V13H3q-.425 0-.712-.288T2 12t.288-.712T3 11h8V6.825q0-.6.513-.888t1.012.038l8.15 5.175q.475.3.475.85t-.475.85z"/></svg>
                    </div>
                </li>
            </ul>
        </div>
    </section>
    <section class="py-12 bg-white flex items-center justify-center relative">
        <div class="container px-[20px] relative w-full max-w-4xl  mx-auto">
            <h2 class="text-3xl font-bold text-gray-800 text-center mb-6">Contactez-nous</h2>
            <p class="text-gray-600 text-center mb-8">
                Remplissez le formulaire ci-dessous et nous vous répondrons dès que possible.
            </p>

            <form class="bg-gray-100 p-6 rounded-lg">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-gray-700 font-medium mb-1">Nom</label>
                        <input type="text" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#34D399]" placeholder="Votre nom">
                    </div>
                    <div>
                        <label class="block text-gray-700 font-medium mb-1">Prénoms</label>
                        <input type="text" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#34D399]" placeholder="Vos prénoms">
                    </div>
                </div>

                <div class="mt-4">
                    <label class="block text-gray-700 font-medium mb-1">Email</label>
                    <input type="email" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#34D399]" placeholder="Votre email">
                </div>

                <div class="mt-4">
                    <label class="block text-gray-700 font-medium mb-1">Numéro de téléphone</label>
                    <input type="tel" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#34D399]" placeholder="Votre numéro">
                </div>

                <div class="mt-4">
                    <label class="block text-gray-700 font-medium mb-1">Sujet</label>
                    <input type="text" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#34D399]" placeholder="Sujet de votre message">
                </div>

                <div class="mt-4">
                    <label class="block text-gray-700 font-medium mb-1">Message</label>
                    <textarea rows="5" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#34D399]" placeholder="Votre message"></textarea>
                </div>

                <div class="mt-6 text-center">
                    <button type="submit" class="bg-[#34D399] text-white font-medium py-3 px-6 rounded-lg hover:bg-[#2AA67F] transition duration-300">
                        Envoyer
                    </button>
                </div>
            </form>
        </div>
    </section>
    <section class="w-full my-[100px] flex items-center justify-center relative">
        <div class="container w-full flex items-center justify-center relative px-[20px]">
            <div class="w-full flex md:flex-row flex-col items-start justify-between relative">
                <div class="md:w-[calc(40%-10px)] w-full my-[10px]">
                    <h2 class="md:text-5xl text-2xl font-bold text-gray-800">
                        Des questions ?
                        <br>
                        Nous avons les réponses
                    </h2>
                    <p class="md:mt-[50px] mt-[25px] md:text-xl text-sm text-gray-500 font-semibold">
                        Découvrez notre FAQ ci-dessous pour tout savoir sur notre plateforme et nos services.
                        Si vous avez encore des doutes, n'hésitez pas à nous contacter directement
                    </p>
                </div>
                <div class="md:w-[calc(60%-10px)] w-full my-[10px]">
                    <div class="max-w-[850px]">
                        <div
                        v-for="(item, index) in faqItems"
                        :key="index"
                        class="border rounded-[5px] my-[10px] overflow-hidden bg-white"
                        >
                            <div
                            class="flex justify-between items-center px-4 py-3 cursor-pointer"
                            :class="{ 'bg-gray-100': item.isOpen }"
                            @click="toggleFAQ(index)"
                            >
                                <h3 class="text-lg font-semibold text-gray-800">
                                    {{ item.question }}
                                </h3>
                                <div class="text-gray-500">
                                    <span v-if="item.isOpen">−</span>
                                    <span v-else>+</span>
                                </div>
                            </div>
                            <div
                            v-if="item.isOpen"
                            class="px-4 py-3 text-gray-600 text-sm overflow-hidden transition-all duration-300"
                            >
                                {{ item.answer }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <FooterComponent/>
</template>

<script setup>
import HeaderComponent from '@/components/HeaderComponent.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import FooterComponent from '@/components/FooterComponent.vue';

const router = useRouter()

function goToRegisterPage () {
    router.push('/register')
}

const faqItems = ref([
  {
    question: "SmartExam est-il adapté aux universités et lycées ?",
    answer: "Oui, SmartExam est conçu pour s’adapter aux établissements d’enseignement supérieur, aux lycées et aux centres d’examen professionnels.",
    isOpen: true,
  },
  {
    question: "Comment fonctionne la planification automatique ?",
    answer: "Notre algorithme analyse les disponibilités, évite les conflits et génère un emploi du temps optimisé en quelques secondes.",
    isOpen: false,
  },
  {
    question: "Peut-on personnaliser les paramètres des examens ?",
    answer: "Oui ! Vous pouvez définir des contraintes, comme la durée des épreuves, les salles disponibles et les groupes d'étudiants.",
    isOpen: false,
  },
  {
    question: "Comment essayer SmartExam ?",
    answer: "Contactez-nous pour une démonstration gratuite et découvrez comment SmartExam peut révolutionner votre organisation.",
    isOpen: false,
  },
]);

const toggleFAQ = (index) => {
  faqItems.value[index].isOpen = !faqItems.value[index].isOpen;
};
</script>

<style>

</style>