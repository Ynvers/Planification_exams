<script setup>
import { ref } from "vue";
import axios from "axios";

const examens = ref([]);
const salles = ref([]);
const disponibilites = ref([]);
const globalHours = ref([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]);
const transition = ref(1);
const planningResponse = ref(null);
const errorMessage = ref("");

const addExam = () => {
  examens.value.push({ nom: "", duree: "", annee: "", filiere: "", nb_etudiants: "" });
};

const addSalle = () => {
  salles.value.push({ nom: "", capacite: "" });
};

const addDisponibilite = () => {
  disponibilites.value.push({ jour: "", salle: "", intervals: [["", ""]] });
};

const addInterval = (index) => {
  disponibilites.value[index].intervals.push(["", ""]);
};

const submitForm = async () => {
  try {
    const formattedData = {
      examens: Object.fromEntries(
        examens.value.map((exam) => [
          exam.nom,
          {
            duree: parseInt(exam.duree),
            annee: parseInt(exam.annee),
            filiere: exam.filiere,
            nb_etudiants: parseInt(exam.nb_etudiants),
          },
        ])
      ),
      salles: Object.fromEntries(
        salles.value.map((salle) => [
          salle.nom,
          {
            capacite: parseInt(salle.capacite),
          },
        ])
      ),
      disponibilites: disponibilites.value.reduce((acc, dispo) => {
        if (!acc[dispo.jour]) acc[dispo.jour] = {};
        acc[dispo.jour][dispo.salle] = dispo.intervals.map((i) => [parseInt(i[0]), parseInt(i[1])]);
        return acc;
      }, {}),
      global_hours: globalHours.value,
      transition: transition.value,
    };

    const response = await axios.post("http://localhost:8000/planifier", formattedData);
    planningResponse.value = response.data;
  } catch (error) {
    errorMessage.value = "Erreur lors de la planification.";
  }
};
</script>

<template>
  <div class="p-6 bg-white rounded-lg shadow-lg">
    <h2 class="text-2xl font-bold text-gray-800 mb-4">Planification des Examens</h2>

    <!-- Examens -->
    <div>
      <h3 class="text-lg font-semibold text-gray-700 mb-2">Examens</h3>
      <div v-for="(exam, index) in examens" :key="index" class="mb-3 flex gap-2">
        <input v-model="exam.nom" type="text" placeholder="Nom de l'examen" class="border p-2 rounded w-1/5">
        <input v-model="exam.duree" type="number" placeholder="Durée (h)" class="border p-2 rounded w-1/5">
        <input v-model="exam.annee" type="number" placeholder="Année" class="border p-2 rounded w-1/5">
        <input v-model="exam.filiere" type="text" placeholder="Filière" class="border p-2 rounded w-1/5">
        <input v-model="exam.nb_etudiants" type="number" placeholder="Nombre d'étudiants" class="border p-2 rounded w-1/5">
      </div>
      <button @click="addExam" class="bg-green-500 text-white px-4 py-2 rounded">Ajouter un examen</button>
    </div>

    <!-- Salles -->
    <div class="mt-6">
      <h3 class="text-lg font-semibold text-gray-700 mb-2">Salles</h3>
      <div v-for="(salle, index) in salles" :key="index" class="mb-3 flex gap-2">
        <input v-model="salle.nom" type="text" placeholder="Nom de la salle" class="border p-2 rounded w-1/2">
        <input v-model="salle.capacite" type="number" placeholder="Capacité" class="border p-2 rounded w-1/2">
      </div>
      <button @click="addSalle" class="bg-green-500 text-white px-4 py-2 rounded">Ajouter une salle</button>
    </div>

    <!-- Disponibilités -->
    <div class="mt-6">
      <h3 class="text-lg font-semibold text-gray-700 mb-2">Disponibilités</h3>
      <div v-for="(dispo, index) in disponibilites" :key="index" class="mb-3">
        <div class="flex gap-2">
          <input v-model="dispo.jour" type="text" placeholder="Jour (ex: Lundi)" class="border p-2 rounded w-1/3">
          <input v-model="dispo.salle" type="text" placeholder="Salle" class="border p-2 rounded w-1/3">
        </div>
        <div v-for="(interval, i) in dispo.intervals" :key="i" class="mt-2 flex gap-2">
          <input v-model="interval[0]" type="number" placeholder="Début (h)" class="border p-2 rounded w-1/2">
          <input v-model="interval[1]" type="number" placeholder="Fin (h)" class="border p-2 rounded w-1/2">
        </div>
        <button @click="addInterval(index)" class="bg-blue-500 text-white px-3 py-1 mt-2 rounded">Ajouter un créneau</button>
      </div>
      <button @click="addDisponibilite" class="bg-green-500 text-white px-4 py-2 rounded">Ajouter une disponibilité</button>
    </div>

    <!-- Bouton d'envoi -->
    <div class="mt-6">
      <button @click="submitForm" class="bg-blue-600 text-white px-6 py-3 rounded-lg font-bold">Planifier</button>
    </div>

    <!-- Message d'erreur -->
    <div v-if="errorMessage" class="mt-6 p-4 bg-red-100 border border-red-400 rounded text-red-800">
      {{ errorMessage }}
    </div>

    <div v-if="planningResponse" class="mt-6">
      <h3 class="text-lg font-bold mb-4">Planning des Examens</h3>
      <div class="overflow-x-auto">
        <table class="w-full border-collapse border border-gray-300">
          <thead>
            <tr class="bg-gray-100">
              <th class="border border-gray-300 p-2">Heure</th>
              <th v-for="jour in Object.keys(planningResponse.planning)" :key="jour" class="border border-gray-300 p-2">
                {{ jour }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="hour in globalHours" :key="hour" class="text-center">
              <td class="border border-gray-300 p-2 font-bold">{{ hour }}h</td>
              <td v-for="jour in Object.keys(planningResponse.planning)" :key="jour" class="border border-gray-300 p-2">
                <div v-for="exam in planningResponse.planning[jour].filter(e => e[0] === hour)" :key="exam[1]" class="bg-blue-100 text-blue-900 p-1 rounded">
                  <span class="font-semibold">{{ exam[1] }}</span> <br />
                  Salle: {{ exam[2] }} <br />
                  Année: {{ exam[3] }} <br />
                  Filière: {{ exam[4] }}
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
