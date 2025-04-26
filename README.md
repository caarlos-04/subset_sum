# Subset Sum Problem 🧮

Aquest projecte implementa solucions per al **Subset Sum Problem**, un problema clàssic de la teoria de la complexitat computacional, NP-complet.

Inclou:
- Solució amb **programació dinàmica** (top-down amb memoization)
- Solució amb **força bruta**
- **Generador d’instàncies** d'entrada

---

## 📋 Estructura del projecte

- `brute_force.py`: Resol el problema amb força bruta.
- `dp.py`: Resol el problema amb programació dinàmica (amb memoization).
- `generator.py`: Crea fitxers `.txt` amb instàncies aleatòries.
- `README.md`: Documentació del projecte.

---

## 🚀 Com usar-ho

1. **Clona el repositori:**
   ```bash
   git clone https://github.com/nom-usuari/subset-sum-problem.git
   cd subset-sum-problem
2. **Genera una instancia:**
   ```bash
   python3 generator.py num_elements valor_maxim
  ```
   Això generarà un fitxer nums.txt
3. **Resol amb força bruta:**
   ```bash
   python3 brute_force.py nums.txt
   ```
   Es mostrarà si existeix solució, en cas de que si, quants subconjunts ho compleixen
4. **Resol amb programació dinàmica:**
   ```bash
   python3 dp.py nums.txt
   ```
   Es mostrarà si existeix solució, en cas de que si, quants subconjunts ho compleixen

---

## 📚 Sobre el Subset Sum Problem

El **Subset Sum Problem** demana si, donat un conjunt de nombres enters i un valor objectiu, existeix algun subconjunt la suma del qual sigui exactament aquest valor.

És un problema **NP-complet**, i està relacionat amb altres problemes importants com el **Knapsack Problem**, el **Partition Problem** i el **3-SAT**.

---

## 🛠️ Requisits

- Python 3.7 o superior

---

## ✨ Crèdits

Creat per **Pol Masip** i **Carlos Mazarico**.  
Projecte desenvolupat com a part de l'assignatura Models de Computació i Complexitat de la Universtiat de Lleida.

---

## 🔗 Bibliografia

- [Subset Sum Problem — Wikipedia](https://en.wikipedia.org/wiki/Subset_sum_problem)
- [GeeksforGeeks — Subset Sum Problem (DP-25)](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)

---

## 🎥 Extra

Aquest codi s'ha utilitzat per preparar un vídeo didàctic explicant el **Subset Sum Problem** i les seves aplicacions pràctiques.


