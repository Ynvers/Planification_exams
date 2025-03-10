# 📅 Planification Automatique des Examens – Web App

## 📌 Description  
Cette application web permet d’automatiser la planification des examens dans les établissements d'enseignement supérieur en optimisant l'affectation des ressources (salles, horaires, étudiants) tout en respectant diverses contraintes.  

Elle repose sur des **algorithmes d'optimisation** utilisant la **programmation par contraintes (CP)** et/ou la **programmation linéaire en nombres entiers (MILP)**.  

## 🎯 Objectifs  
✅ **Génération automatique** d’un planning des examens respectant toutes les contraintes.  
✅ **Interface web intuitive** pour la gestion des données et des contraintes.  
✅ **Flexibilité** : possibilité de modifier dynamiquement les paramètres (nombre de promotions, salles, etc.).  
✅ **Éviter les conflits** d’horaires et optimiser l'utilisation des infrastructures.  


## 🌍 Démonstration  
🚀 **Lien vers la démo** (à venir)  


## 🛠️ Fonctionnalités  
- **Interface web** pour saisir les données (examens, salles, étudiants).  
- **Génération automatique** d’un emploi du temps optimisé.  
- **Ajustements manuels** via l’interface si nécessaire.  
- **Téléchargement** du planning en format PDF/Excel.  
- **Authentification** (optionnelle) pour la gestion des accès.  


## 🔧 Contraintes et Objectif  
✔ **Capacité des salles** : respecter le nombre maximal d’étudiants.  
✔ **Disponibilité des ressources** : tenir compte des salles indisponibles.  
✔ **Non-chevauchement** : un étudiant ne peut avoir deux examens simultanément.  
✔ **Temps de transition** : prévoir une marge entre deux examens dans une salle.  
✔ **Optimisation** : minimiser la durée totale des examens.  


## 🏗️ Technologies utilisées  
- **Back-end** : FastAPI
- **Front-end** :  
- **Optimisation** : OR-Tools (Google)
- **Déploiement** :   


## 🚀 Installation  

### 1️⃣ **Cloner le projet**  
```bash
https://github.com/Ynvers/Planification_exams.git
cd Planification_exams
```
